# MSpyboot-Linux (work in progress)

 A simple Python script to enable secure boot in Linux distros that DO NOT originally support the feature. <br />
 It works with the help of <b> Linux Foundation's secure UEFI secure boot system </b> <br />
 `Source - https://blog.hansenpartnership.com/linux-foundation-secure-boot-system-released/ `
 
 ## Current Status
 The script currently has the following capabilities :-
 - Achieves secure boot without GRUB (with Preloader)
 - Should work on all Linux distros (Tested on Ubuntu and Arch)
 - Has a GUI menu for conviniece (not fully complete)
 
 ## Running the script
 ### Installing dependencies
 `pip install -r requirements.txt `
 
 ### Running the script
 `python ./main.py`
 
 ## TODO
 - [x] Support for distros beyond Ubuntu
 - [ ] Support for GRUB
 - [ ] Better GUI interface 
 - [ ] Implementation of other solutions if the default fails
 - [ ] Proper Python packaging
