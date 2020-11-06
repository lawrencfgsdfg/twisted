import os
import time

try:
    import pygame
except:
    input("pygame is missing. press enter to install\n")
    os.system('python -m pip install pygame')
    time.sleep(1)
else:
    print("pygame is already installed.")
    time.sleep(1)

try:
    import pypresence
except:
    input("pypresence is missing. press enter to install\nNOTE: only install if wanting discord RPC support\n")
    os.system('python -m pip install pypresence')
    time.sleep(1)
else:
    print("pypresence is already installed.")
    time.sleep(1)

"""
try:
    import pyTwistyScrambler
except:
    input("pyTwistyScrambler is missing. press enter to install\n")
    os.system('python -m pip install pyTwistyScrambler')
    time.sleep(1)
else:
    print("pyTwistyScrambler is already installed.")
    time.sleep(1)
"""

print("setup completed.")
time.sleep(5)