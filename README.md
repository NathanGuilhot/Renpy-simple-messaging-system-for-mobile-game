# Renpy | Simple messaging system for mobile game
A simple messaging system for texting-based mobile game, such as "LifeLine" or "Bury me, my Love"; it's based on the NVL mode and it's really easy to use!


It's a follow up to [my previous phone system](https://github.com/NightenDushi/yet-another-phone-for-renpy), but with a vertical layout and some other improvements, such as choices directly available in the phone interface.

## Setup
Built for a 1080x1920 (portrait) game; see the FAQ for landscape/PC.
1. Copy into your `game/` folder:
   - `PhoneTexting.rpy`
   - `images/phone_background.png`, `phone_foreground.png`, `phone_send_frame.png`, `phone_received_frame.png`, `phone_send_icon.png`, `phone_received_icon.png`, `continue_btn.png`
   - `audio/SendText.ogg`, `audio/ReceiveText.ogg` (only if you use the sound callbacks)
2. In `screens.rpy`, edit the `nvl` screen:
```renpy
screen nvl(dialogue, items=None):

    #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
    ####
    ## Indent the rest of the screen
        window:
            style "nvl_window"
            # ...
```
3. In `gui.rpy`: `define gui.nvl_list_length = None` (keeps every message).
4. Set your MC's name in `PhoneTexting.rpy`: `default MC_Name = "Nighten"`.
5. Make `kind=nvl` characters speak:
```renpy
define n_nvl = Character("Nighten", kind=nvl, callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)
```
- Emojis and pictures: use an `{image=...}` tag, sized for the phone screen.
- To get the regular NVL screen back, set `nvl_mode` to anything else (e.g. `"classic"`).

⚠ Only the phone is made for portrait; the rest of the UI (menus, save screens) is the default Ren'Py UI with some bigger text.

## FAQ

**My MC's messages show on the wrong side / I use a player-entered name.**
`MC_Name` must match the displayed name. It can be a list, and `[player_name]`-style names work (substituted before comparing):
```renpy
default MC_Name = ["[player_name]", "Nighten"]
```
Or mark any character as the MC: `Character("[player_name]", kind=nvl, who_style="phone_mc")`.

**Dialogue appears in the normal textbox, not the phone.**
The character isn't an NVL character. Add `kind=nvl`.

**The phone disappears.**
Expected: the phone is the NVL screen, so it hides while a normal (ADV) character speaks. It comes back, with its history, on the next NVL line.

**Text is invisible or uses the wrong font.**
Your game's default text style is leaking in (e.g. white text on a white bubble). Set the phone styles explicitly (next question).

**How do I change fonts, colours, bubble width or background?**
Text styles: `phone_narrator_text`, `phone_name_text`, `phone_mc_text`, `phone_other_text`. Bubble styles: `phone_mc_bubble`, `phone_other_bubble`.
```renpy
style phone_mc_text:
    font "myfont.ttf"
    color "#fff"
style phone_other_bubble:
    background Frame("my_bubble.png", 23, 23)
    padding (20, 20)
    xsize 700
```
The phone itself is `phone_background.png` / `phone_foreground.png`: replace the images.

**Per-character avatars?**
Key by displayed name; anyone missing uses the default icon:
```renpy
define phone_icons = {"Eileen": "eileen_icon.png"}
```

**Choices inside the phone?**
Use `menu (nvl=True):`. A plain `menu:` shows the normal overlay choice.

**How do I clear messages / have separate conversations?**
`nvl clear` empties the phone. For a separate history per contact:
```renpy
default phone_threads = {}
init python:
    def phone_open(name):
        store.nvl_list = store.phone_threads.setdefault(name, [])
```
Call `$ phone_open("Eileen")` before that conversation; call it again after any `nvl clear`.

**Can I use it in a landscape / PC game?**
Yes. Cap the phone's width and it is centred (keep it ≥ 700, bubbles have a fixed width):
```renpy
define phone_width = 800
```

**Which files do I copy?**
See [Setup](#setup) step 1. The `gui/phone/` folder is Ren'Py's own mobile GUI, not this phone.

[Browser demo on itch](https://nighten.itch.io/renpy-simple-messaging-system-for-mobile-game)
[Original post on Lemmasoft](https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=63458#p547793)
[Mirror download on my website](https://nighten.fr/files/phone_messenger_fullscreen/)

If you have any issue or question, please let me know! I hope this will help you!!

And if you need more help for your project, [you can hire me as a programmer!](https://lemmasoft.renai.us/forums/viewtopic.php?f=66&t=61647) :) ✨
Have a nice day!
