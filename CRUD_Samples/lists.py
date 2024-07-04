# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Harish S
        # Role: Architect
        # Code ownership rights: Harish S
    # Version:
        # Version: V 1.0 (July 1)
            # Developer: Harish S
     
    # Description: This code enables CRUD operations in REDIS
    
# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Python 3.10.13 -> pip install 
        #redis 5.0.7 -> pip install redis
        #Pandas 2.2.1 -> pip install Pandas==2.2.1

#Import Libraries
import redis # Import the redis library
import pandas # Data manipulation library

#Create redis connection

c=redis.Redis(host='localhost',port=6379, db=0)

#Create operation

# Create a new key-value pair
c.set('language', 'Python') # here language is the key, python is value

# Read operation

rd=c.get('language').decode('utf-8') # read the value by specifying the key

print(rd)

#Update operation

c.set('language','Java') #update the value

upd=c.get('language').decode('utf-8')

print(upd)

#delete operation

c.delete('language') #delete the key value pair
