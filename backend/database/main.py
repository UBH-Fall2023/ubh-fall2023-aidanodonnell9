import csv


def update_teams(team: str):
    old_to_new: dict[str:str] = {
        "BAL": "WAS",
        "CHZ": "WAS",
        "WSB": "WAS",
        "PHW": "GSW",
        "SFW": "GSW",
        "TRI": "ATL",
        "MLH": "ATL",
        "STL": "ATL",
        "FTW": "DET",
        "MNL": "LAL",
        "ROC": "SAC",
        "CIN": "SAC",
        "KCK": "SAC",
        "SYR": "PHI",
        "NJA": "BRK",
        "NYN": "BRK",
        "NJN": "BRK",
        "SDR": "HOU",
        "BUF": "LAC",
        "SDC": "LAC",
        "NOJ": "UTA",
        "VAN": "MEM",
        "CHH": "NOP",
        "CHA": "CHO",
        "NOH": "NOP",
        "NOK": "NOP",
        "SEA": "OKC",
    }
    updated_team = old_to_new.get(team)
    if updated_team is not None:
        return updated_team
    return team


def backend_parse_NBAPlayers():
    NBAPlayer_Dict: dict[(str, str, int), (list[str], list[str])] = {}
    same_key_found = False
    with open("backend/database/Player Per Game.csv", "r") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            if lines[8] == "NBA":
                player_team = update_teams(lines[9])
                player_seasons_teams = [[lines[1]], [player_team]]
                player_key = (lines[3], int(lines[2]))
                current_keys = NBAPlayer_Dict.keys()
                for key in current_keys:
                    if key[1] == player_key[1]:
                        same_key_found = True
                        player_listOfteams = NBAPlayer_Dict.get(key)
                        if player_team not in player_listOfteams[0][1]:
                            player_listOfteams[0][1].append(player_team)
                        player_listOfteams[0][0].append(lines[1])
                        NBAPlayer_Dict[key] = player_listOfteams
                        continue
                if same_key_found is not True:
                    NBAPlayer_Dict[player_key] = [player_seasons_teams]
                same_key_found = False

    print(NBAPlayer_Dict.get(("Dell Curry", 2299)))
    with open("data.txt", "w") as t_file:
        t_file.write(str(NBAPlayer_Dict))


def team_parse_NBAPlayers():
    adict = {}
    same_key_found = False
    with open("backend/database/Team Abbrev.csv", "r") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            if lines[1] == "NBA":
                adict[lines[2]] = lines[4]
    return adict


def team_names():
    teamDict: dict[str, str] = {}
    with open("backend/database/Team Abbrev.csv") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            if lines[0] == "2024":
                team_name = lines[2]
                team_abrv = lines[4]
                teamDict[team_name] = team_abrv
    with open("data.txt", "w") as t_file:
        t_file.write(str(teamDict))


# def frontend_parse_NBAPlayers[]:
#     NBAPlayer_Dict: dict[[str, int], list[str]] = {}
#     with open["Player Career Info.csv"] as file:
#         csvFile = csv.reader[file]
#         next[csvFile]
#         for lines in csvFile:
#             player_name = lines[1]
#             player_id = int[lines[0]]
#             player_seasons_played = f"{lines[5]} - {lines[6]}"
#             player_key = [player_name, player_id]
#             NBAPlayer_Dict[player_key] = [player_seasons_played]
#         print[NBAPlayer_Dict]


backend_parse_NBAPlayers()
# print(team_parse_NBAPlayers())
# team_names()
