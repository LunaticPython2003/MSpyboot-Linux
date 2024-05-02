import os
import sys
import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel('DarkGrey13')

def root_check(user = os.geteuid):
    if user != 0:
        sg.Popup("The script will only work as root!")
        sys.exit(0)

def preloader():
    window.close()
    root_check()
    os.system("get_files.sh")
    sg.Popup("System will reboot in 3 seconds. Enroll the kernel from hashtool upon reboot")
    time.sleep(3)
    os.system("reboot")

def run_grub():
    window.close()
    root_check()
    os.system('grub_install.sh')
    exit()

layout = [[sg.Text('Select your distro: '), sg.Combo(['Ubuntu/Debian', 'Arch', 'Fedora'])],
           [sg.Text('Select a method: '), sg.Radio('With GRUB', 1), sg.Radio('Without GRUB', 1)],
           [sg.Checkbox('I agree to proceed ahead with the installation script')],
           [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Secure Boot', layout)

while True:
    event, values = window.read()
    print(values)
    if values[1] is True:
        preloader()
    else:
        run_grub()

    if event in (None, 'Cancel'):
         exit()
