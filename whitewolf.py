import os
import colorama
import platform
if platform.platform == "Windows":
   os.system("title WHİTE WOLF")
import wikipedia
print("""  
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
           ser = input("Ara:")
           ss = wikipedia.summary(ser)
           print(colorama.Fore.GREEN+ss)
       except:
           print(colorama.Fore.RED+"BÖYLE BİR ŞEY YOK"+colorama.Fore.GREEN)
        
        