import pyautogui
import keyboard
from time import sleep


class Session:
    def __init__(self):
        self.total_rounds = 0
        self.total_wins = 0
        self.total_golds = 0
        self.max_loss = 0

    def add_round(self):
        self.total_rounds += 1

    def add_win(self):
        self.total_wins += 1

    def add_golds(self):
        self.total_golds += 1

    def check_loss(self, loss):
        if loss > self.max_loss:
            self.max_loss = loss

    def print(self):
        print(f"Round: {self.total_rounds} Wins: {self.total_wins} Golds: {self.total_golds} Losses: {self.max_loss}0.01")


def init_game(bet_amount, losses):
    pyautogui.moveTo(475, 250)

    pyautogui.scroll(1080)
    pyautogui.tripleClick()
    pyautogui.typewrite(str(bet_amount))

    for i in range(0, losses):
        pyautogui.moveTo(635, 250)
        pyautogui.click()
        sleep(0.1)

    pyautogui.moveTo(550, 300)
    pyautogui.click()


def check_result(session):
    session.add_round()
    bronze_coin = (203, 105, 48)
    silver_coin = (138, 138, 137)
    gold_coin = (185, 149, 7)
    result_coin = pyautogui.pixel(1100, 500)

    if result_coin == gold_coin:
        session.add_golds()
    elif result_coin == silver_coin:
        session.add_win()
    return result_coin == silver_coin


def run():
    # Starting parameters
    bet_amount = 0.01
    gold_bar = (216, 180, 53)
    background = (29, 28, 49)
    initialized = False
    session = Session()
    losses = 0

    while True:
        timer_start = pyautogui.pixel(925, 365)
        timer_end = pyautogui.pixel(750, 365)
        if timer_end == gold_bar and not initialized:
            init_game(bet_amount, losses)
            initialized = True
        if timer_end == background and initialized:
            sleep(13)
            res = check_result(session)
            if not res:
                losses += 1
                session.check_loss(losses)

            else:
                session.check_loss(losses)

                losses = 0
            initialized = False
            session.print()
        sleep(1)

def mine_data():
    background = (29, 28, 49)
    bronze_coin = (203, 105, 48)
    silver_coin = (138, 138, 137)
    gold_coin = (185, 149, 7)
    result_coin = pyautogui.pixel(1100, 500)
    bronze_wins = 0
    silver_wins = 0
    gold_wins = 0

    while True:

        timer_end = pyautogui.pixel(750, 365)

        if timer_end == background:
            sleep(13)

            if result_coin == gold_coin:
                gold_wins += 1
            elif result_coin == silver_coin:
                silver_wins  += 1
            else:
                bronze_wins += 1

            print(f"Round: {gold_wins + silver_wins + bronze_wins}"
                  f"Gold: {gold_wins} Silver: {silver_wins} Bronze: {bronze_wins}"
                  f"")

        else:
            sleep(1)



if __name__ == '__main__':
    # init_game()
    # check_result()
    run()
