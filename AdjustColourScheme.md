To adjust colours of output, You need to edit fmts variable in configuration file (default to ~/.clipf/clipf.conf)
To see colour examples with corresponding codes, try this in the console:
```
for i in 0 1 2 3 4 5 6 7 ; do echo -e "\033[3${i}m\\\\033[3${i}m\033[0m" ; done
for i in 0 1 2 3 4 5 6 7 ; do echo -e "\033[3${i};1m\\\\033[3${i};1m\033[0m" ; done
```

You can read more about terminal control sequences here: http://www.termsys.demon.co.uk/vtansi.htm

Terminal colour adjustments, depend of Your terminal emulator. For
Urxvt, You can use this recipe:

Put this in Your ~/.XDefaults:
```
URxvt.color4: #067eff
URxvt.color12: #6699d4
URxvt.background: black
URxvt.foreground: #c1cdcd
```
Colours color0 to color7 mean thin font and color8 to color15 mean
bold font. Colour codes like `#067eff` are in RGB. You can select
appropriate codes for example in Gimp.

Now put this:
```
xrdb ~/.XDefaults
```
in Your ~/.xinitrc file, before WM start.