import os, sys, platform

try:
    os.system('git pull')
except:
    pass

try:
    os.system('xdg-open https://www.youtube.com/@mafiams16')
except:
    pass

bit = platform.architecture()[0]

try:
    if bit == '64bit':
        __import__("mrmafia")._____Exception()
    else:
        __import__("mrmafia32")._____Exception()
except Exception as e:
    exit(f"[X] Error: {e}")
