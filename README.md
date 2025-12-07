# Project Report: Title

## Contributors
- Dan Feder (djfeder2)
- Zach Olbur (zolbur2)
## Summary
### Project Description
The aim of our project is to understand how audio data and other descriptive information can provide insight into the popularity of music. In this project we will look at two datasets containing information on specific songs. One dataset focuses on songs gathered using the Spotify Web API and the other is centered around song data from a subset of the Million Song Dataset. To accomplish the aim of our project we take this data through a series of steps, including acquisition, quality assessment, data cleaning, data integration, and finally data analysis. 
 
### Project Motivation
Through this project, we are seeking to to understand how audio data and descriptive information contribute to the popularity. Specifically, we hope to observe the relationship between different features and song popularity and also identify which factors contribute most heavily to song popularity. We see the results of this project being useful in a couple of ways. To start, these findings could help encourage inspiring musicians to add aspects to their songs that might help them become more popular. Additionally, these findings could provide a framework for labels to evaluate songs by when choosing which artists to sign. Finally, this project could be used as the foundation for developing a platform that recommends songs to listeners based on their preferences.

### Research Questions
Through this project, we are aiming to answer a two related questions:

Our primary aim is that we want to answer this research question: “Can we use the audio data and descriptive information of a song to predict its popularity? We will train a machine learning model to attempt to answer this question.

We also hope to address this broader research question: “What audio features and descriptive information contribute most strongly to popularity of a song?”. To accomplish this, we will observe the relationships between fields in our dataset, and also analyze the specific details of our trained machine learning model.

### Findings
Our analysis revealed several meaningful patterns across the dataset. The first is that musical features like loudness and energy, valence and danceability, and artist familiarity and hotness are highly correlated which helps us interpret later results more accurately. Some visualizations offered limited insight, but our genre analysis clearly showed that soul, piano, emo, and reggae tend to produce more popular tracks. When we compared the top 5% of songs (“hits”) to the rest, we found that higher energy, stronger danceability, and major keys were all commonalities between successful songs. Finally, our regression model achieved an R² of 0.179 which seems realistic since popularity often depends on external social and commercial factors beyond the audio features themselves.

## Data Profile
### Dataset Descriptions
**Spotify Dataset:** Our first dataset includes song information from Spotify. While we pull the information from huggingface, a third party source, the data was originally gathered by the author of the data using the Spotify Web API. Each observation in this dataset represents one track (one song on Spotify). This dataset includes a few different types of information, including the song’s identifying information, audio feature details, and other descriptive information. Identifying information includes fields such as artists, album name, and track name. There are many audio feature details and other descriptive information provided, such as the song’s energy, danceability, loudness, duration, and temp. More information on these fields can be found in the data dictionary provided. Most notably, this dataset also contains the song’s popularity, which is the focus of our research question. There are 114,000 observations in total in this dataset, which are drawn from a wide variety of artists, genres, and popularity levels.

**Million Song Dataset:** Our second dataset includes additional song information. Similarly to the Spotify dataset, this dataset, pulled from Kaggle, a third party source. However the original source of this data is the Million Song Dataset, a dataset created in 2011 by Columbia University’s Laboratory for the Recognition and Organization of Speech and Audio along with The Echo Nest, a music intelligence company. In addition to the full dataset, which contained one million songs, they also released a representative 10,000 song subset of the full dataset. The dataset we use is that 10,000 song subset of the Million Song Dataset. Similarly to the spotify dataset, each observation in this dataset is also a specific track, or instance of a song. The dataset includes identifying information on the songs as well as descriptive information and audio feature details. It contains a lot of similar information to the spotify dataset,including the artist name, album name, song name, song duration, and song temp. However, it also includes a few additional fields that will be valuable during analysis and are not in the spotify dataset, such as artist familiarity and artist hotness (relative buzz surrounding the artist at the time of the dataset’s creation). More information on these fields can be found in the data dictionary provided. This dataset contains 10,000 observations and draws from a variety of artists, genres, and release years.

### Ethical & Legal Considerations
For this project, we used the Spotify Tracks Dataset from Hugging Face and a subset of the Million Song Dataset from Kaggle. Both datasets focus entirely on songs and audio-based features rather than people, which helped minimize any concerns related to respect for persons and consent. Nothing in these datasets contains personal listener information, account data, or anything that could be tied back to an individual, so the ethical risks around confidentiality are very low.
The Spotify dataset is released under a BSD license, which allows reuse as long as proper attribution is given. Since the dataset only includes derived audio features and not the copyrighted audio itself, using and analyzing it should fall well within what the license allows. We do not redistribute the raw files but instead direct others to the original sources.
For the Million Song Dataset, the Kaggle subset lists its license as “unknown,” but the original is intentionally open for academic and research use. One remaining consideration is bias. Both datasets tend to lean toward mainstream, Western music, so our results may reflect those patterns rather than the full global music landscape.




