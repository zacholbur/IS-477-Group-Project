import kaggle
import pandas as pd
import os

df_spotify = pd.read_csv("hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv")
df_spotify.to_csv("SpotifySubset.csv")

kaggle.api.authenticate()
kaggle.api.dataset_download_files("sansastark/subset-of-the-million-song-dataset", path='.', unzip=True)
os.remove("billboard_rank.csv")
