#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:36:14 2017

@author: yuguang
"""
#include song.py
import song

class Playlist:
    def __init__(self, title):
        ''' (Playlist, str) -> NoneType
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.title
        'Canadian Artists'
        >>> playlist.songs
        []
        '''
        self.title = title
        self.songs = []
        
    def add(self, song1):
        ''' (Playlist, Song) -> NoneType
        Add song to this playlist.
        >>> stompa = song.Song('Serena Ryder', 'Stompa', 3, 16)
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(stompa)
        >>> print(playlist.songs[0])
        Serena Ryder, Stompa (3:16)
        '''
        self.songs.append(song1)
        
    def get_duration(self):
        ''' (Playlist) -> (int, int)
        Return the duration of this playlist as tuple of minutes and seconds.
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 16))
        >>> playlist.get_duration()
        (8, 19)
        '''
        total_minutes = 0
        total_seconds = 0
        for song_tmp in self.songs:
            total_minutes += song_tmp.minutes
            total_seconds += song_tmp.seconds
        return (total_minutes + total_seconds // 60, total_seconds % 60)
    
    def __str__(self):
        """ (Playlist) -> str
        Return a string representation of this playlist.
        >>> playlist = Playlist('Canadian Artists')
        >>> playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
        >>> playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 16))
        >>> print str(playlist)
        Canadian Artists (8:19)
        1. Neil Young, Harvest Moon (5:03)
        2. Serena Ryder, Stompa (3:16)
        """
        duration = self.get_duration()
        minutes = str(duration[0])
        seconds = str(duration[1]).rjust(2, '0')
        result = self.title + ' (' + minutes + ':' + seconds + ')'
        # Append the songs in the playlist.
        i = 1
        for song_tmp in self.songs:
            result += '\n' + str(i) + '. ' + str(song_tmp)
            i += 1
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    playlist = Playlist('Canadian Artists')
    playlist.add(song.Song('Neil Young', 'Harvest Moon', 5, 3))
    playlist.add(song.Song('Serena Ryder', 'Stompa', 3, 16))
    print(playlist)
        
        
        
        
        
        
        
        
        