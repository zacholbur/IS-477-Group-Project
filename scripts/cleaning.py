import pandas as pd

df_spotify = pd.read_csv("../data/raw/SpotifyRaw.csv")

df_spotify["ArtistLower"] = df_spotify["artists"].str.lower()
df_spotify["SongLower"] = df_spotify["track_name"].str.lower()


df_spotify = df_spotify[df_spotify["popularity"] != 0]
df_spotify = df_spotify.drop_duplicates()
df_spotify = df_spotify.drop_duplicates(subset=['ArtistLower','SongLower'], keep='last')

df_spotify.to_csv("../data/processed/SpotifyCleaned.csv")

df_million_song = pd.read_csv("../data/raw/MillionSongRaw.csv")

df_million_song["ArtistLower"] = df_million_song["ArtistName"].str.lower()
df_million_song["SongLower"] = df_million_song["Title"].str.lower()

df_million_song = df_million_song.drop(["ArtistLongitude", "ArtistLocation","ArtistLatitude","Danceability", "Energy"], axis=1)
df_million_song = df_million_song.sort_values("Year").drop_duplicates(subset=["ArtistLower", "SongLower"], keep='last')
df_million_song = df_million_song.drop(["Year"], axis=1)

df_million_song.to_csv("../data/processed/MillionSongCleaned.csv")