## Build sbctl from source
git clone https://github.com/foxboron/sbctl.git
cd sbctl
make

echo "Check if you are in setup mode!"
sudo sbctl status

read -p "Are you in setup? (y/n)? " choice
case ${choice:0:1} in
    y|Y )
        sudo sbctl create-keys;
        sudo sbctl enroll-keys;
        echo 'default_uki="/boot/EFI/Linux/Arch.efi"' > /etc/mkinitcpio.d/linux.preset; ##Specify the path for the UKI
        sudo mkinitcpio -P; ##Compile the Unified Kernel Image
        sudo sbctl sign -s /boot/EFI/Linux/Arch.efi; ##Sign the Image
        sudo sbctl sign -s /boot/EFI/Linux/*; ##Alternatively sign all the efi files
        reboot;
    ;;
    * )
        echo No
    ;;
esac
