import os
import distro
import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel('DarkGrey13')

def run_deb(flag):
    window.close()
    if flag is True:
        os.system("sudo apt install efibootmgr")
        os.system("get_files.sh")
        sg.Popup("System will reboot in 3 seconds. Enroll the kernel from hashtool upon reboot")
        time.sleep(3)
        os.system("init 6")
    else:
        print("GRUB installation not implemented at the moment")
        exit()

layout = [[sg.Text('Select your distro: '), sg.Combo(['Ubuntu/Debian', 'Arch', 'Fedora'])],
           [sg.Text('Select a method: '), sg.Radio('With GRUB', 1, default=True), sg.Radio('Without GRUB', 2)],
           [sg.Checkbox('I agree to proceed ahead with the installation script')],
           [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Secure Boot', layout)

while True:
    event, values = window.read()
    print(values)
    if values[0] == 'Ubuntu/Debian':
        run_deb(values[1])
    elif values[0] == 'Arch':
        run_pac(values[1])
    
    if event in (None, 'Cancel'):
         exit()