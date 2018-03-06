

##Wallpaper Changer for Openbox & Conky

Added by me: 
- Removed spaces at the end of the conky
- Conky fitted to my system
- removed unused files
- added script to generate a second conky showing the shortcuts from rc.xml


### Original

> This contains two shell scripts, and there are a few options to get these working. Timechanger.sh is a script that I grabbed and modded from a comment on stackoverflow. It just runs in the background when you add it to ~/.config/openbox/autostart.sh and changes every X minutes. That's a possibility, but the 'best practices' way would probably be to set up a cron job to execute wallchange.sh.

> Wallchange.sh itself is just running the feh command to grab a random wallpaper from your folder and change it. Combined with ~/.config/openbox/rc.xml, you can bind it to a keybind (as in the example rc.xml) to change your wallpaper at will.

> It uses imagemagick convert to convert your wallpaper into a 1x1 image, and then inverts the color (for use with conky text colors.)

> .conkyrc is a modified version of HaxOS

> Scripts for imagemagick/etc based on scripts posted on reddit by user maybe_born_with_it, but converted for use with feh and so on.

