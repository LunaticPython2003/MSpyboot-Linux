#! /bin/bash

cd /tmp 
wget https://blog.hansenpartnership.com/wp-uploads/2013/PreLoader.efi # Gets the Preloader file
wget https://blog.hansenpartnership.com/wp-uploads/2013/HashTool.efi # Gets the hashtool
sudo cp ./Preloader.efi /boot/efi/EFI/systemd/PreLoader.efi
sudo cp ./HashTool.efi /boot/efi/EFI/HashTool.efi

sudo cd /boot/efi/EFI/systemd
mv ./systemd-bootx64.efi ./loader.efi
cp ./preloader.efi ./systemd-bootx64.efi
#efibootmgr --verbose --disk /dev/sdX --part Y --create --label "PreLoader" --loader /boot/efi/EFI/systemd/PreLoader.efi