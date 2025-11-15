## Description of changes to project plan

After submitting our project plan, we realized that our datasets were not going to be able to be integrated. This is primarily because while they were both focused on the topic of breast cancer, they shared no common identifying information, so there would be no way to link records from one dataset to the other. We posted on CampusWire asking for advice on this, and were directed by the TAs to choose new datasets for our project. As a result, we have decided to take this project in an entirely new direction with new datasets and a new research purpose. Below is the new direction of our project.

**New project aim:** The new aim of this project is to better understand how audio data can provide insight into the popularity of music. Specifically, we want to understand how audio features from the datasets can be used to identify if a song will become popular based on many different music related variables.
We want to recommend music to listeners based on aspects of a song, as well as encourage inspiring musicians to add aspects to their songs that might help them become more popular.

**New research questions:** Can we calculate the popularity of a song based on factors like key signature, tempo, and other relevant variables?

**Broader research question:** What audio features contribute most strongly to popularity of a song?

**New Datasets:** Our first new dataset includes song information from Spotify. While we pull the information from a third party source, the data was originally gathered using the Spotify API. This dataset includes identifying information such as artist, album, song title, and year of release, as well as descriptive information such as popularity, danceability, loudness, and energy. This dataset can be found in this repository at Data/SpotifySubset.csv.

Our second dataset includes additional song information. While it is most directly pulled from Kaggle, the original source of this data is the Million Song Dataset, which was created by Columbia University’s Laboratory for the Recognition and Organization of Speech and Audio along with The Echo Nest, a music intelligence company. Our dataset is a small subset of the Million Song Dataset. This dataset contains similar information on different songs, with identifying information such as artists, album, song title, and year of release, and descriptive information such as loudness and energy. It also contains additional descriptive information, including tempo, artist familiarity, and key. This dataset can be found in this repository at Data/MillionSongSubset.csv.

**New constraints:** Potential biases in the data. Because the portion of our data with the emotion labels come from Spotify, it mainly reflects the listening habits of Spotify users, which may lean towards more Western or mainstream music. As a result, our emotional clusters might not fully represent global listening patterns. This might mean specifying our analysis towards an American audience to avoid this issue.
We also encounter issues in the datasets like inconsistent genre labels, duplicate tracks, and missing values. These challenges require a bit more cleaning and validation before we can fully complete analysis. One final constraint is that the spotify data is from 2010 to 2019, which is a limited range that doesn’t contain the most recent data.

## Update on Tasks
Due to time spent changing our datasets and developing a new research question and project direction, we have not made as much progress as we initially planned for in the project plan. However, as will be shown in the timeline to follow these task updates, we are confident that we are still on a good schedule to comfortably complete the project. 

**Ethical data handling:** Given that our two datasets are from third party sites, Kaggle and HuggingFace, we reviewed the original sources and the related terms of services. We determined that we were permitted to use the relevant data. Our next step with this task will be to detail these findings in a document and outline any other ethical data handling considerations and concerns.

**Data collection** and acquisition: We have successfully acquired the data and have created a script to download the data in an automated fashion. The relevant script is “aquisiton.py”, and the resulting csv files can be found in the data folder of our repository. The final step for this task will be to use hashing to ensure the integrity of the data after it is acquired. 

**Storage and organization:** We have determined that our data best lends itself towards being stored in a csv within a file system. Our next step for this task will be to more clearly document our rationale behind this and outline our storage structure. 
Data integration: We have conducted a proof of concept for data integration, which can be found at add github location. The full scale data integration will need to be completed still (see timeline for more information).

The following tasks still to be completed:
- Diagram relating our process to a specific data lifecycle model
- Data quality
- Data cleaning
- Data Analysis
- Workflow automation and provenance 
- Review of Metadata and data documentation 

## Updated Timeline for Remainder of Project

- **Already completed:** At the time of this status report submission, we made some progress towards the ethical data handling, data collection & acquisition, and storage & organization portions of the project. Additionally, we have conducted an initial data integration proof of concept. 

- **Week 13 (November 17 - November 23):** Our goal for week 13 will be to conduct the data quality assessment and subsequent data cleaning. We will also finish the last step of data acquisition, which is the hashing, complete a full scale data integration, and create the documents/write-ups to complete the ethical data handling and storage & organization tasks. At this point, our data should be ready to conduct analysis on.

- **Weeks 14-15 (November 24 - December 7):** During these weeks, we will conduct the data analysis and produce the related visualizations. Additionally, we will focus on workflow automation and provenance. Both team members will be involved in this process. We will also begin to spend time organizing and creating drafts of the necessary documents needed for our final project submission.

- **Week 16 (December 8 - 10):** These final few days will provide us the time needed to evaluate the reproducibility and transparency of our project as well as the metadata and data documentation. We will make any necessary adjustments and/or additions. We will then also finalize the other written sections of our final report, at which point our project will be complete. 

## **Contribution Summary**

#### Dan Feder:
Thus far, a large part of my focus has been on the data collection and acquisition process. Once Zach found the datasets we wanted to use for this new pivot on the project, I worked on locating the origin of these datasets and then researching how to best acquire the data. We decided to look for a different second music dataset that didn’t originate from the Spotify API, at which point I conducted the research to identify and acquire this second dataset. I reviewed the original sources of these datasets to ensure that we were allowed to use them. From there I wrote a script to automatically download the csv files directly from Kaggle and HuggingFace to enhance reproducibility. 

Regarding the project plan and status report, I developed the initial timeline for our first project focus, and then also created the revised timeline for our new project focus. I also wrote the updates on each of the tasks for this status report, and outlined our new datasets under the changes to our project plan section. 

#### Zach Olbur:
For the project so far, a lot of my tasks revolved around data exploration. Initially I had chosen two breast cancer datasets. Through some analysis (referenced in 477_project_work_pre_pivot.py) I found that the initial files were not integratable. They shared no common attributes which made it almost impossible to merge them together. From there, we decided to choose new datasets. The datasets we ended up choosing were two Spotify datasets. Both from the Spotify API, however, one was the most popular songs and the other was general songs. With this dataset, I was able to do an exact merge on the two (reference in Exploring New DF Option (Spotify Data).py). However, we have decided to look into a new data set in addition to only one of these spotify datasets. The purpose for this is to add variations into where we are pulling the data from. We currently only have 1 other dataset with not too many matching rows so more work has to be done to merge them.
With this pivot, we were held back on progress for a bit, however, my contributions included updating our project plan to reflect the changes in our project along with a new timeline for our work. My completed task included starting the data integration between the two datasets.

