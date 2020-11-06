import os
import time

print("this is for uninstalling libraries used.")

try:
    import pygame
except:
    print("pygame already absent")
    time.sleep(1)
continue:
    input("press enter to remove pygame")
    os.system('python -m pip uninstall pygame')

try:
    import pypresence
except:
    print("pypresence already absent")
    time.sleep(1)
continue:
    input("press enter to remove pypresence")
    os.system('python -m pip uninstall pypresence')

print("setup completed.")
time.sleep(5)