import kaggle
import pandas as pd

kaggle.api.authenticate()
kaggle.api.dataset_download_files('paradisejoy/top-hits-spotify-from-20002019', path='.', unzip=True)

df_kaggle = pd.read_csv("songs_normalize.csv")
df_huggingface = pd.read_csv("hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv")

df_huggingface.to_csv("huggingface_songs.csv")