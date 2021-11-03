# The script of the game goes in this file.

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# The game starts here.
label main_menu:
    return

label start:
    window hide

    nvl_narrator "Nighten added Eileen to the group"
    n_nvl "Hey! Welcome to the demo Eileen!"
    e_nvl "who's this?"
    n_nvl "haha, silly you"
    n_nvl "We talked about showing off the phone the other day, remember?"
    e_nvl "it's today? {image=emoji/fear.png}"
    e_nvl "oops sorry night', I forgot {image=emoji/sweat.png}"
    n_nvl "No problem, you must be quite busy!"
    n_nvl "congrat on showing the emoji tho {image=emoji/clap.png}"
    e_nvl "Nothing magical, it's just a {a=https://www.renpy.org/doc/html/text.html#text-tag-image}image tag{/a} :)"
    n_nvl "But since we use regular renpy, we can use the same principle to send pictures!"
    e_nvl "Right! Let me take a selfie {image=emoji/camera.png}"
    e_nvl "{image=EileenSelfieSmall.png}"
    n_nvl "awww, you look fantastic!"
    e_nvl "And now I have a huge screen to shine!"

    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "Choice 1"
            pass
        "Test choice 2":
            nvl_narrator "Choice 2"
            pass
        "Test choice 3":
            nvl_narrator "Choice 3"
            pass
        "Test choice 4":
            nvl_narrator "Choice 4"
            pass
    
    n_nvl "Thank you Eileen for doing this demo with me!"
    e_nvl "no problem, I hope people will make good use of it!"
    e_nvl "byyee {image=emoji/wave.png}"

    return
