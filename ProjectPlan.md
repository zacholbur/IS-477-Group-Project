Overview:
	The aim of this project will be to determine the extent to which analysis of relevant patient data can provide insight into the topic of breast cancer. Specifically, we want to see the role such methods can play in identifying the presence or absence of breast cancer given the details of a particular tumor.

Research Question(s): 
	Our project will seek to answer two main research questions in order to tackle this topic.
More broadly, we will seek to answer the question,”What factors of a tumor in a breast cancer patient are most relevant in determining the diagnosis (malignant or benign) for a tumor?”. More specifically, we will want to answer the question, “How accurately can tumor size and location predict whether a breast tumor is malignant or benign?”. 

Team: 
	Regarding our team, we plan to discuss each step of the project together first at a higher level in order to ensure we are aligned on a single vision for the project. From there, we can each specialize in particular areas within the project. We will discuss the data lifecycle and ethical data handling together. From there, Zach will specialize in data collection and acquisition, extraction and enrichment, and data quality. Dan will specialize in storage and organization, data integration, and data cleaning. Workflow automation and provenance and reproducibility and transparency will be focused on by both members. Throughout, we will both focus on documenting the data providing relevant metadata. By specializing in an area, that does not mean the team member will be the sole person working on that section, but rather that they will take charge in the primary planning, oversight, and delegating of that portion of the project to ensure for effective completion. 

Datasets:

Both of our datasets will be acquired from the UC Irvine Machine Learning Repository. 

Here are the two data sets and the considerations regarding them: 

Tumor size consideration: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic 

This first data set is called Breast Cancer Wisconsin (Diagnostic). This dataset describes breast cancer diagnostic data, where each record represents a tumor sample with both identifying information and cell features used to predict whether the tumor is benign or malignant. According to the article, “Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.  They describe characteristics of the cell nuclei present in the image.”

Tumor location considerations: 
https://archive.ics.uci.edu/dataset/14/breast+cancer
The second data set is called Breast Cancer. This dataset relates to breast cancer recurrence, and contains patient demographic and clinical information used to predict whether cancer will recur or not recur after treatment. It includes 286 total instances where each instance is described by 9 predictive features and 1 binary target variable.

Overall, we hope to utilize the information outlined in these datasets to answer our research question, as well as better understand breast cancer and its features.

Timeline:
The following outline provides a rough timeline for our project completion: 
Week 7 (October 6 - October 12): We will begin by focusing on developing our data lifecycle and creating a plan to address relevant ethical data handling considerations. Zach will primarily focus on the data lifecycle and Dan will focus on the ethical data handling. This should be a lighter workload, which will provide us space to make any necessary adjustments upon receiving feedback on this project plan.  
Week 8 (October 13 - October 19): After this, we will focus on creating a script to collect and acquire our data, and also develop our structure for storing and organizing the data. Zach will specialize in the data collection and acquisition, and Dan will focus on the data storage and organization.
Week 9 (October 10  - October 26): In week 9, we will focus on extraction and enrichment, as well as creating our script for integrating our two data sources together. Zach will be in charge of enrichment and extraction, and Dan will focus on data integration.
Week 10 (October 27 - November 2): Here, we will address data quality and data cleaning. Zach will spend time analyzing the data to identify data quality concerns and Dan will work on addressing those concerts through cleaning the data
Week 11 (November  3 - November 9): Week 11 will serve as our primary week for conducting our data analysis. Given the importance of this step, we will work together to analyze the data and create the necessary visualizations to explain our findings.
Week 12 (November 10 - November 16): After conducting the data analysis, we will focus on creating our workflow automation. This step will be all encompassing, and as such, we will work together. During this process, each team member will focus on the portions of the workflow that they have previously specialized in.
Week 13 (November 17 - November 23): Week 12 will provide us an opportunity to review our project through the lens of reproducibility and transparency and make any necessary changes to ensure these two goals have been clearly accomplished. We will also review our work to ensure the proper metadata has been provided and data has been documented. This step will be done together.
Weeks 14-16 (November 24 - December 10): These last weeks will be reserved for final quality checks, revisions, and implementing any other feedback we have received. This will also provide us the time needed to organize and finalize the necessary documents needed for our final project submission.

Constraints: 
The first identifiable constraint is medical knowledge. Zach and Dan lack background in the field of medicine, especially when it comes to cancer and understanding features of a tumor. It will take a lot of research beyond simple data analysis to truly understand what the data is telling us. This can be done through consulting peer reviewed articles and identifying similar studies to ours.
Another constraint is available data. In total, our data sets sum up to around 1000 rows. This means that we are working with limited data which can introduce biases based on the region the data was collected as well as who was chosen for the study. More rows would have been ideal, however, we are confident 1000 can fit the purposes of our research.

Gaps: 
Perhaps features beyond just tumor sizes can be beneficial for this study. Factors like demographic information regarding race, smoking habits/other carcinogen consumption, family history, etc. can help better answer our research questions. Additionally, a deeper understanding of the variables would help fill some of the gaps within our knowledge. Features like concavity, compactness, and smoothness regarding the tumors do not mean a lot to us currently, but with proper research, we can understand our data better.

