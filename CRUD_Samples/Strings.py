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

c.rpush('languages', 'python', 'java', 'go') # languages is the key, python,java and go are values

# Read operation

prog_lang = c.lrange('languages', 0, -1) # reads the values from key 
Languages = [lang.decode('utf-8') for lang in prog_lang] # save the values as list 
print('original list:', Languages) 

# Update operation

c.lset('languages', 1, 'javascript')

# Read whether the updation is completed and java is replaced with javascript

prog_lang = c.lrange('languages', 0, -1) # reads the values from key 
Languages = [lang.decode('utf-8') for lang in prog_lang] # save the values as list 
print('updated list: ',Languages) 

# delete a single element in the list

c.lrem('languages',1,'javascript')

# Read whether the deletion is completed and  javascript is deleted

prog_lang = c.lrange('languages', 0, -1) # reads the values from key 
Languages = [lang.decode('utf-8') for lang in prog_lang] # save the values as list 
print('deleted list: ',Languages) 

# delete entire list

c.delete('languages')

# Check if the list still exists
exists = c.exists('languages')
print(exists)  # Output: 0 (means the list does not exist) 










