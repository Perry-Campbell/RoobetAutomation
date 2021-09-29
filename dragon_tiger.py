import pyautogui
import keyboard
from time import sleep


def run():
    tiger = (222, 222, 0)
    dragon = (255, 32, 0)
    tie = (0, 190, 130)

    first_result = (1207, 720)
    last_result = (1475, 800)
    round = 0
    decks = 0
    end_deck = False
    #pyautogui.moveTo(first_result)

    while not end_deck:
        for i in range(0, 18):

            x = first_result[0] + (i * 16)

            for j in range(0, 6):
                y = first_result[1] + (j * 16)
                #pyautogui.moveTo(x, y)
                res = pyautogui.pixel(x, y)
                print(f"Round: {round}")
                round += 1
                while not was_played(res):
                    if inactive():
                        res = pyautogui.pixel(x, y)
                        continue
                    if not was_played(first_result):
                        end_deck = True
                        sleep(60)
                        break
                    print("Stuck")
                    res = pyautogui.pixel(x, y)
                    sleep(10)
                write_to_file(round, res_string(res))
        end_deck = True
            #pyautogui.moveTo(x, first_result[1])



def inactive():
    unhighlighted = (255, 171, 0)
    highlighted = (255, 197, 77)
    button = pyautogui.pixel(970, 580)
    if button == highlighted or button == unhighlighted:
        pyautogui.moveTo(970, 580)
        pyautogui.click()
        return True
    return False

def write_to_file(round_num, res):
    with open("bacarat_data.txt", 'a') as file:
        file.write(f"{round_num} {res}\n")


def res_string(res):
    tiger = (222, 222, 0)
    dragon = (255, 32, 0)
    tie = (0, 190, 130)
    if res == tiger:
        return "tiger"
    elif res == dragon:
        return "dragon"
    elif res == tie:
        return "tie"


def was_played(res):
    tiger = (222, 222, 0)
    dragon = (255, 32, 0)
    tie = (0, 190, 130)
    return res == tiger or res == dragon or res == tie


if __name__ == "__main__":
    # print(pyautogui.pixel(1207, 720))
    run()
