import time
import sys
import random
import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# WOW functions are inefficient. i'm a lazy person i'll fix it later

try: from scrambler import *
except: print("> scrambler.py not found\n")

try: import pygame; pygame.init()
except: input("> pygame not installed, enter to exit\n")

# you can change this to disable RPC attempts.
discordRunning = False;
if False:
    try:
        from pypresence import Presence
        RPC = Presence('770513436735569940' )
        print("> trying rpc...")
        RPC.connect()
        discordRunning = True
    except: print("> rpc failed.")

# render text obviously
def rendertext(t, xpos, ypos, size, center, hexcolor, dobold, doitalic, doblit, r=-1, g=-1, b=-1):
    font = pygame.font.SysFont("arial", size, bold=dobold, italic=doitalic)
    text = font.render(t, True, pygame.Color(hexcolor))
    if r > 0 or g > 0 or b > 0: text = font.render(t, True, (r, g, b))
    text_rect = text.get_rect(center=(320, 180))
    if center == False: screen.blit(text,(xpos, ypos))
    else:
        if center == True: screen.blit(text,text_rect)
        else:
            text_rect = text.get_rect(center=(320, center))
            screen.blit(text,text_rect)
    clock.tick(100)
    if doblit: pygame.display.flip()

def renderrect(xpos, ypos, width, height, doblit, hexcolor, center):
    rect = pygame.Rect(xpos, ypos, width, height)
    if center: rect.center = (320, 180)
    pygame.draw.rect(screen, pygame.Color(hexcolor), rect)
    if doblit: pygame.display.flip()

# update rpc
def doRPC(d, s):    
    try: RPC.update(details=d, state=s, large_image="thing", large_text=version + "; by lawrencfgsdfg")
    except: return

def waitSpaceUp():
    global starting
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                doRPC("solving", currentscr)
                starting = time.time()
                print("space up, timer start")
                active = 1
                waitSpaceTime()
            if event.type == pygame.QUIT: RPC.close(); pygame.quit(); sys.exit();

def waitSpace():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: return
            if event.type == pygame.QUIT: RPC.close(); pygame.quit(); sys.exit();
        renderrect(0, 0, 200, 70, False, '#0e0e1c', True)
        rendertext(str(format(time.time() - starting, '.2f')), 0, 0, 48, True, '#8096c8', False, False, True) # abs(math.cos(float(format(time.time() - starting, '.2f')))*128), 120, 200

def waitSpaceTime():
    global active, ending, timelog # check timer state here
    if active == 1: # timer was running, now stopped
        waitSpace()
        active = 0
        ending = time.time()
        timed = format(ending - starting, '.2f')
        doRPC("solved in " + str(timed), currentscr)
        renderrect(0, 0, 200, 70, False, '#0e0e1c', True)
        rendertext(str(timed), 0, 0, 48, True, '#8096c8', False, False, True, 128, 150, 200)
        scramble()
        waitSpaceTime()
    else: # timer was stopped, now waiting
        active = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    renderrect(0, 0, 200, 70, False, '#0e0e1c', True)
                    rendertext("waiting", 0, 0, 48, True, '#8096c8', False, False, True)
                    print("initial space down, waiting")
                    waitSpaceUp() # start timing
                    return
                if event.type == pygame.QUIT: RPC.close(); pygame.quit(); sys.exit();

def scramble():
    global currentscr
    # renderrect(0, 290, 290, 40, False, 'black', True)
    renderrect(170, 270, 300, 40, False, '#0e0e1c', False)
    try:
        oldscr = currentscr
        currentscr = getScramble(10)
        rendertext("current: " + currentscr, 0, 0, 17, 280, '#8096c8', False, False, True)
        if not oldscr == "": rendertext("old: " + oldscr, 0, 0, 17, 300, '#205252', False, False, True)
    except: rendertext("scrambler.py missing", 0, 0, 17, 290, '#ff6464', False, False, True)

# basic init
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
version = "v0.2"
pygame.display.set_caption('twisted ' + version)
currentscr = "none"
active = 0

screen.fill((23, 23, 46))
renderrect(175, 275, 300, 40, False, '#05050a', False) # scramble
renderrect(225, 150, 200, 70, False, '#05050a', False) # ready shadow
renderrect(0, 0, 200, 70, False, '#0e0e1c', True) # ready
rendertext("ready", 0, 0, 48, True, '#8096c8', 0, False, False)

doRPC(version, "testing")
rendertext("twisted " + version, 2, 1, 12, False, '#27274f', False, False, False)
rendertext("discord rpc running: " + str(discordRunning), 2, 347, 10, False, '#0e0e1c', 0, False, False)
scramble()
waitSpaceTime()
