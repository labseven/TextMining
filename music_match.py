""" Generates lyrics for any artist.
    Why pay shadow writers when a robot can do their job?

    Parameters: Artist name
    Returns: Song lyrics
"""

import requests
import json
import sys
import nltk
import markovgen
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


api_url = "https://api.musixmatch.com/ws/1.1/"
api_key = ""


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words;
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))

    sentence = ""

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return ''

        # choose a random suffix
        word = random.choice(suffixes)
        sentence = sentence + " " + word
        start = shift(start, word)

    return sentence

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)



def loadApiKey():
    global api_key
    api_key_file = open("music_match_api_key.txt", "r")
    api_key = api_key_file.read().rstrip()
    api_key = "&apikey=" + api_key


def get_song_lyrics(track_id):
    # print("Track id: " + str(track_id))

    resp = requests.get(api_url + "track.lyrics.get?track_id=" + str(track_id) + api_key)

    if resp.json()["message"]["header"]["status_code"] == 200:
        # print(resp.json()["message"]["body"]["lyrics"]["lyrics_body"])

        lyrics = resp.json()["message"]["body"]["lyrics"]["lyrics_body"] #.rstrip()


        # Remove Copyright notice
        for i in range(len(lyrics), 0, -1):
            if lyrics[i-3:i] == "...":
                lyrics = lyrics[:i-4]
                break
        print("Got song " + str(track_id))
        # print(lyrics)

    else:
        print("Error: Status " + str(resp.json()["message"]["header"]["status_code"]))
        return ""
    return lyrics



def add_lyrics(lyrics, order = 2):
    for line in lyrics.split('\n'):
        for word in line.split(' '):
            process_word(word, order)


def gen_lyrics(lines=50, num=7):
    text = ""
    for i in range(lines):
        text = text + random_text(num) + "\n"
        if(i%5 == 4):
            text = text + "\n"
    return text


def get_artist_id(artist):
    resp = requests.get(api_url + "artist.search?q_artist=" + artist + "&page_size=5" + api_key)

    artist_id = resp.json()["message"]["body"]["artist_list"][0]["artist"]["artist_id"]
    print(artist + " is artist_id " + str(artist_id))
    return artist_id


def get_artist_albums(artist_id):
    resp = requests.get(api_url + "artist.albums.get?artist_id=" + str(artist_id) + "&s_release_date=desc&g_album_name=1" + api_key)

    album_list = []
    for album in resp.json()["message"]["body"]["album_list"]:
        # print()
        # print(album['album']['album_id'])
        album_list.append(album['album']['album_id'])

    return album_list


def artist_song_list(artist):
    """ Searches for an artist, and returns a list of song ids of that artist"""

    song_list = []
    for album in get_artist_albums(get_artist_id(artist)):
        resp = requests.get(api_url + "album.tracks.get?album_id=" + str(album) + "&page=1" + api_key)
        for song in resp.json()["message"]["body"]["track_list"]:
            song_list.append(song["track"]["track_id"])

    return song_list


def process_song_list(song_ids):
    for song in song_ids:
        add_lyrics(get_song_lyrics(song))
    return 1

def process_artist(artist):
    process_song_list(artist_song_list(artist))

def main(self, artist):
    loadApiKey()
    # print(get_song_lyrics("15953433"))

    process_artist(artist)
    print()
    print("My lyrics: ")
    print(gen_lyrics(50))

if __name__ == '__main__':
    main(*sys.argv)
