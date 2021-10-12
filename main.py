'''Author: Jay Desale
Date-created: 18th September 2021
The main motive of writing this small algorithm is to just play around adding a layer of gibberish between the user password and the hash
however i would love to see people recommending me changes and upgrades to make this thing actually useful, if possible:D
With all due respect i am unaware if identical algorithms do exist and are older than mine and if they do then please do let me know 
i wont call it my own algorithm.'''

#the libraries i needed
import hashlib
import random
import time

#user gives the password and is stored inside the variable "usrinp"
usrinp = input("enter your password: ")

#password string is converted to a list stored into the variable "inpsplit" and shuffled  
inpsplit = list(usrinp)
random.shuffle(inpsplit)

#creating and shuffling the gibberish stuff(it includes morse and binary and some random signs) 
words0 = ["$", "_", "$"]
random.shuffle(words0)
words1 = ["-.--", "---", "..-", "...", ".._.._", "._w21s!", ".ez21_.", ".,,,,......!", ""]
random.shuffle(words1)
words2 = ["04", "123", "1fr", "0rf", "0rfeg", "0btb", "1", "1^^", "0w2", "1d232", "1dd2", "000d32f", "01f23g",  "011011g3243ff34", "10",  "0110", "1110",  "011011", "11vergt",  "011105t4fx4", "10004g5h46", "0000v6j76k68", "101656vbhc65", "06h5rh56", "0005h57j5v", "0105h7j60010", "00hegfc3ug342djrj439r001010"]
random.shuffle(words2)


#combining the shuffled user password with the shuffled gibberish and storing in a variable "com"
com = (inpsplit + words0 + words1 + words2)

# shuffling the mixture of shuffled user password and shuffled gibberish
random.shuffle(com)


#converting list back to string :))
joinstr = ''.join(com)                
# print(f"this is your gibberish layer: " + joinstr) #you can uncomment this line to see whats the gibberish layer the algorithm added
print("generating the hash!!")
time.sleep(1)

#hashing using the sha-256
hash_object = hashlib.sha256(b'' + joinstr.encode())
hex_dig = hash_object.hexdigest()
print(f"Note your hashed string :D enjoy!!" + hex_dig)


















