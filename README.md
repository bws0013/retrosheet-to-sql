### Last Big Edit Date
11/04/20

### Description

Read in retrosheet data and add it to a database for easier access.

### Roadmap

Current goals include
* Skipping converting data to json before adding it to db.
* Improving how games are determined to have already been read in through the database
* Clean up code base to remove unneeded files.
* Automate more of the run instructions

### My Run Environment
```
$ python --version
Python 3.8.6
```

```
$ pip --version
pip 20.2.3 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
```

```
$ mysql --version
mysql  Ver 8.0.21 for osx10.13 on x86_64 (Homebrew)
```

```
$ bash --version
GNU bash, version 3.2.57(1)-release (x86_64-apple-darwin17)
Copyright (C) 2007 Free Software Foundation, Inc.
```

### Run Instructions
* When running on a linux box I needed used root the entire time
* Make sure you have a similar Run Environment to what I have above
  * Python3, Pip3, Mysql, Bash
  * Note that when installing and setting up mysql you should [set](https://phoenixnap.com/kb/access-denied-for-user-root-localhost) the root password as `password` unless you want to change it in `db.py`
* Download dependencies per requirements.txt.
  * `pip install -r requirements.txt`
* Create a mysql database called baseballdata
  * `CREATE DATABASE baseballdata;`
* Run the `setup.sh` script to create the required directories
  * `bash setup.sh`
  * Optionally these can be created manually
* Change directories in the code directory `cd code`
* Change the year in `main.py` or keep it where it is (2016)
* Run `main.py`
  * `python main.py`
* Access the database and use this data
  * Login to the mysql database `sudo mysql -uroot -p`
  * Select the `baseballdata` database with `use baseballdata;`
* Make queries against the data in mysql

### Run Notes
The only files that can be read right now are the "Regular Season Event Files" which represent a large (though not complete) set of the retrosheet data. This limitation is due to how data files are downloaded from the retrosheet site and is a limitation I am looking to solve for.

The check for if one or more games has been read in currently works by taking all game ids from the database before any others are added. If the new game ids being read in are a subset of the existing game ids the file is not read in. This has some problems in the event a file was only partially read in and is something I will look to improve.

### Notes on files
The `sql_tables.sql` file contains the tables that are present in the database.

The `structure.json` file contains an example of what the json object looks like before its added to the database.

The `parse_guide.md` file is an explanation of data in each field. This was a modified guide from the better ones found on retrosheets.

As far as code goes the `code/main.py` file is the primary file to run. It will take a take in a year, download the zip file for the games of that year, extract the files, convert them into json objects, then send the json data to mysql.

There is a config file `code/config.ini` that I plan to utilize more later on. I would not recommend changing its values unless you know what you are doing.

### Required Notice Related To Data Usage

The information used here was obtained free of charge from and is copyrighted by Retrosheet. Interested parties may contact Retrosheet at "www.retrosheet.org".

Requirement found [here](https://www.retrosheet.org/notice.txt#:~:text=Recipients%20of%20Retrosheet%20data%20are,product%20based%20upon%20the%20data).
