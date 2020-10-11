#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Made by fernandomaroto for EndeavourOS and Portergos.
# Should work in any arch-based distros
# Trying K.I.S.S filosophy

import subprocess
import libcalamares
from pathlib import Path

root_mount_point = libcalamares.globalstorage.value("rootMountPoint")

def update_db():

    # Hope is simpler this way

    START_HAVEGED = "haveged -w 1024"
    PACMAN_INIT = "pacman-key --init"
    PACMAN_POPULATE = "pacman-key --populate"
    #PACMAN_REFRESH = "pacman-key --refresh-keys --keyserver hkp://ipv4.pool.sks-keyservers.net:11371"
    PACMAN_REFRESH = "/usr/bin/rank_pacman_key.sh"
    STOP_HAVEGED = "pkill haveged"
    BACKUP_MIRROLIST = "cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak"
    #BEST_MIRRORS = "reflector --verbose --age 8 --fastest 128 --latest 64 --number 32 --sort rate --save /etc/pacman.d/mirrorlist"
    BEST_MIRRORS = "reflector --verbose -a1 -f10 -l70 -phttps --sort rate --save /etc/pacman.d/mirrorlist"

    RANK_MIRRORS = "/usr/bin/update-mirrorlist"

    # Update database, step by step in the running iso only. Necessary if running old iso version
    subprocess.call(START_HAVEGED.split(' ')) 
    subprocess.call(PACMAN_INIT.split(' '))  
    subprocess.call(PACMAN_POPULATE.split(' ')) 

    #try:
    subprocess.call([PACMAN_REFRESH])
    #except:
    #    pass

    subprocess.call(STOP_HAVEGED.split(' '))   
    subprocess.call(BACKUP_MIRROLIST.split(' '))  

#############################################################
    update_mirrors_installed = Path("/usr/bin/update-mirrorlist")

    try:
        if not update_mirrors_installed.exists():
            subprocess.call(BEST_MIRRORS.split(' '))
        else:
            #subprocess.call([BEST_MIRRORS], shell=True)
            subprocess.call([RANK_MIRRORS, '||', BEST_MIRRORS], shell=True)
    except:
        pass

#############################################################
    

    # After the above there is no need to run cmds again in case the user tries to launch calamares a second time

    try:
        open('/tmp/run_once', 'a')
        run_once.close()
    except:
        pass
    
def run():
    """
    Installing base filesystem. Please wait! It may take some time!
    """

    # created new function above to update, populate, refresh, best mirrors etc
    
    executed_before = Path("/tmp/run_once")

    try:
        if not executed_before.exists():
            update_db()
    except:
        pass

    # Install base system + endeavouros packages + copy necessary config files

    PACSTRAP = "/usr/bin/pacstrap_calamares -c"
    PACKAGES = "base sudo grub endeavouros-keyring endeavouros-mirrorlist grub2-theme-endeavouros xterm"
    OLD_BASE = "mkinitcpio mkinitcpio-busybox mkinitcpio-nfs-utils diffutils inetutils jfsutils less logrotate man-db man-pages mdadm nano netctl perl s-nail sysfsutils systemd-sysvcompat texinfo usbutils vi which linux linux-firmware device-mapper"
    FILESYSTEM_TOOLS = "cryptsetup e2fsprogs f2fs-tools btrfs-progs lvm2 reiserfsprogs xfsprogs"

    RSYNC_CMD = "rsync -vaRI"
    CHROOT_CLEANER_SCRIPT = "/usr/bin/chrooted_cleaner_script.sh"
    CLEANER_SCRIPT = "/usr/bin/cleaner_script.sh"
    PACMAN_CONF = "/etc/pacman.conf"
    PACMAN_MIRRORS = "/etc/pacman.d/mirrorlist"
    GRUB_CONFIG = "/etc/default/grub" # /etc/default/grub removed from cleaner scripts - last step at calamares
    # https://forum.endeavouros.com/t/calamares-3-2-24-needs-testing/4941/37

    subprocess.call(PACSTRAP.split(' ') + [root_mount_point] + PACKAGES.split(' ') + OLD_BASE.split(' ') + FILESYSTEM_TOOLS.split(' '))

    subprocess.call(RSYNC_CMD.split(' ') + [CHROOT_CLEANER_SCRIPT] + [root_mount_point])
    subprocess.call(RSYNC_CMD.split(' ') + [CLEANER_SCRIPT] + [root_mount_point])
    subprocess.call(RSYNC_CMD.split(' ') + [PACMAN_CONF] + [root_mount_point])

    subprocess.call(RSYNC_CMD.split(' ') + [PACMAN_MIRRORS] + [root_mount_point])
    subprocess.call(RSYNC_CMD.split(' ') + ["/tmp/run_once"] + [root_mount_point])
    subprocess.call(RSYNC_CMD.split(' ') + [GRUB_CONFIG] + [root_mount_point])
   
