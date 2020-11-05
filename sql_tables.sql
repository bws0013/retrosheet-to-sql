
-- id, version and all of the info fields, will need to find all the fields
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

-- All of the starts
CREATE TABLE IF NOT EXISTS start (
  gameid VARCHAR(12) NOT NULL,
  player_code VARCHAR(10) NOT NULL,
  player_name TEXT NOT NULL,
  home_field_indicator INT(1) NOT NULL,
  batting_order INT(2) NOT NULL,
  field_position INT(2) NOT NULL,
  PRIMARY KEY (gameid, player_code)
);

-- All of the subs in the game
CREATE TABLE IF NOT EXISTS subs (
  event_count INT(3) NOT NULL,
  gameid VARCHAR(12) NOT NULL,
  player_code VARCHAR(10) NOT NULL,
  player_name TEXT NOT NULL,
  home_field_indicator INT(1) NOT NULL,
  batting_order INT(2) NOT NULL,
  field_position INT(2) NOT NULL,
  PRIMARY KEY (gameid, event_count)
);

-- All of the data fields
CREATE TABLE IF NOT EXISTS data (
  gameid VARCHAR(12) NOT NULL,
  type TEXT NOT NULL,
  player_code VARCHAR(10) NOT NULL,
  earned_runs INT(3) NOT NULL,
  PRIMARY KEY (gameid, player_code)
);

-- All of the play fields
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
