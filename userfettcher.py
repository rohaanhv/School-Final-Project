from time import sleep
import requests

# this is our terminal output, all data will be written to a file but some data is displayed on the terminal
user = input('who we spying on: ')
r = requests.get('https://ch.tetr.io/api//users/' + str(user))


# delay in printing the data to terminal so that it looks neater and less jumpy
# each time we print the data we will wait for 0.1 seconds before printing and 0.7*0.1 seconds before printing the next data
# this isnt neccessary but it makes the output better and i like it even if it makes my code look bad. im keeping it cry about it
delay1 = 0.1
delay2 = 0.7*delay1

# this spamms a bunch of carfully selected data from the api to the terminal
r = r.json()
try:
    sleep(delay1)
    print('user id :', end = ' ')
    sleep(delay2)
    print(str(r['data']['user']['_id']))

except:
    print('user no found')
    exit()
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('acct created on :', end=" ")
sleep(delay2)
print(r['data']['user']['ts'])
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('games played :', end = ' ')
sleep(delay2)
print(str(r['data']['user']['gamesplayed']))
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('games won :', end = ' ')
sleep(delay2)
print(str(r['data']['user']['gameswon']))
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('win rate :', end = ' ')
sleep(delay2)
persn = (int(r['data']['user']['gameswon']) / int(r['data']['user']['gamesplayed'])) * 100
print(round(persn, 2), end = '%\n')
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('play time :', end = ' ')
sleep(delay2)
print(round(int(r['data']['user']['gametime'])/3600, 2))
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('country :', end = ' ')
sleep(delay2)
print(str(r['data']['user']['country']))
# //////////////////////////////////////////////////////////////////////////////
sleep(delay1)
print('amount of friends :', end = ' ')
print(str(r['data']['user']['friend_count']))
sleep(delay2)
# //////////////////////////////////////////////////////////////////////////////
# league data
sleep(delay1)
print('league :')
sleep(delay2)
print(str("    games played : " + str(r['data']['user']['league']['gamesplayed'])))
print(str("    games won : " + str(r['data']['user']['league']['gameswon'])))
persn = (int(r['data']['user']['league']['gamesplayed']) / int(r['data']['user']['league']['gameswon'])) * 100
print('    win loss ratio : ' + str(round(persn, 2)), end = '%\n')
print(str("    rating : " + str(r['data']['user']['league']['rating'])))
print(str("    rank : " + str(r['data']['user']['league']['rank'])))
# end of spam

# now we will write all of our data to a file so that we can use it later if we need
with open(str(user) + ".json", "w") as file:
    file.write(str(r))

# pause program so that we can read the data 
while True:
    pass

# someone notes:
# not everything in this file is neccessary, but i made it anyway because i like it and i want to make this as usefull as possible
# i also made it so that the program will not crash if the user is not found, but instead it will just print the error message
# some people might be criticle of all the spamming of code, but there is no other way to do it, and i added breaks to make it look better
# if you use the same user imput twice the file will be over written with the new data. this is to keep it up to date if you wanted to get an update on the data