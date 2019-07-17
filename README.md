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
