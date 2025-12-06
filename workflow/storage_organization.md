### Storage & Organization Outline
Our data itself is stored using common separated value (CSV) files. There are CSV files for our raw data, one for each source, CSV files for our cleaned data, also one for each source, and one CSV file containing our integrated dataset. We believe this structured form of storage is a good fit for our data, as in each file, all records share a common structure already. 	

For storing our overall project work, we have decided to use a logical file system as our storage system. We believe this will effectively allow all our materials to be organized in a manner that maximizes efficiency, transparency, and ease of use for end users.

### Naming Conventions
As is demonstrated in the detailed description below, we have emphasized choosing descriptive but brief titles for naming our folders and files. Our folders are named to best describe what information they contain, and our files are named with two factors in mind: What stage of the project they relate to and what information they contain. Depending on what we deemed to be more relevant, our file names include one of these components, and many contain both. Within our workflow folder, we have used numbers as prefixes for the file names in order to sort them in order of stepping through our workflow, from the first stage to the last. For our other folders, we do not believe order is as necessary, so they have not been sorted in any manner. Overall, we believe this naming system establishes a structure that is seamless to navigate through. 

### Filesystem Structure:
Below please find a detailed explanation of our file system:

#### Root Directory:
The root directory of our repository contains key files, including our project plan, status report, and final report markdown files, as well as a README file providing key summary information regarding our repository.

In addition to these files, our root directory includes five folders: workflow, data, results, scripts, and previous stages. Each folder will be described in detail below.

#### Workflow 
Our workflow directory contains detailed information regarding our end-to-end process for carrying out this project. Each artifact in the folder corresponds to a different project requirement and stage of our workflow. As mentioned above, these files have been named to be sorted in order of when they are carried out, from the first step to the last step of our workflow. This folder establishes complete transparency related to our project, as a user can view exactly how we conducted our project at each stage. 

#### Data
As the name suggests, our data directory contains the relevant data files for our project. This directory is made up of two sub directories, titled raw and processed. “Data/raw” contains our acquired datasets, in the form of two CSV files, one for the Spotify dataset and the other for the Million Song Dataset. Additionally, “Data/raw” contains two textfiles that store the results of our SHA-256 hashing our datasets to serve as a reference to be checked against during when our workflow is reproduced. “Data/processed” contains three CSV files, which contain our cleaned Spotify dataset, cleaned Million Song dataset, and integrated dataset.

#### Results 
The results directory contains the results of our data analysis. This is stored in the form of three different jupyter notebooks that display key insights and visualizations from our data analysis.

#### Scripts 
The scripts directory contains the python scripts related to each stage of our workflow. The purpose of these scripts is that they are called and run by our snakefile in order to reproduce our workflow in an automated manner.

#### Previous Stages
Finally, the previous stages directory includes all files from previous checkpoints of our project that are not necessary to the final version of the project. 
