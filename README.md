# Versions
```
$ python3 --version
Python 3.7.3

$ pip3 --version
pip 19.0.3
```

# Installation
To install Mox's dependencies perform the following:
```shell
pip3 install -r requirements.txt
pip3 install -e .
```

# Databases
The application is using PostgreSQL. Perform the following commands to create the local databases.
```shell
createdb mox_dev
createdb mox_test
```

To perform the migrations execute the following script:
```shell
./scripts/migrate_latest.py
```

This script will default to the `development` environment. You can specify the environment with an argument:
```shell
./scripts/migrate_latest.py test
./scripts/migrate_latest.py prod
```
