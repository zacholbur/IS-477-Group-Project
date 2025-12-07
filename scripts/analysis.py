import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import os

if not os.path.exists("results"):
    os.makedirs("results")

df = pd.read_csv("data/processed/Integrated.csv")
audio_features = [
    "popularity", "danceability", "energy", "key", "mode", "loudness",
    "speechiness", "acousticness", "instrumentalness",
    "liveness", "valence", "tempo",
    "ArtistFamiliarity", "Hotness"
]
cols = [c for c in audio_features if c in df.columns]

plt.figure(figsize=(14, 10))
sns.heatmap(df[cols].corr(), annot=False, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap of Audio Features (Full Feature Set)")
plt.savefig("results/correlation_heatmap.png")
plt.close()


plt.figure(figsize=(14, 10))

# Popularity vs Energy
plt.subplot(2, 3, 1)
sns.scatterplot(data=df, x="energy", y="popularity", alpha=0.5)
plt.title("Popularity vs Energy")

# Popularity vs Loudness
plt.subplot(2, 3, 2)
sns.scatterplot(data=df, x="loudness", y="popularity", alpha=0.5)
plt.title("Popularity vs Loudness")

# Popularity vs Speechiness
plt.subplot(2, 3, 3)
sns.scatterplot(data=df, x="speechiness", y="popularity", alpha=0.5)
plt.title("Popularity vs Speechiness")

# Popularity vs Acousticness
plt.subplot(2, 3, 4)
sns.scatterplot(data=df, x="acousticness", y="popularity", alpha=0.5)
plt.title("Popularity vs Acousticness")

# Popularity vs Valence
plt.subplot(2, 3, 5)
sns.scatterplot(data=df, x="valence", y="popularity", alpha=0.5)
plt.title("Popularity vs Valence")

# Popularity vs Tempo
plt.subplot(2, 3, 6)
sns.scatterplot(data=df, x="tempo", y="popularity", alpha=0.5)
plt.title("Popularity vs Tempo")

plt.tight_layout()
plt.savefig("results/popularity_scatter.png")
plt.close()

genre_means = df.groupby("track_genre")["popularity"].mean().sort_values()

plt.figure(figsize=(12, 8))
sns.barplot(x=genre_means.index, y=genre_means.values, palette="rainbow")
plt.xticks(rotation=45, ha='right')
plt.title("Average Popularity by Genre")
plt.ylabel("Mean Popularity")
plt.xlabel("Genre")
plt.savefig("results/genre_popularity.png")
plt.close()


threshold = df['popularity'].quantile(0.95)
df['is_hit'] = df['popularity'] >= threshold

hit_summary = df.groupby("is_hit")[[
    "energy", "danceability", "loudness", "tempo", "acousticness",
    "instrumentalness", "liveness", "valence", "speechiness"
]].mean().T

with open("results/hit_summary.txt", "w") as f:
    print("Hit vs Non-Hit Summary Statistics:", file=f)
    print(hit_summary, file=f)


hits = df[df['is_hit'] == True]

plt.figure(figsize=(6,4))
sns.countplot(data=hits, x="mode", color="seagreen")
plt.title("Mode Distribution for Hit Songs")
plt.xticks([0, 1], ["Minor", "Major"])
plt.xlabel("Mode")
plt.ylabel("Count")
plt.savefig("results/mode_popularity.png")
plt.close()

features = [
    "danceability", "energy", "loudness", "speechiness", "acousticness",
    "instrumentalness", "liveness", "valence", "tempo",
    "key", "mode", "ArtistFamiliarity", "Hotness"
]

X = df[features]
y = df["popularity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=365
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=365
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

with open("results/model_stats.txt", "w") as f:
    print("R² Score:", round(r2, 3), file=f)
    print("RMSE:", round(rmse, 3), file=f)

    importance = pd.DataFrame({
        "feature": features,
        "importance": model.feature_importances_
    }).sort_values("importance", ascending=False)

    print("\nFeature Importance:", file=f)
    print(importance.to_string(index=False), file=f)
    print("-" * 30, file=f)