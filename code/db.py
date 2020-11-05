import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="baseballdata"
)

# This is just for testing purposes
def drop_all_tables():
    sql = "DROP TABLE data"
    mycursor.execute(sql)
    sql = "DROP TABLE info"
    mycursor.execute(sql)
    sql = "DROP TABLE plays"
    mycursor.execute(sql)
    sql = "DROP TABLE start"
    mycursor.execute(sql)
    sql = "DROP TABLE subs"
    mycursor.execute(sql)

def get_gameid_values_set():
    mycursor.execute("select distinct(gameid) from info;")

    all_gameid_tuples = mycursor.fetchall()
    all_gameid_strings = []

    for a in all_gameid_tuples:
        all_gameid_strings.append(a[0])
    return set(all_gameid_strings)

def create_info_table():
    create = '''
    CREATE TABLE IF NOT EXISTS info (
      gameid VARCHAR(12) NOT NULL,
      version_number INT NOT NULL,
      attendance TEXT,
      date TEXT,
      daynight TEXT,
      fieldcond TEXT,
      hometeam TEXT,
      howscored TEXT,
      lp TEXT,
      number TEXT,
      oscorer TEXT,
      pitches TEXT,
      precip TEXT,
      save TEXT,
      site TEXT,
      sky TEXT,
      starttime TEXT,
      temp TEXT,
      timeofgame TEXT,
      ump1b TEXT,
      ump2b TEXT,
      ump3b TEXT,
      umphome TEXT,
      usedh TEXT,
      visteam TEXT,
      winddir TEXT,
      windspeed TEXT,
      wp TEXT,
      PRIMARY KEY (gameid)
    );
    '''
    mycursor.execute(create)

def create_start_table():
    create = '''
    CREATE TABLE IF NOT EXISTS start (
      gameid VARCHAR(12) NOT NULL,
      player_code VARCHAR(10) NOT NULL,
      player_name TEXT NOT NULL,
      home_field_indicator INT(1) NOT NULL,
      batting_order INT(2) NOT NULL,
      field_position INT(2) NOT NULL,
      PRIMARY KEY (gameid, player_code)
    );
    '''
    mycursor.execute(create)

def create_subs_table():
    create = '''
    CREATE TABLE IF NOT EXISTS subs (
      gameid VARCHAR(12) NOT NULL,
      event_count INT(3) NOT NULL,
      player_code VARCHAR(10) NOT NULL,
      player_name TEXT NOT NULL,
      home_field_indicator INT(1) NOT NULL,
      batting_order INT(2) NOT NULL,
      field_position INT(2) NOT NULL,
      PRIMARY KEY (gameid, event_count)
    );
    '''
    mycursor.execute(create)

def create_data_table():
    create = '''
    CREATE TABLE IF NOT EXISTS data (
      gameid VARCHAR(12) NOT NULL,
      type TEXT NOT NULL,
      player_code VARCHAR(10) NOT NULL,
      earned_runs INT(3) NOT NULL,
      PRIMARY KEY (gameid, player_code)
    );
    '''
    mycursor.execute(create)

def create_plays_table():
    create = '''
    CREATE TABLE IF NOT EXISTS plays (
      gameid VARCHAR(12) NOT NULL,
      event_count INT(3) NOT NULL,
      inning_number INT(2) NOT NULL,
      home_field_indicator INT(1) NOT NULL,
      player_code VARCHAR(10) NOT NULL,
      count_at_action VARCHAR(2) NOT NULL,
      all_pitches TEXT,
      play_events TEXT NOT NULL,
      PRIMARY KEY (gameid, event_count)
    );
    '''
    mycursor.execute(create)

def create_all_tables():
    create_info_table()
    create_start_table()
    create_subs_table()
    create_data_table()
    create_plays_table()

def insert_into_table(sql, vals):
    mycursor = mydb.cursor()
    # print(sql)
    # print(vals)
    if isinstance(vals, list):
        mycursor.executemany(sql, vals)
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
    else:
        mycursor.execute(sql, vals)
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()
create_all_tables()


# print(get_gameid_values_set())

# drop_all_tables()

# mycursor.execute("CREATE DATABASE baseballdata")
# create_all_tables()
#
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)
