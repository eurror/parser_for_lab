# Parser

This parser allows you to parse places for housing from the [kijiji website](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273)  and upload all of the parsed data into postgreSQL.

Also [Docker image]() is available.

## Installation
1. Clone into your local machine
```bash
git clone git@github.com:eurror/parser_for_lab.git
```
2. Create .env file in main directory and fill next fields
```bash
DB_USER=#your db username
DB_PASSWORD=#password for user
DB_NAME=#name of your database
```
3. After you're done with steps above, start **parser/main.py** file
```bash
python3 manage.py main.py
```
