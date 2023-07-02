import os
import colorama
import platform
if platform.platform == "Windows":
   os.system("title WHİTE WOLF")
import wikipedia
print(colorama.Fore.GREEN+"""  
░██╗░░░░░░░██╗██╗░░██╗██╗████████╗███████╗
░██║░░██╗░░██║██║░░██║██║╚══██╔══╝██╔════╝
░╚██╗████╗██╔╝███████║██║░░░██║░░░█████╗░░
░░████╔═████║░██╔══██║██║░░░██║░░░██╔══╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝

░██╗░░░░░░░██╗░█████╗░██╗░░░░░███████╗
░██║░░██╗░░██║██╔══██╗██║░░░░░██╔════╝
░╚██╗████╗██╔╝██║░░██║██║░░░░░█████╗░░
░░████╔═████║░██║░░██║██║░░░░░██╔══╝░░
░░╚██╔╝░╚██╔╝░╚█████╔╝███████╗██║░░░░░
░░░╚═╝░░░╚═╝░░░╚════╝░╚══════╝╚═╝░░░░░""")
wikipedia.set_lang("Tr")
while True:
       try:
           ser = input(colorama.Fore.GREEN+"Ara:")
           ss = wikipedia.summary(ser)
           print(colorama.Fore.GREEN+ss)
       except:
           print(colorama.Fore.RED+"BÖYLE BİR ŞEY YOK"+colorama.Fore.GREEN)
        
        