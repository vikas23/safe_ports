# Search

This app will read the post requests from different agents in the data center and parse while dumping the data to database in central server

## Style guide

* https://gist.github.com/sloria/7001839

## Required packages

    pip install -r requirements.txt

#### Usage:

Running script on command line as a background process:

```shell
  nohup python CE_server.py &
```

#### Check if server is running

```
GET Method
```

hostname:port/

# Return: 
'service is running'


#### Entry point:


```
POST Method
```

hostname:port/register_resource


# Input:

Our JS API will recieve json object as shown below:

```json
{
    "hostname":"",
    "interfaces":"",
    "osinfo": "",
    "openports": "",
    "cpuinfo" : ""
}
```

# Code Flow / Algorithm

```python
Read post request
connect to database
Store json object read to the table
Parse the json object
Store the information in database schema
```


# config

config file should containt relevant information mentioned below:
```
ENVIRONMENT : system enviornment
CONN_STRING : database credentials
LOG_FILE_NAME : filename of log
LOG : log location
HOSTNAME : hostname
PORT : port
```
