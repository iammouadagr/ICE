#pragma once

module Server
{
    class Song
    {
       string id;
       string title;
       string album;
       string artist;
       int duration;
       string artwork;
       string path;
    };

    sequence<Song> SongList;

    interface Hello
    {
        void sayHello();
        void shutdown();
        Song add(string id, string title, string album, string artist, int duration, string artwork, string path);
        Song update(string id, string title, string album, string artist, int duration, string artwork, string path);
        bool delete(string id);
        SongList library();
        SongList findAllByTitle(string title);
        SongList findAllByArtist(string artist);
        Song upload(string path);
        string stream(string id);


    }
}