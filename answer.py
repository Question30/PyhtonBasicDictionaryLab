# Problem 1

# Use the following states and capitals to create dictionary objects.
# Los Angeles, California
# Albany, New York
# Honolulu, Hawaii
# Juneau, Alaska
# Austin, Texas
# Create a Dictionary object with the {} bracket notation where the States are the Keys and the Capitals are the values.
# Create a Dictionary object with built-in dict() function where the States are the Keys and the Capitals are the values.
# Use the type() method to check the object type of each object
# Print each object to see all the key:value pairs in the dictionary

states1 = {
    "California": "Los Angeles",
    "New York": "Albany",
    "Hawaii" : "Honolulu",
    "Alaska" : "Juneau",
    "Texas" : "Austin"
}

states2 = dict([
    ("California", "Los Angeles"),
    ("New York","Albany"),
    ("Hawaii" , "Honolulu"),
    ("Alaska" , "Juneau"),
    ("Texas" , "Austin")
])

print(type(states1))
print(type(states2))
print(states1)
print(states2)

# Problem 2

# Use a dictionary object from Problem 1 to complete the following:
# Retrieve the value for the key 'California'
# Add the State: Capital pair for Florida to the dictionary
# Update the capital of California to 'Sacremento'
# Delete Alaska from the Dictionary'

print(states1["California"])
states1["Florida"] = "Tallahassee"
states1["California"] = "Sacremento"
del states1["Alaska"]
print(states1)


# Problem 3

# Use the dictionary methods and for loop examples above to complete the following task:

# Create a dictionary object called 'playlist' with a minimum of 6 key:value pairs.
# Each Key in the dictionary should be an artist name
# Each Value should be a corresponding song by that artist
# Use a for loop to create a print statement that prints all the artists in the playlist
# Use a for loop to create a print statment that prints all the songs in the playlist
# Use a for loop to create a print statement that says: "(Song Name) by (Artist) is in the current playlist."
# Remove the last Key:Value pair from the Dictionary
# Add the song "Anti-Hero" by Taylor Swift to your playlist.
# Overwrite one of your songs to have REMIX in front of the song title
# Define & call a function that will print all the artists and songs from the object you pass into it.


playlist = {
    "Linkin Park" : "In The End",
    "Euro Trash" : "Dipped In Sugar",
    "Yellow Claw": "Crash This Party",
    "System Of A Down" : "BYOB",
    "KILLEDDY" : "STILLINTOU",
    "AREZRA" : "Goodbye"
}

for artist in playlist.keys():
    print(artist)

for song in playlist.values():
    print(song)

for artist, song in playlist.items():
    print(f"{song} by {artist} is in the current playlist")

playlist.popitem();
playlist["Taylor Swift"] = "Anti-Hero"

playlist["Euro Trash"] = "Remix " + playlist["Euro Trash"]

print(playlist)

def print_all(songlist):
    for artist, song in songlist.items():
        print(f"{song} by {artist}")


print_all(playlist)