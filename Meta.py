import os,sys,random

os.system('clear')

logo2 = """
\x1b[1;96m /$$$$$$$        
| $$__  $$              | $
| $$  \ $$  /$$$$$$$ /$$$$$$$$
| $$$$$$$  /$$__  $$ |_  $$_/
| $$__    | $$$$$$$$    |  $
| $$  \ $ | $$____$$   |  $ 
| $$    $/|  $$$$_$ $_| |  $ $
|_______/  \_______/    \___/
                                        """
logo3 = '\x1b[0;35m \n      \x1b[0;33\n       \x1b[101m\x1b[37;>

print logo2 + logo3
nmbr = str(random.randint(11111, 99999))
be = '\x1b[1;92mBeta-Successful'
logo1 = """ | """
k = str('1000000')
c = str('786000')
for n in range(60):
    print be +  logo1 +k+nmbr + logo1 + c
