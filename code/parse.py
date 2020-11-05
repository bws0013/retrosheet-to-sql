import csv
import convert_game
from configparser import ConfigParser

config_file_name = 'config.ini'

file_storage_path = './../storage/'
output_file_name = 'output.json'

def read_data_file(filename):
    all_records = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 0
        for row in csv_reader:
            all_records.append(row)
    return all_records

def get_next_game_id_row(all_records, start_row=0):
    id_row = -1
    for i in range(start_row, len(all_records)):
        row = all_records[i]
        if row[0] == 'id':
            id_row = i
            break
    return id_row

def get_game_data(all_records, start_row):
    records = []
    if start_row < 0 or start_row > len(all_records):
        return []
    records.append(all_records[start_row])
    for i in range(start_row + 1, len(all_records)):
        row = all_records[i]
        if row[0] == 'id':
            break
        else:
            records.append(row)
    return records

def get_all_game_ids_set(filename):
    all_records = read_data_file(filename)

    game_ids = []
    for i in all_records:
        if i[0] == 'id':
            game_ids.append(i[1])
    return set(game_ids)

def get_all_game_id_rows(all_records):
    all_start_rows = []
    latest_start_row = -1
    while True:
        latest_start_row += 1
        start_row = get_next_game_id_row(all_records, latest_start_row)
        if start_row == -1:
            break
        all_start_rows.append(start_row)
        latest_start_row = start_row
    return all_start_rows

def get_all_game_data(filename):
    all_game_data = []

    all_records = read_data_file(filename)
    game_id_rows = get_all_game_id_rows(all_records)

    for g in game_id_rows:
        game_data = get_game_data(all_records, g)
        all_game_data.append(game_data)
    return all_game_data

# Helper method for making a sql query
def get_all_info_types(filename):
    info_map = {}
    all_records = read_data_file(filename)
    for r in all_records:
        if r[0] == "info":
            info_map[r[1]] = True
    for key, value in info_map.items() :
        print (key, value)
    print(len(info_map))

def set_global_vars():
    config_reader = ConfigParser()
    config_reader.read(config_file_name)
    global file_storage_path
    global file_event_type
    file_storage_path = config_reader.get('storage', 'storage_path')
    output_file_name = config_reader.get('output', 'temporary_output_file')

def output_game_data(filepath):
    set_global_vars()
    all_games_data = get_all_game_data(filepath)
    all_games_json = convert_game.get_all_games(all_games_data)
    full_output_file_name = file_storage_path + '/' + output_file_name
    print(all_games_json, file=open(full_output_file_name, 'w'))

# path = './../storage//data_files/2016eve/2016WAS.EVN'
# print(get_all_game_ids(path))

# Modify the below to read in a different file
# path = "./../storage/data_files/2016eve/2016ANA.EVA"
# path = "./../storage/ANA201808100.in"
# output_game_data(path)
