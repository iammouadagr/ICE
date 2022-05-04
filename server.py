import sys
import Ice
import signal
import db
import os
import vlc

Ice.loadSlice('Server.ice')
import Server


class HelloI(Server.Hello):
    def sayHello(self, current):
        print("Hello World!")
        print(db.findOneByTitle("Stronger"))


    def shutdown(self, current):
        current.adapter.getCommunicator().shutdown()

    def add(self,title,album,artist,duration,artwork,path,current):
        newRecord = {
                "title": title,
                "album": album,
                "artist": artist,
                "duration": duration,
                "artwork": artwork,
                "path": path
        }
        print("Song added success")
        return db.insert(newRecord)

    def findAllByTitle(self,title,current):
        results = []
        for song in db.findAllByTitle(title):
            if song:
                song['_id'] = str(song['_id'])
                results.append(Server.Song(song['_id'],
                                           song['title'],
                                           song['album'],
                                           song['artist'],
                                           song['duration'],
                                           song['artwork'],
                                           song['path']))
        for song in results:
            print(song)
        return results

    def findAllByArtist(self,artist,current):
        results = []
        for song in db.findAllByArtist(artist):
            if song:
                song['_id'] = str(song['_id'])
                results.append(Server.Song(song['_id'],
                                           song['title'],
                                           song['album'],
                                           song['artist'],
                                           song['duration'],
                                           song['artwork'],
                                           song['path']))
        for song in results:
            print(song)
        return results
    def library(self,current):
        results =[]
        for song in db.findAllByArtist():
            if song:
                song['_id'] = str(song['_id'])
                results.append(Server.Song(song['_id'],
                                           song['title'],
                                           song['album'],
                                           song['artist'],
                                           song['duration'],
                                           song['artwork'],
                                           song['path']))
        for song in results:
            print(song)
        return results

    def stream(self,songId,current):

        songToStream = {}
        hostName = "localhost"
        library = db.findAll();
        songExists = [m for m in library if str(m['_id']) == songId]

        if len(songExists) <=0:
            return None
        for song in songExists:
            print(song)
            songToStream = song

        path = os.path.join(os.path.dirname(__file__), songToStream["path"])
        print(path)
        if not os.path.exists(path):
            return None

        port = 8008
        urlPath = str(port)+"/stream"+str(songToStream['_id'])+".mp3"
        streamStr = "#transcode{acodec=mp3,ab=128,channels=2,samplerate=44100}:http{dst=:" + str(urlPath) + "}"

        myVlcInstance = vlc.Instance()

        output = myVlcInstance.vlm_add_broadcast(
            bytes(songId, 'utf-8'),
            bytes(path, 'utf-8'),
            bytes(streamStr, 'utf-8'),
            0,
            [],
            True,
            False)

        print("Broadcast created!")

        url = "http://" + hostName + ":" + urlPath;

        if output != 0:
            print("Broadcast error")
            return None

        myVlcInstance.vlm_play_media(songId)
        print(url);
        return url






with Ice.initialize(sys.argv,"config.server") as communicator:
#with Ice.initialize(sys.argv) as communicator:

    #
    # Install a signal handler to shutdown the communicator on Ctrl-C
    #
    signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown())

    #
    # The communicator initialization removes all Ice-related arguments from argv
    #
    if len(sys.argv) > 1:
        print(sys.argv[0] + ": too many arguments")
        sys.exit(1)

    adapter = communicator.createObjectAdapter("Hello")
    adapter.add(HelloI(), Ice.stringToIdentity("hello"))
    adapter.activate()
    communicator.waitForShutdown()

