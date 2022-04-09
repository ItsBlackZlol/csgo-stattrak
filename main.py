import requests


def stattrak(steamlink):
    if steamlink.lower().startswith("https://steamcommunity.com/profiles/"):
        steamid = steamlink.split('/', 4)[4]

    url = f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=12A1D1DE83F9932934EDD6DF2BA00463&steamid={steamid}"
    try:
        r = requests.get(url)
        data = r.json()

        tkills = data["playerstats"]["stats"][0]["value"]
        tdeath = data["playerstats"]["stats"][1]["value"]

        twon = data["playerstats"]["stats"][127]["value"]

        stats = f"\n========================================\nyou won {twon} matches.\nyou killed {tkills} people.\nyou died {tdeath} times.\nyour K/D is {round(int(tkills) / int(tdeath), 2)}\n========================================"

        print(stats)
    except:
        print("\nThe entered steamlink is invalid.")


sl = input("Please enter your steam link >>> ")
stattrak(sl)