import pymongo

client = pymongo.MongoClient('mongodb+srv://moag:I1wb7IkTDFnayFtn@maincluster.6imaj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client["soup"]
songs = db["songs"]

first_record = {
    "title": "Stronger",
    "album": " Graduation",
    "artist": "Kanye West",
    "duration":311,
    "artwork":"/artworks/default.png",
    "path":"songs/Stronger-Kanye_West.mp3"
}

#inserted_record = songs.insert_one(first_record)

def insert(song):
    return songs.insert_one(song)

def update(song):
    return songs.update_one(song)

def delete(id):
    return songs.delete_one(id)

def findAll():
    return songs.find({})

def findAllByTitle(title):
    return songs.find({"title": title})

def findAllByArtist(artist):
    return songs.find({"artist":artist})



