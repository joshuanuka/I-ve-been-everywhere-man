tests=int(input())                       #The number of trips
travels=[]
for k in range (tests):                  
    number=int(input())                  #The number of cities
    lines=[]
    for i in range(number):
        lines.append(input()+'\n')       #appends the city names to the empty list
        
    newlist=[]                           #makes a new list
    for places in lines:
        if places not in newlist:        #to ensure city names are not repeated
            newlist.append(places)
    travels.append(str(len(newlist)))    #counts the cities
print('\n'.join(travels))                #outputs number of cities for each travel
