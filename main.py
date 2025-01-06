import keyboard


def on_enter_press():
    keyboard.write(" 🗿🍷", exact=True)
    keyboard.press_and_release("enter")


keyboard.add_hotkey('enter', on_enter_press, suppress=True)

keyboard.wait("num 5")