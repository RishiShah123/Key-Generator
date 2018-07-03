import random # importing random function
from collections import Counter  # will be used when verifying to make sure a letter is reapted





class key(): # creating key gen class
    alpha = 'qwertyuiopasdfghjklzxcvbnm1234567890'  # charecters used in the key gen
    sum = 0  # sum of all the digets in the ord func

    def __init__(self, diget_key = ''):  # init class and blank key varibile
        self.diget_key = diget_key  # defineing self
    def create(self): # Creating of key
        self.diget_key = ''  # reseting self.key to make sure it is blank
        self.sum = 0 # setting the sum as 0 incase a previus key was made and it was wrong so I am reseting
        while len(self.diget_key) < 19:  # keep making the key until it is more that 18; example of the key is '1234 - 5678- 9 10 11 12-13 14 15 16' 16 + 3 = 19
            chunk = ''  # setting a varible for the small 4 diget parts of key
            while len(chunk) < 5 : # making sure the len of the chunk is not more than 4

                x  = random.choice(key.alpha) # picking a random charecter and setting it to a varible
                self.sum += int(ord(x)) # adding the ord of it to the sum varible
                chunk += x # addint the random letter to the chunk
            else: # after it equals 4
                self.diget_key += chunk +  '-' # add a hash to split it
        else: # after the whole key
            self.diget_key = self.diget_key[:-1] # remove the last letter which  is a dash

    def verify(self): # verifying if the key meets our reqiurments
        x =  Counter(self.diget_key) # setting x to a dict of the amount of times each letter apprets
        target = self.diget_key[0] # setting the key which has to be repeated
        count = x[target] # setting a varible of the amount of times the first  char appears

        if count == 3 and self.sum == 1900: # if the first diget is repeated 3 times and the sum is 1900
            
            return True # return true and break loop
        else: # if not
            self.diget_key += 'the count is ' + str(count) +  'the sum is' + str(self.sum) # print the key with the count and sum so you can follow the bad keys
            return False # return false and break loop

    def __str__(self): # incase to print the final key and it is a magic function
         y = str(self.sum )
         return f"your key is {self.diget_key}"  #  when you try to print the class it return the final key


gen = key() # defining the class to run it
active = True # setting an active varible to make sure it runs
gen.create() # calling the create func
while active: # setting a loop incase the key is incorect
    if gen.verify() == True: # if the key gen return the key is valid
        print(gen) # print the key
        break # break the loop
    else: # if the key is inncort
        print(gen) # print the previtus key wiht the sum and ord
        gen.create() # make a new key
