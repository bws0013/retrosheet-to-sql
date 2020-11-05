import wget
import pathlib
import zipfile
from configparser import ConfigParser
import ssl

# Regular season event files only, at the moment

config_file_name = 'config.ini'

file_storage_path = './../storage/'
file_event_type = 'eve'

def extract_files_from_zip(filename):
    sub_dir_name = filename.split('.')[0]
    input_path = file_storage_path + '/zip_files/' + filename
    output_path = file_storage_path + '/data_files/' + sub_dir_name
    with zipfile.ZipFile(input_path, "r") as zip_loc:
        zip_loc.extractall(output_path)

def download_file(year):
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://www.retrosheet.org/events/%s%s.zip" % (year, file_event_type)
    filename = url.split('/')[-1]
    if does_file_exist(filename) == True:
        print("> File already exists:", filename)
        return
    wget.download(url, file_storage_path + '/zip_files/')
    print("\n> Download Complete")

def does_file_exist(filename):
    relative_path = file_storage_path + '/zip_files/' + filename
    if pathlib.Path(relative_path).exists():
        return True
    return False

def set_global_vars():
    config_reader = ConfigParser()
    config_reader.read(config_file_name)
    global file_storage_path
    global file_event_type
    file_storage_path = config_reader.get('storage', 'storage_path')
    file_event_type = config_reader.get('storage', 'event_type')

def get_all_file_paths(year):
    filenames = []
    data_dir = file_storage_path + '/data_files/' + year + file_event_type + '/'
    data_files = pathlib.Path(data_dir)
    for f in data_files.iterdir():
        if f.is_file() and '.EV' in f.name:
            filenames.append(data_dir + f.name)
    # print(filenames)
    return filenames

def download_open_and_get_files(year):
    set_global_vars()
    filename = year + file_event_type + '.zip'

    download_file(year)
    extract_files_from_zip(filename)
    return get_all_file_paths(year)

# set_global_vars()

# year = '2016'
# download_open_and_get_files(year)

# print("> Done")
