import time
import sys
import random

ascii_art = """
╭━╮╭━┳━━━┳━━━┳━━━╮╭╮╱╭┳━━━┳━━━┳╮╭━┳━━┳━╮╱╭┳━━━╮╭━━━┳━━━┳━━━┳━━━━╮
┃┃╰╯┃┃╭━━┫╭━╮┃╭━╮┃┃┃╱┃┃╭━╮┃╭━╮┃┃┃╭┻┫┣┫┃╰╮┃┃╭━╮┃┃╭━╮┃╭━╮┃╭━━┫╭╮╭╮┃
┃╭╮╭╮┃╰━━┫┃╱╰┫┃╱┃┃┃╰━╯┃┃╱┃┃┃╱╰┫╰╯╯╱┃┃┃╭╮╰╯┃┃╱╰╯┃╰━━┫┃╱┃┃╰━━╋╯┃┃╰╯
┃┃┃┃┃┃╭━━┫┃╭━┫╰━╯┃┃╭━╮┃╰━╯┃┃╱╭┫╭╮┃╱┃┃┃┃╰╮┃┃┃╭━╮╰━━╮┃┃╱┃┃╭━━╯╱┃┃
┃┃┃┃┃┃╰━━┫╰┻━┃╭━╮┃┃┃╱┃┃╭━╮┃╰━╯┃┃┃╰┳┫┣┫┃╱┃┃┃╰┻━┃┃╰━╯┃╰━╯┃┃╱╱╱╱┃┃
╰╯╰╯╰┻━━━┻━━━┻╯╱╰╯╰╯╱╰┻╯╱╰┻━━━┻╯╰━┻━━┻╯╱╰━┻━━━╯╰━━━┻━━━┻╯╱╱╱╱╰╯
"""

print(ascii_art)


