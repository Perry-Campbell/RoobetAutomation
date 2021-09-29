
import pyautogui
import keyboard

# make sure its set on easy and bet amount is $0.01


def init_game(doubled):
    # set to easy
    pyautogui.moveTo(825, 680, 2)
    pyautogui.moveRel(0, -45, 1)
    if not doubled:
        # set bet amount

        pyautogui.tripleClick()

    pyautogui.typewrite("0.01")

    # start new game
    pyautogui.moveRel(50, -60, 1)
    pyautogui.click()


def play_round():
    pyautogui.moveRel(-20, -70, 1)
    pyautogui.click()


def check_first_round():
    star_color = (244, 224, 89)
    pyautogui.moveTo(840, 510, 0.2)
    try:
        pix = pyautogui.pixel(840, 505)
    except:
        pix = pyautogui.pixel(840, 505)
    print(pix)
    return pix == star_color


def second_round():
    pyautogui.moveTo(840, 470, 1)
    pyautogui.click()


def check_second_round():
    pyautogui.sleep(.5)
    star_color = (244, 224, 89)
    try:
        pix = pyautogui.pixel(840, 470)
    except:
        pix = pyautogui.pixel(840, 470)
    print(pix)
    return pix == star_color

def double_money():
    pyautogui.click(1045, 635)

def cashout():
    pyautogui.moveTo(840, 575, 0.5)
    pyautogui.click()

def quit_check():
    try:
        if keyboard.is_pressed("q"):
            print("Exiting")
            return True
    except:
        pass

def run():
    doubled = False
    while True:
        if quit_check():
            exit(0)
        init_game(doubled)
        play_round()
        if not check_first_round():
            double_money()
            doubled = True
            continue
        if quit_check():
            exit(0)
        second_round()
        if not check_second_round():
            double_money()
            doubled = True
            continue
        if quit_check():
            exit(0)
        cashout()
        doubled = False


if __name__ == '__main__':
    run()