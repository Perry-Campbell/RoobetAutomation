import pyautogui
import keyboard
from time import sleep


def initialize_game():
    # scrolls to top of screen
    pyautogui.scroll(1080)


def run():
    result = pyautogui.pixel(950, 500)
    list_results = ""
    red = (230, 68, 45)
    black = (41, 41, 41)
    green = (0, 176, 112)

    while True:

        # Making sure array has last 2 rounds
        print(result)
        if len(list_results) >= 2:

            print(list_results[-2:])
        if result == red:
            list_results += "r"
            if len(list_results) < 2:
                sleep(13)
                continue
            sleep(5)
        elif result == black:
            list_results += "b"
            if len(list_results) < 2:
                sleep(13)
                continue
            sleep(5)
        elif result == green:
            list_results += list_results[-1]
            if len(list_results) < 2:
                sleep(13)
                continue
            sleep(5)


        if is_betting_period():
            bet(list_results)
            result = pyautogui.pixel(950, 500)
            sleep(13)
        else:
            # pyautogui.moveTo(950, 500)
            result = pyautogui.pixel(950, 500)
            sleep(.5)


def bet(list_results):
    print(list_results)
    bet_red = (920, 825)
    bet_black = (980, 825)

    # counting number of consecutive losses backwards
    losses = 2
    try:
        while list_results[-losses] == list_results[-1]:
            losses += 1
    except(IndexError):
        pass

    money =  losses-3
    if list_results[-2:] == "bb":
        print(f"{money} on red")
        pyautogui.moveTo(bet_red)
        pyautogui.click()
        for i in range(money):
            pyautogui.moveTo(1465, 750)
            pyautogui.click()
            sleep(.1)
    elif list_results[-2:] == "rr":
        print(f"{money} on black")
        pyautogui.moveTo(bet_black)
        pyautogui.click()
        for i in range(money):
            pyautogui.moveTo(1465, 750)
            pyautogui.click()
            sleep(.1)




def is_betting_period():
    # Green 0 button location ->   pyautogui.moveTo(735, 650)
    green = (0, 177, 114)
    prog_bar = pyautogui.pixel(735, 650)
    return prog_bar == green


if __name__ == "__main__":
    run()
