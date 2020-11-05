import csv
import json

def read_data_file(filename):
    all_records = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 0
        for row in csv_reader:
            all_records.append(row)
    return all_records

def parse_play_fields(play_fields):
    plays = []
    for p in play_fields:
        temp = {}
        temp["event_count"] = int(p[0])
        temp["inning_number"] = int(p[1])
        temp["home_field_indicator"] = int(p[2])
        temp["player_code"] = p[3]
        temp["count_at_action"] = p[4]
        temp["all_pitches"] = p[5]
        temp["play_events"] = p[6]
        plays.append(temp)
    return plays

def parse_sub_fields(sub_fields):
    subs = []
    for s in sub_fields:
        temp = {}
        temp["event_count"] = int(s[0])
        temp["player_code"] = s[1]
        temp["name"] = s[2]
        temp["home_field_indicator"] = int(s[3])
        temp["batting_order"] = int(s[4])
        temp["field_position"] = int(s[5])
        subs.append(temp)
    return subs

def parse_info_fields(info_fields):
    infos = []
    for i in info_fields:
        temp = {}
        temp[i[0]] = i[1]
        infos.append(temp)
    return infos

def parse_start_fields(start_fields):
    starts = []
    for s in start_fields:
        temp = {}
        temp["player_code"] = s[0]
        temp["name"] = s[1]
        temp["home_field_indicator"] = int(s[2])
        temp["batting_order"] = int(s[3])
        temp["field_position"] = int(s[4])
        starts.append(temp)
    return starts

def parse_data_fields(data_fields):
    datas = []
    for d in data_fields:
        temp = {}
        temp["type"] = d[0]
        temp["player_code"] = d[1]
        temp["earned_runs"] = int(d[2])
        datas.append(temp)
    return datas

def get_fields(records):
    id = ""
    version = ""

    play = []
    info = []
    start = []
    data = []
    sub = []

    event_count = 0
    for r in records:
        if r[0] == "play":
            r[0] = event_count
            event_count += 1
            play.append(r)
        elif r[0] == "info":
            info.append(r[1:])
        elif r[0] == "start":
            start.append(r[1:])
        elif r[0] == "data":
            data.append(r[1:])
        elif r[0] == "sub":
            r[0] = event_count
            event_count += 1
            sub.append(r)
        elif r[0] == "com":
            continue # This one we should ignore
        elif r[0].endswith("adj"):
            continue # This one we should ignore
        elif r[0] == "id":
            id = r[1]
        elif r[0] == "version":
            version = r[1]
        else:
            print("ERROR")
            print(r)
    return id, version, play, info, start, data, sub

def get_game(game_records):
    id, version, plays, infos, starts, datas, subs = get_fields(game_records)
    play_list = parse_play_fields(plays)
    info_list = parse_info_fields(infos)
    start_list = parse_start_fields(starts)
    data_list = parse_data_fields(datas)
    sub_list = parse_sub_fields(subs)

    game = {}
    game["id"] = id
    game["version"] = version
    game["plays"] = play_list
    game["info"] = info_list
    game["start"] = start_list
    game["data"] = data_list
    game["subs"] = sub_list
    return game

def get_all_games(all_game_records):
    all_games = []
    for g in all_game_records:
        all_games.append(get_game(g))
    return json.dumps(all_games)

# path = "./../storage/ANA201808100.in"

# game_records = read_data_file(path)
# game = get_game(game_records)
#
# out = json.loads(game)
# print(out["id"])
