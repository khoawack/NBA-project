import requests
import os
import time

def refresh_data():
    response = requests.get('https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com/NBA/liveData/scoreboard/todaysScoreboard_00.json')
    nba = response.json()
    return nba

while True:

    nba = refresh_data()

    clear = lambda: os.system('clear')
    clear()
    print("Date:", nba['scoreboard']['gameDate'], nba["meta"]["time"])
    print("---------------------------------")
    num_games = range(len(nba['scoreboard']['games']))

    response = requests.get(
        'https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com/NBA/liveData/scoreboard/todaysScoreboard_00.json')
    nba = response.json()

    for i in num_games:
        if (nba['scoreboard']['games'][i]["gameStatusText"] == "Final"):  # if finished print finished
            print("FINISHED")
        else:
            print(nba['scoreboard']['games'][i]["gameStatusText"])  # print quarter and time left

        print("HOME:  ", nba['scoreboard']['games'][i]['homeTeam']["teamName"], "   ",
              nba['scoreboard']['games'][i]['homeTeam']["wins"], ":",
              nba['scoreboard']['games'][i]['homeTeam']["losses"])
        print(nba['scoreboard']['games'][i]['homeTeam']["score"])

        print("AWAY:  ", nba['scoreboard']['games'][i]['awayTeam']["teamName"], "   ",
              nba['scoreboard']['games'][i]['awayTeam']["wins"], ":",
              nba['scoreboard']['games'][i]['awayTeam']["losses"])
        print(nba['scoreboard']['games'][i]['awayTeam']["score"])

        print("---------------------------------")

    time.sleep(5)





