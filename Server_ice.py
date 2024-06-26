# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.7
#
# <auto-generated>
#
# Generated from file `Server.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Server
_M_Server = Ice.openModule('Server')
__name__ = 'Server'

if 'Song' not in _M_Server.__dict__:
    _M_Server.Song = Ice.createTempClass()
    class Song(Ice.Value):
        def __init__(self, id='', title='', album='', artist='', duration=0, artwork='', path=''):
            self.id = id
            self.title = title
            self.album = album
            self.artist = artist
            self.duration = duration
            self.artwork = artwork
            self.path = path

        def ice_id(self):
            return '::Server::Song'

        @staticmethod
        def ice_staticId():
            return '::Server::Song'

        def __str__(self):
            return IcePy.stringify(self, _M_Server._t_Song)

        __repr__ = __str__

    _M_Server._t_Song = IcePy.defineValue('::Server::Song', Song, -1, (), False, False, None, (
        ('id', (), IcePy._t_string, False, 0),
        ('title', (), IcePy._t_string, False, 0),
        ('album', (), IcePy._t_string, False, 0),
        ('artist', (), IcePy._t_string, False, 0),
        ('duration', (), IcePy._t_int, False, 0),
        ('artwork', (), IcePy._t_string, False, 0),
        ('path', (), IcePy._t_string, False, 0)
    ))
    Song._ice_type = _M_Server._t_Song

    _M_Server.Song = Song
    del Song

if '_t_SongList' not in _M_Server.__dict__:
    _M_Server._t_SongList = IcePy.defineSequence('::Server::SongList', (), _M_Server._t_Song)

_M_Server._t_Hello = IcePy.defineValue('::Server::Hello', Ice.Value, -1, (), False, True, None, ())

