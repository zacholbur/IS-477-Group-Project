import kaggle
import pandas as pd
import os

kaggle.api.authenticate()

kaggle.api.dataset_download_files('paradisejoy/top-hits-spotify-from-20002019', path='.', unzip=True)
os.rename("songs_normalize.csv","SpotifySubset.csv")

kaggle.api.dataset_download_files("sansastark/subset-of-the-million-song-dataset", path='.', unzip=True)
os.remove("billboard_rank.csv")
