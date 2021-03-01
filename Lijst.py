#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:48:33 2021

@author: Job
"""
#import sys

print("Initializing client...")

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import timedelta, datetime

include_old = False

os.environ['SPOTIPY_CLIENT_ID'] = 'CLIENT_ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'CLIENTSECRET'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://www.jobvandenhurk.nl/?code=AQC3DPuor_F6ItRb72EDOfRy4DkbMf18xBRZvw40bfLmguAiB1oqwsAYFPb8rf2kJnn5eA-9J__5aPT3Rkl-oqBALVkFyw06I2ML32h5YZ5oqI5illa4bOUB5IwfuflPjJ7mDOuyvJ6kBd3wVjPOUHwoYmXi8dAVc9xbTmkHqr1LqFKrlIJAjYAXuOSByHW_Q0O_'
playlist_id = "spotify:playlist:3eWl5GKJEiDZo7YclZUF9e"
playlist_old_id = "spotify:playlist:6njDUhX0iKekg4l0wrOxGN"
username = "username_code"


def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

print("Fetching tracks...")
tracks = get_playlist_tracks(username,playlist_id)

if include_old:
    tracks_old = get_playlist_tracks(username,playlist_old_id)
    tracks = tracks + tracks_old
    
    

nroftracks = len(tracks)

users = {
    "1142407505":   {"name":"Jaap",
                    "nroftracks":0,
                    "timeoftracks":0},
    "ramon2511":    {"name":"Ramon",
                    "nroftracks":0,
                    "timeoftracks":0},
    "1118229742":   {"name":"Job",
                    "nroftracks":0,
                    "timeoftracks":0},
    "bamsnl":       {"name":"Neef",
                    "nroftracks":0,
                    "timeoftracks":0},
    "zharlock":     {"name":"Thomas",
                    "nroftracks":0,
                    "timeoftracks":0}}


playlist_duration_ms = 0

print("Doing some statistics on tracks...")
ix = 0
erase_ix = []
for track in tracks:
   
    
    if not(not(tracks[ix]["track"])):
        playlist_duration_ms = playlist_duration_ms + track["track"]["duration_ms"]
        if track["added_by"]["id"] == "1118229742":
             users["1118229742"]["nroftracks"] = users["1118229742"]["nroftracks"] + 1
             users["1118229742"]["timeoftracks"] = users["1118229742"]["timeoftracks"] + track["track"]["duration_ms"]
        if track["added_by"]["id"] == "1142407505":
             users["1142407505"]["nroftracks"] = users["1142407505"]["nroftracks"] + 1
             users["1142407505"]["timeoftracks"] = users["1142407505"]["timeoftracks"] + track["track"]["duration_ms"]        
        if track["added_by"]["id"] == "ramon2511":
             users["ramon2511"]["nroftracks"] = users["ramon2511"]["nroftracks"] + 1
             users["ramon2511"]["timeoftracks"] = users["ramon2511"]["timeoftracks"] + track["track"]["duration_ms"]  
        if track["added_by"]["id"] == "bamsnl":
             users["bamsnl"]["nroftracks"] = users["bamsnl"]["nroftracks"] + 1
             users["bamsnl"]["timeoftracks"] = users["bamsnl"]["timeoftracks"] + track["track"]["duration_ms"]  
        if track["added_by"]["id"] == "zharlock":
             users["zharlock"]["nroftracks"] = users["zharlock"]["nroftracks"] + 1
             users["zharlock"]["timeoftracks"] = users["zharlock"]["timeoftracks"] + track["track"]["duration_ms"]             
        
    else:
        erase_ix.append(ix)
    ix = ix+1  
    
# erase non-items:
for ix in sorted(erase_ix,reverse=True):
    del tracks[ix]
        
    
nye = datetime(2022, 1, 1, 00, 00)

start_of_playlist = nye - timedelta(milliseconds=playlist_duration_ms)

    
print(start_of_playlist)
print("Total tracks: %s" % (nroftracks))

for user in users:
    print(users[user]["name"] + ": %s tracks, %.2f%%, total duration %.2f hours, %.2f%%" % (users[user]["nroftracks"], (users[user]["nroftracks"]/nroftracks)*100,users[user]["timeoftracks"]/(1000*3600),  (users[user]["timeoftracks"]/playlist_duration_ms)*100))
