# import pyTwistyScrambler
# from pyTwistyScrambler import scrambler222
import time
import sys
import random

# discord rpc init, and prevent crash
discordRunning = "false"

try:
    import pygame
    pygame.init()
except:
    print("pygame fucked")

# here for when the module just decides not to fucking work and i have to debug shit and not wait for RPC to work
# basically, make True for when you want discord, False if you don't care
if True:
    try:
        from pypresence import Presence
        client_id = '770513436735569940' 
        RPC = Presence(client_id)
        RPC.connect()
        print("discord rpc running")
        discordRunning = "true"
    except:
        print("pypresence fucked")
        discordRunning = "false"

# screen shit
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()

# done is running var, also version shit here
done = False
version = "v0.1"
pygame.display.set_caption('twisted ' + version)

font = pygame.font.SysFont("Arial", 16)

# render text... well, no shit
def rendertext(t, xpos, ypos, size, center, r, g, b, centerypos):
    font = pygame.font.SysFont("Arial", size)
    text = font.render(t, True, (r, g, b))
    text_rect = text.get_rect(center=(320, 180))
    if not center:
        screen.blit(text,(xpos, ypos))
    else:
        if centerypos > 0:
            text_rect = text.get_rect(center=(320, centerypos))
            screen.blit(text,text_rect)
        else:
            screen.blit(text,text_rect)
    pygame.display.flip()

def renderrect(xpos, ypos, width, height):
    rect = pygame.Rect(xpos, ypos, width, height)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    pygame.display.flip()
    

# update rpc
def doRPC(d, s):
    try:
        RPC.update(details=d, state=s, large_image="thing", large_text=version + "; by lawrencfgsdfg")
    except:
        print("tried updating RPC, failed")


screen.fill((0, 0, 0))
rendertext("twisted " + version, 4, 4, 16, False, 75, 75, 75, 0)
rendertext("twisted " + version, 3, 3, 16, False, 255, 255, 255, 0)
rendertext("lawrencfgsdfg", 4, 21, 10, False, 75, 75, 75, 0)
rendertext("lawrencfgsdfg", 3, 20, 10, False, 255, 255, 255, 0)

doRPC(version, "testing")
# rpc update

finalscramble = ""
active = 0

def waitSpaceUp():
    global starting
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                doRPC("solving", finalscramble)
                starting = time.time()
                print("space up, timer start")
                renderrect(0, 70, 620, 200)
                rendertext("solve", 0, 0, 48, True, 255, 255, 255, 0)
                active = 1
                waitSpaceTime()
                

def waitSpace():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # second space
                return

def waitSpaceTime():
    global active
    global ending
    # check timer state
    if active == 1:
        # timer state was running, now is stopped.
        waitSpace()
        active = 0
        ending = time.time()
        timed = round((ending - starting)/0.01)*0.01
        print("second space, timer stop, solve " + str(timed))
        doRPC("solved in " + str(timed), finalscramble)
        renderrect(145, 70, 350, 200)
        rendertext(str(timed), 0, 0, 48, True, 255, 255, 255, 0)
        getScramble()
        waitSpaceTime()
    else:
        # timer state was stopped, now is running.
        active = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    rect = pygame.Rect(0, 70, 640, 200)
                    pygame.draw.rect(screen, (0, 0, 0), rect)
                    rendertext("waiting", 0, 0, 48, True, 255, 255, 255, 0)
                    print("initial space down, waiting")
                    waitSpaceUp()
                    return

OLDSCRAMBLE = ""
finalscramble = ""
def getScramble():
    # don't ask me how the FUCK this works
    print("\n")
    global OLDSCRAMBLE
    global finalscramble
    
    renderrect(0, 290, 640, 50)
    
    char = ["F", "R", "U"]
    char2 = ["B", "L", "D"]
    scramble = []
    currentchar = ""
    lastchar = "temp"
    
    i = 0
    while i < 6:
        rand = random.randint(1, 3)
        currentchar = random.randint(0, 2)
        while currentchar == lastchar:
            print("currentchar is same as last one")
            currentchar = random.randint(0, 2)
        lastchar = currentchar
        
        if rand == 1:
            currentchar = char[currentchar] + "'"
        elif rand == 2:
            currentchar = char[currentchar] + "2"
        else:
            currentchar = char[currentchar]
        print(currentchar + " appended")
        scramble.append(currentchar)
        
        rand = random.randint(1, 3)
        currentchar = random.randint(0, 2)
        while currentchar == lastchar:
            print("currentchar is same as last one")
            currentchar = random.randint(0, 2)
        lastchar = currentchar
    
        if rand == 1:
            currentchar = char2[currentchar] + "'"
        elif rand == 2:
            currentchar = char2[currentchar] + "2"
        else:
            currentchar = char2[currentchar]
        print(currentchar + " appended")
        scramble.append(currentchar)
        
        i = i + 1
    
    print("\n\nfinal generated scramble: " + ' '.join(scramble))
    OLDSCRAMBLE = finalscramble
    finalscramble = (' '.join(scramble))
    
    rendertext("current: " + str(finalscramble), 0, 100, 18, True, 255, 255, 255, 300)
    
    if not OLDSCRAMBLE == "":
        rendertext("old: " + str(OLDSCRAMBLE), 0, 300, 18, True, 100, 100, 100, 320)

rendertext("ready", 0, 0, 48, True, 255, 255, 255, 0)

running = 0
startTime = "bruh"
finalTime = "bruh"
i = 0

pygame.display.flip()
getScramble()
waitSpaceTime()