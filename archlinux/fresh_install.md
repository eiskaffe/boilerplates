# What to do after completing a fresh arch linux isntallation
This list aims to help after installing arch linux for a faster start

## 1 - Install LTS kernel
Check the current kernel
```terminal
uname -r
```
Install LTS kernel
```terminal
sudo pacman -S linux-lts
```

(optional) Remove non-LTS kernel
```terminal
sudo pacman -Rs linux
```

## 2 - Install microcode
For Intel processors:
```terminal
sudo pacman -S intel-ucode
```

For AMD processors:<br>
install the linux-firmware package

## 3 - Disable GRUB delay
Append this to the `/etc/default/grub` file
```
# achieve the fastest possible boot:
GRUB_FORCE_HIDDEN_MENU="true"
```
Download 31_hold_shift
```terminal
curl -LO https://raw.githubusercontent.com/eiskaffe/scripts/main/archlinux/31_hold_shift
```
Then move the file to the correct location using
```terminal
sudo mv 31_hold_shift /etc/grub.d/
```
Make it executeable
```terminal
chmod a+x /etc/grub.d/31_hold_shift 
```
Reconfigure GRUB (run this even if you did not do this step)
```terminal
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

## 4 - Set up a firewall
Install UFW
```terminal
sudo pacman -S ufw
```
Start and enable UFW
```terminal
sudo ufw enable
```
```terminal
sudo ufw status verbose
```
Enable the start-up on system start
```terminal
sudo systemctl enable ufw.service
```

## 5 - Remove orphans
```terminal
sudo pacman -Rns $(pacman -Qtdq)
```
