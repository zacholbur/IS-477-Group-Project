import kaggle
import pandas as pd
import os
import hashlib

df_spotify = pd.read_csv("hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv", index_col=0)
if os.path.exists("../data/raw/SpotifyRaw.csv"):
    os.remove("../data/raw/SpotifyRaw.csv")
df_spotify.to_csv("../data/raw/SpotifyRaw.csv")


kaggle.api.authenticate()
kaggle.api.dataset_download_files("sansastark/subset-of-the-million-song-dataset", path='../data/raw/', unzip=True)
if os.path.exists("../data/raw/billboard_rank.csv"):
    os.remove("../data/raw/billboard_rank.csv")
if os.path.exists("../data/raw/MillionSongSubset.csv"):
    if os.path.exists("../data/raw/MillionSongRaw.csv"):
        os.remove("../data/raw/MillionSongRaw.csv")
    os.rename("../data/raw/MillionSongSubset.csv","../data/raw/MillionSongRaw.csv")
df_million_song = pd.read_csv("../data/raw/MillionSongRaw.csv")

with open("../data/raw/SpotifyRaw.csv", "rb") as f:
   observations_bytes = f.read()
spotify_hash = hashlib.sha256(observations_bytes).hexdigest()
with open("../data/raw/SpotifyHash.txt","r") as f:
   if spotify_hash == f.read().strip():
      print("Spotify dataset matches reference")
   else:
      raise ValueError("Spotify dataset does not matche reference!")
   
with open("../data/raw/MillionSongRaw.csv", "rb") as f:
   observations_bytes = f.read()
million_song_hash = hashlib.sha256(observations_bytes).hexdigest()
with open("../data/raw/MillionSongHash.txt","r") as f:
   if million_song_hash == f.read().strip():
      print("Million Song dataset matches reference")
   else:
      raise ValueError("Million Song dataset does not match reference!")
