# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Harish S
        # Role: Architect
        # Code ownership rights: Harish S
    # Version:
        # Version: V 1.0 (July 1)
            # Developer: Harish S
     
    # Description: This code enables CRUD operations in REDIS to store csv data
    
# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Python 3.10.13 -> pip install 
        #redis 5.0.7 -> pip install redis
        #Pandas 2.2.1 -> pip install Pandas==2.2.1

# Import Libraries

import pandas as pd #data manipulation library
import redis #data store / in memory database which store data in RAM
import json  #to transform our data in json format
import msgpack #to save data from 

# Read data

path=input("enter the path of csv file: ") # path of csv file

df= pd.read_csv(path+"Cars_data.csv") # Read csv file

# Initiate connection to Redis

c=redis.Redis(host='localhost',port='6379',db=0)

# Save csv data in Redis

key='csvfiles' #provide name of the key of your choice

csv2json=df.to_json(orient='records') #convert csv to json

c.set(key,csv2json) #save json data in redis

# Read data from redis component 

redisdata=c.get(key) #  get data from redis 

# Convert Redis data into dataframe

df=pd.read_json(redisdata.decode('utf-8'))

print(df.head())