
import os, platform

 

try:

 

        import requests

 

except:

 

        os.system('pip2 install requests')
 

bit = platform.architecture()[0]

 

if bit == "64bit":

        os.system('xdg-open https://youtube.com/@teach-alamin')

 

        import mrmafia

 

        MRMAFIA_Main()

 

elif bit == "32bit":

        os.system('xdg-open https://youtube.com/@teach-alamin')

 

        import mrmafia32

 

        MRMAFIA_Main()