if 'HelloPrx' not in _M_Server.__dict__:
    _M_Server.HelloPrx = Ice.createTempClass()
    class HelloPrx(Ice.ObjectPrx):

        def sayHello(self, context=None):
            return _M_Server.Hello._op_sayHello.invoke(self, ((), context))

        def sayHelloAsync(self, context=None):
            return _M_Server.Hello._op_sayHello.invokeAsync(self, ((), context))

        def begin_sayHello(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_sayHello.begin(self, ((), _response, _ex, _sent, context))

        def end_sayHello(self, _r):
            return _M_Server.Hello._op_sayHello.end(self, _r)

        def shutdown(self, context=None):
            return _M_Server.Hello._op_shutdown.invoke(self, ((), context))

        def shutdownAsync(self, context=None):
            return _M_Server.Hello._op_shutdown.invokeAsync(self, ((), context))

        def begin_shutdown(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_shutdown.begin(self, ((), _response, _ex, _sent, context))

        def end_shutdown(self, _r):
            return _M_Server.Hello._op_shutdown.end(self, _r)

        def add(self, id, title, album, artist, duration, artwork, path, context=None):
            return _M_Server.Hello._op_add.invoke(self, ((id, title, album, artist, duration, artwork, path), context))

        def addAsync(self, id, title, album, artist, duration, artwork, path, context=None):
            return _M_Server.Hello._op_add.invokeAsync(self, ((id, title, album, artist, duration, artwork, path), context))

        def begin_add(self, id, title, album, artist, duration, artwork, path, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_add.begin(self, ((id, title, album, artist, duration, artwork, path), _response, _ex, _sent, context))

        def end_add(self, _r):
            return _M_Server.Hello._op_add.end(self, _r)

        def update(self, id, title, album, artist, duration, artwork, path, context=None):
            return _M_Server.Hello._op_update.invoke(self, ((id, title, album, artist, duration, artwork, path), context))

        def updateAsync(self, id, title, album, artist, duration, artwork, path, context=None):
            return _M_Server.Hello._op_update.invokeAsync(self, ((id, title, album, artist, duration, artwork, path), context))

        def begin_update(self, id, title, album, artist, duration, artwork, path, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_update.begin(self, ((id, title, album, artist, duration, artwork, path), _response, _ex, _sent, context))

        def end_update(self, _r):
            return _M_Server.Hello._op_update.end(self, _r)

        def delete(self, id, context=None):
            return _M_Server.Hello._op_delete.invoke(self, ((id, ), context))

        def deleteAsync(self, id, context=None):
            return _M_Server.Hello._op_delete.invokeAsync(self, ((id, ), context))

        def begin_delete(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_delete.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_delete(self, _r):
            return _M_Server.Hello._op_delete.end(self, _r)

        def library(self, context=None):
            return _M_Server.Hello._op_library.invoke(self, ((), context))

        def libraryAsync(self, context=None):
            return _M_Server.Hello._op_library.invokeAsync(self, ((), context))

        def begin_library(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_library.begin(self, ((), _response, _ex, _sent, context))

        def end_library(self, _r):
            return _M_Server.Hello._op_library.end(self, _r)

        def findAllByTitle(self, title, context=None):
            return _M_Server.Hello._op_findAllByTitle.invoke(self, ((title, ), context))

        def findAllByTitleAsync(self, title, context=None):
            return _M_Server.Hello._op_findAllByTitle.invokeAsync(self, ((title, ), context))

        def begin_findAllByTitle(self, title, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_findAllByTitle.begin(self, ((title, ), _response, _ex, _sent, context))

        def end_findAllByTitle(self, _r):
            return _M_Server.Hello._op_findAllByTitle.end(self, _r)

        def findAllByArtist(self, artist, context=None):
            return _M_Server.Hello._op_findAllByArtist.invoke(self, ((artist, ), context))

        def findAllByArtistAsync(self, artist, context=None):
            return _M_Server.Hello._op_findAllByArtist.invokeAsync(self, ((artist, ), context))

        def begin_findAllByArtist(self, artist, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_findAllByArtist.begin(self, ((artist, ), _response, _ex, _sent, context))

        def end_findAllByArtist(self, _r):
            return _M_Server.Hello._op_findAllByArtist.end(self, _r)

        def upload(self, path, context=None):
            return _M_Server.Hello._op_upload.invoke(self, ((path, ), context))

        def uploadAsync(self, path, context=None):
            return _M_Server.Hello._op_upload.invokeAsync(self, ((path, ), context))

        def begin_upload(self, path, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_upload.begin(self, ((path, ), _response, _ex, _sent, context))

        def end_upload(self, _r):
            return _M_Server.Hello._op_upload.end(self, _r)

        def stream(self, id, context=None):
            return _M_Server.Hello._op_stream.invoke(self, ((id, ), context))

        def streamAsync(self, id, context=None):
            return _M_Server.Hello._op_stream.invokeAsync(self, ((id, ), context))

        def begin_stream(self, id, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.Hello._op_stream.begin(self, ((id, ), _response, _ex, _sent, context))

        def end_stream(self, _r):
            return _M_Server.Hello._op_stream.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Server.HelloPrx.ice_checkedCast(proxy, '::Server::Hello', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Server.HelloPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Server::Hello'
    _M_Server._t_HelloPrx = IcePy.defineProxy('::Server::Hello', HelloPrx)

    _M_Server.HelloPrx = HelloPrx
    del HelloPrx

    _M_Server.Hello = Ice.createTempClass()
    class Hello(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Server::Hello')

        def ice_id(self, current=None):
            return '::Server::Hello'

        @staticmethod
        def ice_staticId():
            return '::Server::Hello'

        def sayHello(self, current=None):
            raise NotImplementedError("servant method 'sayHello' not implemented")

        def shutdown(self, current=None):
            raise NotImplementedError("servant method 'shutdown' not implemented")

        def add(self, id, title, album, artist, duration, artwork, path, current=None):
            raise NotImplementedError("servant method 'add' not implemented")

        def update(self, id, title, album, artist, duration, artwork, path, current=None):
            raise NotImplementedError("servant method 'update' not implemented")

        def delete(self, id, current=None):
            raise NotImplementedError("servant method 'delete' not implemented")

        def library(self, current=None):
            raise NotImplementedError("servant method 'library' not implemented")

        def findAllByTitle(self, title, current=None):
            raise NotImplementedError("servant method 'findAllByTitle' not implemented")

        def findAllByArtist(self, artist, current=None):
            raise NotImplementedError("servant method 'findAllByArtist' not implemented")

        def upload(self, path, current=None):
            raise NotImplementedError("servant method 'upload' not implemented")

        def stream(self, id, current=None):
            raise NotImplementedError("servant method 'stream' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Server._t_HelloDisp)

        __repr__ = __str__

    _M_Server._t_HelloDisp = IcePy.defineClass('::Server::Hello', Hello, (), None, ())
    Hello._ice_type = _M_Server._t_HelloDisp

    Hello._op_sayHello = IcePy.Operation('sayHello', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Hello._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Hello._op_add = IcePy.Operation('add', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_Server._t_Song, False, 0), ())
    Hello._op_update = IcePy.Operation('update', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_Server._t_Song, False, 0), ())
    Hello._op_delete = IcePy.Operation('delete', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    Hello._op_library = IcePy.Operation('library', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Server._t_SongList, False, 0), ())
    Hello._op_findAllByTitle = IcePy.Operation('findAllByTitle', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Server._t_SongList, False, 0), ())
    Hello._op_findAllByArtist = IcePy.Operation('findAllByArtist', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Server._t_SongList, False, 0), ())
    Hello._op_upload = IcePy.Operation('upload', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Server._t_Song, False, 0), ())
    Hello._op_stream = IcePy.Operation('stream', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_string, False, 0), ())

    _M_Server.Hello = Hello
    del Hello

# End of module Server
