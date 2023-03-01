# Parser

This parser will allow you to parse places for housing from the [kijiji website](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273)  and load all of the data into postgreSQL.

Also [Docker image]() is available.

## Installation
1. Clone into your local machine
```bash
git clone git@github.com:eurror/parser_for_lab.git
```
2. Change database settings in **parser/db.py**
```python
engine = create_engine("postgresql://<db_user>:<db_password>@localhost:5432/<db_name>", echo=False)
```
3. After you're done with steps above, start **parser/main.py** file
```bash
python3 manage.py main.py
```