def print_slowly(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(duration=3):
    print("Loading", end="")
    for _ in range(duration):
        time.sleep(0.5)
        print(".", end="")
    print()

def code_cascade(duration=3, intense=False):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    end_time = time.time() + duration
    while time.time() < end_time:
        line_length = 60 if not intense else random.randint(40, 80)
        code_line = ''.join(random.choice(chars) for _ in range(line_length))
        print(code_line)
        time.sleep(0.05 if not intense else 0.02)

def simulate_hacking(option):
    if option == 1: #Esta es la parte de Crackear windows------------------------------------------------------------
        print_slowly("Initializing Windows hack tool...")
        loading_animation()
        hackwindows = -1
        while Opcionmenu != 0:
        
            print(' 1. Cracking my WINDOWS 7 '
                + ' \n 2. Cracking my WINDOWS 8  '
                + ' \n 3. Cracking my WINDOWS 10 '
                + ' \n 4. Cracking my WINDOWS 11 '
                + ' \n 0. Exit')
            hackwindows = -1
            
            try:
                hackwindows = int(input("Enter the number of your Windows menu: "))
                
                
                if hackwindows == 1:
                        print_slowly("Initializing Windows 7 hack tool...")
                        loading_animation()
                        print_slowly("Bypassing security protocols...")
                        code_cascade(3)
                        print_slowly("Downloading sensitive data...")
                        code_cascade(2)
                        print_slowly("---------Your Windows 7 was activated successfully.---------")
                        break
                elif hackwindows == 2:    
                        print_slowly("Initializing Windows 8 hack tool...")
                        loading_animation()
                        print_slowly("Bypassing security protocols...")
                        code_cascade(3)
                        print_slowly("Downloading sensitive data...")
                        code_cascade(2)
                        print_slowly("---------Your Windows 8 was activated successfully.---------")
                        break
                elif hackwindows == 3:    
                        print_slowly("Initializing Windows 10 hack tool...")
                        loading_animation()
                        print_slowly("Bypassing security protocols...")
                        code_cascade(3)
                        print_slowly("Downloading sensitive data...")
                        code_cascade(2)
                        print_slowly("---------Your Windows 10 was activated successfully.---------")
                        break
                elif hackwindows == 4:    
                        print_slowly("Initializing Windows 11 hack tool...")
                        loading_animation()
                        print_slowly("Bypassing security protocols...")
                        code_cascade(3)
                        print_slowly("Downloading sensitive data...")
                        code_cascade(2)
                        print_slowly("---------Your Windows 11 was activated successfully.---------")
                        break
                elif hackwindows == 0:
                    print("Exiting now...")
                    break
                else:
                    print("Invalid option, please try again.")
            except ValueError:
                print("Please enter a valid number.")
                
    elif option == 2: #Esta es la parte de Crackear MS OFFICE------------------------------------------------------------
        print_slowly("Initializing MS Office crack tool...")
        loading_animation()
        hackoffice = input("Enter your email: ")
        print_slowly("Bypassing security protocols...")
        code_cascade(3)
        print_slowly("Downloading sensitive data...")
        code_cascade(2)
        print_slowly("---Your MS OFFICE has been successfully activated for Email:\n"+ hackoffice +"---")
        
    elif option == 3: #Esta es la parte de Crackear MS OFFICE------------------------------------------------------------
        print_slowly("Connecting to WhatsApp server...")
        loading_animation()
        hackwas = input("Enter your WhatsApp number: ")
        hackwas2 = input("Enter your victim's number: ")
        print_slowly("Intercepting messages...")
        code_cascade(3)
        print_slowly("Decrypting conversations...")
        code_cascade(2)
        print("\n-------------------------------------------------\n" 
              + hackwas 
              + ": [11:50 a.m., 30/8/2024] \nEl Brayan: Ole manin, como estas? Ve manito tenes de pronto\n20k que me prestes te los pago mañana?\n"
              +"\n"+ hackwas2 
              + ": [1:32 p.m., 30/8/2024] \nFern ☕: Hola bro, aun los necesitas?\n-----------------------------------------------------------")
    elif option == 4: #Esta es la parte de hack computers------------------------------------------------------------
        hackpc = input("Enter the IP of your neighbor's, friend's or colleague's computer: ")
        
        print_slowly("Attempting to access neighbor's computer...")
        loading_animation()
        print_slowly("Scanning for open ports...")
        code_cascade(3)
        print_slowly("Gaining access to files...")
        code_cascade(2)
        print_slowly("""
        \n-------------------------------------------------\n
        
        
        
        Adaptador de Ethernet:

        Ip Public. . . . . . . . . . . . . . . .  : """+ hackpc + """
        Vínculo: dirección IPv6 local. . . . . .  : fe83::f199:334b:55b4:e888%11
        Dirección IPv4. . . . . . . . . . . . . . : 192.138.66.106
        Máscara de subred . . . . . . . . . . . . : 255.255.255.0
        Puerta de enlace predeterminada . . . . . : 192.138.66.122
        
        
        ACCESS POINT:::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        SSH -o """+ hackpc + """  -u DuquePresi -p guerrilleroHP3*
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        
        YOU ARE CONNECTED!!!
        
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        
        
        PS C:/DISCOLOCAL/IDE>
        
        
        \n-------------------------------------------------\n
        
        """)
    elif option == 5: #Esta es la parte de Crackear MS OFFICE------------------------------------------------------------
        print_slowly("Scanning for Wi-Fi networks...")
        loading_animation()
        print_slowly("""
        \n-------------------------------------------------\n
        
        
        
               
        ACCESS POINT:::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        
        SSID: IE_INEM2024   PASSWORD: Emcali1234xd
        
        
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        
        YOU ARE CONNECTED!!!
        
        :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        
        \n-------------------------------------------------\n
        
        """)
        print_slowly("Cracking Wi-Fi password...")
        code_cascade(3)
        print_slowly("Connecting to network...")
        
    elif option == 6: #Esta es la parte de Crackear MS OFFICE------------------------------------------------------------
        print_slowly("Resetting or damaging device...")
        loading_animation()
        print_slowly("Overloading system resources...")
        code_cascade(2, intense=True)
        print_slowly("Corrupting critical files...")
        code_cascade(2, intense=True)
        print_slowly("System malfunction imminent!")
        code_cascade(3, intense=True)
        print_slowly("Critical error! Device shutdown imminent!")
        print("""
        \n-------------------------------------------------\n
        
        
███████╗ █████╗ ██████╗ ██╗   ██╗███████╗██████╗     ██████╗████████╗██╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██║   ██║██╔════╝██╔══██╗   ██╔════╝╚══██╔══╝██║██╔═══██╗
███████╗███████║██████╔╝██║   ██║█████╗  ██████╔╝   ██║  ███╗  ██║   ██║██║   ██║
╚════██║██╔══██║██╔═══╝ ██║   ██║██╔══╝  ██╔══██╗   ██║   ██║  ██║   ██║██║   ██║
███████║██║  ██║██║     ╚██████╔╝███████╗██║  ██║██╗╚██████╔╝  ██║   ██║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ 
                                                                                
                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿            ⣿⣿⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
                   ⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
                   ⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⣿⣿⣿⣿⣿⣿⣿⣧⠀
                   ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⣿⣿⣿⣿⣿⣿⣿⣿⡇
                   ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                   ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿  ⣿⣿⣿⣿⡇
                   ⠀⠀⠀⠀⢿⣿⣿⣿⣿   ⣿⣿⣿⣿⣿⣿⣿  ⣿⣿⣿⣿⠃
                   ⠀⠀⠀⠀⠸⣿⣿⣿⣿    ⣿⣿⣿⣿⣿     ⣿⣿⡟⠀
                   ⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀
                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀

        ERROR CRÍTICO: WINDOWS ha encontrado un problema irrecuperable y necesita reiniciar.
        
        
        \n-------------------------------------------------\n
        
        """)

    

# Inicializar con un valor que asegure la entrada al bucle

Opcionmenu = -1

while Opcionmenu != 0:
    
    print('\nThis is a software that emulates computer hacking of systems, developer by Diego Plata IDEO X' 
          + ' \n 1. Cracking my WINDOWS 7 / 8 / 10 / 11 '
          + ' \n 2. Cracking my MS OFFICE 365 '
          + ' \n 3. Hacking a WhatsApp'
          + ' \n 4. Hacking my neighbor, friend or partner\'s computer'
          + ' \n 5. Hacking my work or school WIFI network'
          + ' \n 6. Reset or Damage device'
          + ' \n 0. Exit')
    
    try:
        Opcionmenu = int(input("Enter the menu number: "))
        
        if Opcionmenu in range(1, 7):
            simulate_hacking(Opcionmenu)
        elif Opcionmenu == 0:
            print("Exiting now...")
            break
        else:
            print("Invalid option, please try again.")
    except ValueError:
        print("Please enter a valid number.")

print("Bye my bro and sorry!!!")
