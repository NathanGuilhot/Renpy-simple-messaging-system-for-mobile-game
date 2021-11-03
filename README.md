# Renpy | Simple messaging system for mobile game
A simple messaging system for texting-based mobile game, such as "LifeLine" or "Bury me, my Love"; it's based on the NVL mode and it's really easy to use!


It's a follow up to [my previous phone system](https://github.com/NightenDushi/yet-another-phone-for-renpy), but with a vertical layout and some other improvements, such as choices directly available in the phone interface.

## Instruction
- This project is optimized for 1080x1920 resolution
- Add the images and *PhoneTexting.rpy* to your project
- In this file, change the name of the main character to yours (MC_Name)
- Edit the nvl screen in screen.rpy as follow:

```renpy
screen nvl(dialogue, items=None):      #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
     if nvl_mode == "phone":
         use PhoneDialogue(dialogue, items)
     else:
     ####
     ## Indent the rest of the screen
         window:
             style "nvl_window"
             # ...
```
- Change gui.nvl_list_length in gui.rpy to None, so that all the message are shown
- Now you just have to make a NVL character speak :)
- To include emojis and pictures, you can simply use an image tag; make sure they are the right size for the phone screen.

⚠ Note that the rest of the UI is not optimized for vertical game; you'd have to edit most of the screens to provide a pleasant experience to the player. I hope this phone will be a good starting point tho!
(in this project I only increased the size of some text to make it testable)

[Browser demo on itch](https://nighten.itch.io/renpy-simple-messaging-system-for-mobile-game)
[Original post on Lemmasoft](https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=63458#p547793)
[Mirror download on my website](https://nighten.fr/files/phone_messenger_fullscreen/)

If you have any issue or question, please let me know! I hope this will help you!!

And if you need more help for your project, [you can hire me as a programmer!](https://lemmasoft.renai.us/forums/viewtopic.php?f=66&t=61647) :) ✨
Have a nice day!
