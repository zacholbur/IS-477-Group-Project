import pandas as pd 
import recordlinkage as rl
df_spotify = pd.read_csv("../data/processed/SpotifyCleaned.csv", index_col=0)
df_million_song = pd.read_csv("../data/processed/MillionSongCleaned.csv", index_col=0)

df_exact_join = pd.merge(
    df_spotify,
    df_million_song,
    left_on=['ArtistLower', 'SongLower'],  
    right_on=['ArtistLower', 'SongLower'], 
    how='inner'                        
)

spotify_idxs = df_exact_join.set_index(['ArtistLower', 'SongLower']).index
df_spotify_remaining = df_spotify[~df_spotify.set_index(['ArtistLower', 'SongLower']).index.isin(spotify_idxs)].copy()

million_idxs = df_exact_join.set_index(['ArtistLower', 'SongLower']).index
df_million_song_remaining = df_million_song[~df_million_song.set_index(['ArtistLower', 'SongLower']).index.isin(million_idxs)].copy()

def first_word(name):
    first = name.strip().split()[0].lower()
    if first == "the" and len(name.strip().split()) > 1:
        first = name.strip().split()[1].lower()
    return first

df_spotify_remaining["FirstWord"] = df_spotify_remaining["ArtistLower"].apply(first_word)
df_million_song_remaining["FirstWord"] = df_million_song_remaining["ArtistLower"].apply(first_word)


indexer = rl.Index()
indexer.block("FirstWord")
pairs = indexer.index(df_spotify_remaining, df_million_song_remaining)

def get_matched_pairs(candidates, left_df, right_df):
    match_pairs = candidates.index.to_frame(index=False)
    match_pairs.columns = ["left_index", "right_index"]

    merged = (
        match_pairs
        .merge(left_df, left_on="left_index", right_index=True, suffixes=('', '_left'))
        .merge(right_df, left_on="right_index", right_index=True, suffixes=('_left', '_right'))
    )
    return merged

compare = rl.Compare()
compare.string("ArtistLower", "ArtistLower", method="levenshtein", threshold=0.5, label="Artist_Sim")
compare.string("SongLower", "SongLower", method="levenshtein", threshold=0.6, label="Song_Sim")

features = compare.compute(pairs, df_spotify_remaining, df_million_song_remaining)

candidates = features[
    (features["Artist_Sim"] == 1) &
    (features["Song_Sim"] == 1)
]

df_approx_matches = get_matched_pairs(candidates, df_spotify_remaining, df_million_song_remaining)

df_approx_matches = df_approx_matches.drop(index=[1,8,12,25,26,28,29,31,34,36,38,39,43,44,48])

df_exact_join = df_exact_join[['track_id','artists', 'album_name', 'track_name',
       'popularity', 'duration_ms', 'explicit', 'danceability', 'energy',
       'key_x', 'loudness', 'mode_x', 'speechiness', 'acousticness',
       'instrumentalness', 'liveness', 'valence', 'tempo', 'track_genre', 
       'ArtistFamiliarity','Hotness', 'end_of_fade_in', 'start_of_fade_out']]

df_approx_matches = df_approx_matches[['track_id', 'artists',
       'album_name', 'track_name', 'popularity', 'duration_ms', 'explicit',
       'danceability', 'energy', 'key_left', 'loudness', 'mode_left',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'track_genre', 'ArtistFamiliarity',
       'Hotness', 'end_of_fade_in',
        'start_of_fade_out']]

df_exact_join.columns = ['track_id', 'artists',
       'album_name', 'track_name', 'popularity', 'duration_ms', 'explicit',
       'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'track_genre', 'ArtistFamiliarity',
       'Hotness', 'end_of_fade_in','start_of_fade_out']

df_approx_matches.columns = ['track_id', 'artists',
       'album_name', 'track_name', 'popularity', 'duration_ms', 'explicit',
       'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'track_genre', 'ArtistFamiliarity',
       'Hotness', 'end_of_fade_in', 'start_of_fade_out']

df_integreated = pd.concat([df_exact_join, df_approx_matches], ignore_index=True)
df_integreated.to_csv("../data/processed/Integrated.csv")
