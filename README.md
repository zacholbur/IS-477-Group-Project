# Project Report: Title

## Contributors
- Dan Feder (djfeder2)
- Zach Olbur (zolbur2)
## Summary

## Data Profile
### Dataset Descriptions
**Spotify Dataset:** Our first dataset includes song information from Spotify. While we pull the information from huggingface, a third party source, the data was originally gathered by the author of the data using the Spotify Web API. Each observation in this dataset represents one track (one song on Spotify). This dataset includes a few different types of information, including the song’s identifying information, audio feature details, and other descriptive information. Identifying information includes fields such as artists, album name, and track name. There are many audio feature details and other descriptive information provided, such as the song’s energy, danceability, loudness, duration, and temp. More information on these fields can be found in the data dictionary provided. Most notably, this dataset also contains the song’s popularity, which is the focus of our research question. There are 114,000 observations in total in this dataset, which are drawn from a wide variety of artists, genres, and popularity levels.

**Million Song Dataset:** Our second dataset includes additional song information. Similarly to the Spotify dataset, this dataset, pulled from Kaggle, a third party source. However the original source of this data is the Million Song Dataset, a dataset created in 2011 by Columbia University’s Laboratory for the Recognition and Organization of Speech and Audio along with The Echo Nest, a music intelligence company. In addition to the full dataset, which contained one million songs, they also released a representative 10,000 song subset of the full dataset. The dataset we use is that 10,000 song subset of the Million Song Dataset. Similarly to the spotify dataset, each observation in this dataset is also a specific track, or instance of a song. The dataset includes identifying information on the songs as well as descriptive information and audio feature details. It contains a lot of similar information to the spotify dataset,including the artist name, album name, song name, song duration, and song temp. However, it also includes a few additional fields that will be valuable during analysis and are not in the spotify dataset, such as artist familiarity and artist hotness (relative buzz surrounding the artist at the time of the dataset’s creation). More information on these fields can be found in the data dictionary provided. This dataset contains 10,000 observations and draws from a variety of artists, genres, and release years.

### Ethical & Legal Considerations


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