## Data Quality
### Quality Analysis Methodology
We conducted our data quality assessment and subsequent data cleaning before data integration. As a result, our quality analysis focused on distinct aspects of both the spotify dataset and million song dataset. We assessed quality through the lens of accuracy, completeness, consistency, and timeliness. Below is a summary of our assessment. The full quality assessment can be found in the workflow folder.

### Quality Analysis Summary
**Accuracy:** Both datasets were deemed to be syntactically accurate as evidenced by observing the different attribute data type choices. One consideration regarding semantic accuracy in the spotify dataset was the presence of observations with popularity scores of 0. There were 16,020 instances of this in the dataset, equating to roughly 14.05% of all observations. Upon further review, it was clear that many of these songs shouldn’t have a popularity of 0, and were inaccurate values that effectively represented missing data. Given that our research question is centered around popularity, we couldn’t move forward with these rows and removed them during data cleaning. Additionally, both the spotify and million song datasets had instances of tempos of 0. Under ordinary terms, this would have been a concern due it clearly being inaccurate. However, our final integrated dataset doesn’t contain any instances of tempos of 0, so it is not a concern for our use case.

One concern for semantic accuracy in the million song dataset was that the energy and danceability were listed as 0 for every observation. Similarly, the year column contains 5320 values of 0, equal to roughly 53.19 percent of all observations. These instances of 0s in these three fields were clearly inaccurate and effectively missing, and were removed during data cleaning.

One final consideration for accuracy is that these datasets were originally created using the Spotify web API and from the million song dataset. While we can’t truly confirm the origin of these datasets, the fact that they are cited as being drawn from these credible sources gives us confidence that the data correctly corresponds to the ground truth. Overall, aside from a few considerations that were addressed during data cleaning, we believe that these datasets have strong accuracy. 

**Completeness:** As mentioned above, the popularity field in the spotify dataset had effectively missing values, represented by a popularity of 0. Additionally, there was only one row in the spotify dataset with labeled missing data. However, since this row also had a popularity of 0, both of these issues were resolved by dropping observations with popularities of 0.

The million song dataset had missing values in 4 columns: ArtistLatitude (1903 missing values), ArtistLocation (1131), ArtistLongitude (1903), and mbID (8). The mbID missing was not a large concern because this identifier was not included in the final integrated dataset. To address the other three fields, we choose to remove them during dating cleaning. Additionally, as mentioned above the million song dataset’s energy, danceability, and year fields had large amounts of effectively missing data were also removed during the data cleaning process.

One final consideration is that while these two datasets contain a large amount of data,114,000 and 10,000 rows in the spotify and million song datasets respectively, this data doesn’t include all the songs that data could be collected on. To put it simply, this is not a complete dataset of all songs that in theory could be used for analysis. However, both dataset’s songs are fairly evenly distributed across different genres and the Spotify songs include a wide range of song popularities, and the million song dataset shows that it covers a wide range of different years. As such, we believe these datasets are representative and were sufficient to conduct a proper analysis on.

Overall, the missing values in popularity needed to be addressed in the spotify dataset, and missing values in ArtistLatitude, ArtistLocation, ArtistLongitude, and Year needed to be addressed in the million song dataset. Once these concerns were addressed, we believe that this data exhibits very strong completeness.
	

**Consistency:** With the exception of tempo and the million song dataset’s year column, which have already been discussed, there were not any clear domain violations within either dataset. The other consideration related to consistency is the existence of duplicate values. For our analysis, we didn’t want the same song by the same artist to exist twice in the dataset. The spotify dataset had 49,340 instances of this and 894 complete duplicates, and the million song dataset had 119 instances of this but 0 complete duplicates. This was addressed during data cleaning. Both datasets are stored in a csv and are each represented as one single table, so there was no concern of inter-relation constraints being violated for either dataset. Overall, the consistency of these datasets seem strong.

**Timeliness:** Both datasets are static datasets, meaning that their contents will not ever be updated. However, for the most part, this is not a concern. The data has incredibly low volatility, as the attributes such as artist and song title do not change for songs, and the audio features gathered are almost never updated for songs once they are created for both original sources (the spotify api and million song dataset). One additional consideration is that the spotify dataset has not been updated since 2023, and the million song dataset doesn’t contain any songs more recent than 2010. As a result, it is fair to say that they are not the most current datasets. However, we don’t believe this is necessarily an issue, as long as finders are interpreted accordingly.

### Final Assessment
Overall, the general theme that emerged from our data quality assessment is that each dimension of quality had a few considerations that needed to be addressed. However, we believe that these considerations were addressed properly during the data cleaning, integration, and analysis processes. As a result, we believe we were left with two quality datasets that were fit for use and able to be used for effective analysis.

## Findings

## Future Work

## Reproducing

## References
