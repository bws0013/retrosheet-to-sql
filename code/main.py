import json
import db
import file_getter
import parse
from configparser import ConfigParser

config_file_name = 'config.ini'

file_storage_path = './../storage/'
output_file_name = 'output.json'

def json_to_map(games_file):
    with open(games_file) as f:
        data = json.load(f)
    return data

def add_info_fields(game):
    value_placeholder = ''
    gameid = game['id']
    version_num = game['version']
    info_fields = game["info"]
    key_sql = 'gameid,version_number,'
    val_sql = [gameid, version_num]
    for field in info_fields:
        key = list(field.keys())[0]
        val = list(field.values())[0]
        if(val != ''):
            key_sql += key + ","
            val_sql.append(val)
    for i in range(len(val_sql)):
        value_placeholder += '%s,'
    generate_insert_query(key_sql[:-1], [tuple(val_sql)], value_placeholder[:-1], "info")


# CREATE TABLE IF NOT EXISTS plays (
#   gameid VARCHAR(12) NOT NULL,
#   event_count INT(3) NOT NULL,
#   inning_number INT(2) NOT NULL,
#   home_field_indicator INT(1) NOT NULL,
#   player_code VARCHAR(10) NOT NULL,
#   count_at_action VARCHAR(2) NOT NULL,
#   all_pitches TEXT,
#   play_events TEXT NOT NULL,
#   PRIMARY KEY (gameid, event_count)
# );



def add_play_fields(game):
    value_placeholder = '%s,%s,%s,%s,%s,%s,%s,%s'
    gameid = game['id']
    play_events = game["plays"]
    key_sql = 'gameid,event_count,inning_number,home_field_indicator,player_code,count_at_action,all_pitches,play_events'
    val_sql = []
    for event in play_events:
        ec = event["event_count"]
        iu = event["inning_number"]
        hf = event["home_field_indicator"]
        pc = event["player_code"]
        ca = event["count_at_action"]
        ap = event["all_pitches"]
        pe = event["play_events"]
        val_sql.append((gameid, ec, iu, hf, pc, ca, ap, pe))
    generate_insert_query(key_sql, val_sql, value_placeholder, "plays")

def add_data_fields(game):
    value_placeholder = '%s,%s,%s,%s'
    gameid = game['id']
    data_events = game["data"]
    key_sql = 'gameid,type,player_code,earned_runs'
    val_sql = []
    for event in data_events:
        ty = event["type"]
        pc = event["player_code"]
        er = event["earned_runs"]
        val_sql.append((gameid, ty, pc, er))
    generate_insert_query(key_sql, val_sql, value_placeholder, "data")

def add_sub_fields(game):
    value_placeholder = '%s,%s,%s,%s,%s,%s,%s'
    gameid = game['id']
    sub_events = game["subs"]
    key_sql = 'gameid,event_count,player_code,player_name,home_field_indicator,batting_order,field_position'
    val_sql = []
    for event in sub_events:
        ec = event["event_count"]
        pc = event["player_code"]
        na = event["name"]
        hf = event["home_field_indicator"]
        bo = event["batting_order"]
        fp = event["field_position"]
        val_sql.append((gameid, ec, pc, na, hf, bo, fp))
    generate_insert_query(key_sql, val_sql, value_placeholder, "subs")

def add_start_fields(game):
    value_placeholder = '%s,%s,%s,%s,%s,%s'
    gameid = game['id']
    start_events = game["start"]
    key_sql = 'gameid,player_code,player_name,home_field_indicator,batting_order,field_position'
    val_sql = []
    for event in start_events:
        se = event["player_code"]
        na = event["name"]
        hf = event["home_field_indicator"]
        bo = event["batting_order"]
        fp = event["field_position"]
        val_sql.append((gameid, se, na, hf, bo, fp))
    generate_insert_query(key_sql, val_sql, value_placeholder, "start")

# https://www.w3schools.com/python/python_mysql_insert.asp
def generate_insert_query(key_sql, val_sql, value_placeholder, db_name):
    insert_query = "INSERT INTO {0} ({1}) VALUES ({2})".format(db_name, key_sql, value_placeholder)
    vals = val_sql
    # print(insert_query)
    # print(vals)
    db.insert_into_table(insert_query, vals)

def add_games_to_db(games_file):
    all_games = json_to_map(games_file)
    for game in all_games:
        # print(game)
        add_info_fields(game)
        add_start_fields(game)
        add_sub_fields(game)
        add_data_fields(game)
        add_play_fields(game)
    print("> Game Added To DB")


def set_global_vars():
    config_reader = ConfigParser()
    config_reader.read(config_file_name)
    global file_storage_path
    global output_file_name
    file_storage_path = config_reader.get('storage', 'storage_path')
    output_file_name = config_reader.get('output', 'temporary_output_file')

def get_parse_and_add_to_db(year):
    set_global_vars()
    db.create_all_tables()
    current_game_ids = db.get_gameid_values_set()

    output_file = file_storage_path + output_file_name

    ### Get data files
    filepaths = file_getter.download_open_and_get_files(year)

        ### Parse the games to json
    for file in filepaths:
        print("> File:", file)
        parse.output_game_data(file)
        games_to_add = parse.get_all_game_ids_set(file)
        if games_to_add.issubset(current_game_ids):
            print("Games already in db")
            continue

        ### Convert games to sql
        add_games_to_db(output_file)


year = '2015'
get_parse_and_add_to_db(year)

# game = json_to_map("output.json")
# add_info_fields(game)
# year = 2019
# download_open_and_get_files
# convert_games_to_sql("output.json")
