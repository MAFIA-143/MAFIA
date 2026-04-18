import os, sys, platform
try:os.system('git pull')
except:pass
try:os.system('xdg-open https://www.youtube.com/@mafiams16')
except:pass
bit = platform.architecture()[0]
try:
    if bit == '64bit':
        import mrmafia
        mrmafia._____Exception()
    if bit == '32bit':
        import mrmafia32
        mrmafia32._____Exception()
except Exception as e:
    exit(str(e))
