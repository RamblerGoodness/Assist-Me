# main.py
import threading
import twitch_bot
import pygame_display

def run_twitch_bot():
    bot = twitch_bot.Bot()
    bot.run()

def run_pygame_display():
    pygame_display.main()

if __name__ == "__main__":
    t1 = threading.Thread(target=run_twitch_bot)
    t2 = threading.Thread(target=run_pygame_display)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
