# Here's the code for the phone!

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
default MC_Name = "Nighten" ##The name of the main character (or a list of names), used to place them on the screen. Can be "[player_name]"
define phone_icons = {} ##Optional icon per character, e.g. {"Sarah": "sarah_icon.png"}

init -1 python:

    # Is this message from the main character?
    def phone_is_mc(d):
        if d.who_args.get("style") == "phone_mc":
            return True
        names = MC_Name if isinstance(MC_Name, (list, tuple)) else [MC_Name]
        return d.who in [renpy.substitute(name) for name in names]

    # Character callback ; Play a sound when a message is received
    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"

    vbox:
        spacing 0
        # Messenger screen
        frame:
            # ysize 0.85
            if len(items)>=2:
                ysize 1632-(len(items)-2)*(120+10)-20
            else:
                ymaximum 1632
            viewport:
                draggable True
                mousewheel True
                # cols 1
                yinitial 1.0
                # scrollbars "vertical"
                vbox:
                    xalign 0.5
                    null height 20
                    use nvl_phonetext(dialogue,items)
                    null height 100
        # Button to progress
        if len(items)==0: #If we don't have a menu
            button:
                padding (0,0)
                add Solid("#ffda4a")
                add Transform("continue_btn.png", align=(0.5,0.5))
                action RollForward()
        else:
            # Phone Menu Choice
            frame:
                background Solid("#ffda4a")
                foreground None

                vbox:
                    yalign 0.5
                    for i in items: #For each choices...
                        button:
                            action i.action
                            xalign 0.5
                            frame:
                                background Solid("#f1f6fe")
                                foreground None
                                xysize (1000,120)

                                text i.caption:
                                    align (0.5,0.5)
                                    text_align 0.5
                                    size 60
                            # style "nvl_button"


# The actual messenger screen
screen nvl_phonetext(dialogue,items):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # If it's the narrator talking
            null height 30
            text d.what:
                    xalign 0.5
                    ypos 0.0
                    xsize 650
                    text_align 0.5
                    italic True
                    size 40
                    slow_cps False
                    id d.what_id
                    if d.current and len(items)==0:
                        at message_narrator
            null height 30
        else:
            $ is_mc = phone_is_mc(d)
            if is_mc:
                $ message_frame = "phone_send_frame.png"
            else:
                $ message_frame = "phone_received_frame.png"

            hbox:
                spacing 10
                if is_mc:
                    box_reverse True
                    xalign 1.0
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if is_mc:
                        $ message_icon = phone_icons.get(d.who, "phone_send_icon.png")
                    else:
                        $ message_icon = phone_icons.get(d.who, "phone_received_icon.png")

                    add message_icon:
                        if d.current  and len(items)==0:
                            at message_appear_icon()
                        
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if not is_mc and previous_d_who != d.who:
                        text d.who:
                            size 30

                    frame:
                        padding (20,20)
                        

                        background Frame(message_frame, 23,23,23,23)
                        # xsize 750

                        if d.current and len(items)==0:
                            if is_mc:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)
                            # xsize 750
                            slow_cps False
                            size 45
                            

                            if is_mc:
                                color "#FFF"
                                text_align 1.0
                                xanchor 1.0
                                xpos 1.0
                            else:
                                color "#000"

                                
                            id d.what_id
        $ previous_d_who = d.who
                    
style phoneFrame is default
style phone_mc is nvl_label ##Give a character who_style="phone_mc" to put them on the main character side

style phoneFrame_frame:
    background "phone_background.png"
    foreground "phone_foreground.png"
    
    yfill True
    xfill True
    # ysize 815
    # xsize 495

    padding (20,0)


style phoneFrame_viewport:
    yfill True
    xfill True

    # yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True

transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

