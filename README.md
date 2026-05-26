# Create the Perfect Group Assignments!

## Overview
\[TBD at the end of the project\]

## Objective
Group work is a critical component of collaborative learning in academic and nonacademic settings alike. In many situations, groups are formed randomly, with little thought put into compatibility. This can lead to mismatches in communication styles, work ethics, and overall interpersonal compatibility. These issues can reduce efficiency and impact learning outcomes. 

The Big 5 Personality Traits are a psychological model that measures personality based on five factors: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. This model has been commonly used to examine individual strengths and weaknesses, which helps people to understand the types of roles that fit their personality traits and the type of people they would want to collaborate with. Through this framework, it can help create more balanced teams, resulting in more efficiency and better productivity. 

Prior research in team based scientific environments demonstrate that personality traits significantly influence collaboration quality, particularly agreeableness and conscientiousness have a large impact on group cohesion and productivity (Dwivedy et al., 2025). Therefore, it is effective to use the Big 5 Personality Traits to create compatible and collaborative teams.

Our goal is to implement a machine learning pipeline that groups individuals into their most optimal and productive team. We will do this by balancing compatibility and diversity of personality traits, rather than clustering the most similar traits together. 


## Data
1. [IPIP300 Kaggle Dataset](https://www.kaggle.com/datasets/edersoncorbari/ipip-neo-big-five-personality-300-item-version)

For our real-world dataset, we chose to use the results of the Big-Five Personality Test, which was compiled for the International Personality Item Pool (IPIP). This inventory of data is used as a means of psychological analysis. The test aims to score each individual’s openness, conscientiousness, extraversion, agreeableness, and neuroticism (OCEAN) on a scale of 1-5 according to their agreement with 300 different statements, also answered on a scale of 1-5. The dataset records 307,313 individuals and their responses to the survey, as well as their final OCEAN attribute ranking.

2. [Huggingface](https://huggingface.co/datasets/Fatima0923/Automated-Personality-Prediction)

In addition, for the option of using synthetic and simulated data, we chose to expand upon current literary reviews researching LLM’s ability to predict personality on the Big-Five metrics using input texts. Using this synthetic dataset which predicts the OCEAN personality attributes on a scale of 1-5 based on input text, we can also compare the results of clustering real-world personalities and predicted ones. This specific predictive dataset contains 20,877 rows of text inputs, along with the predicted OCEAN attribute rankings.

## Proposed Methodology
1. Unsupervised Learning (Clustering)
- Create meaningful groupings of individuals using personality based features
- Apply and compare clustering techniques such as:
- K-means clustering
- Hierarchical clustering
- DBSCAN

2. Constrained Optimization
- Develop a grouping algorithm that enforces fixed group sizes and a balance between similarity and diversity

For our project, we propose a pipeline for building groups with diverse personalities using Big 5 Personality Trait scores. We will use these personality scores to perform a clustering algorithm such as K-means to group students with similar personality profiles. The number of clusters will be determined based on the desired group size and validated by evaluation methods such as the elbow method. Each cluster represents a group of individuals with similar personality profiles, according to the OCEAN test.

Finally, we construct teams by selecting one member from each different cluster. This method forms groups with a mix of personality types to create efficient teams with diverse personalities, supported by (Gómez-Zará et al., 2022). In the end, we will compare this clustering-based group strategy with other baseline methods to evaluate effectiveness.

## Evaluation Metrics
Since we assume clustering methods, we will first assume elliptical groupings and evaluate inertia when using the K-means algorithm. However, for a more thorough evaluation of our grouping pipeline which looks at psychological attributes, we can evaluate each cluster’s average ranking and variance for OCEAN attributes. This will be used to ensure a consistent match with a specific personality type, such as "spontaneity" or “self-discipline” and “reliability,” with respect to a low or high conscientiousness rating.

Other metrics that we are able to evaluate using cluster variances are silhouette scores or the Davies-Bouldin Index to analyze distance of points within a cluster. 

For all metrics used, interpretation of scores and its respective personality trait based on the value’s closeness to either end of the scale is imperative to designing optimal groups in a class-setting.

Prior to our final evaluation of our model, we will also split our data into a testing and training set to holistically evaluate our model. Finally, based on our final group assignments, we will analyze the personality assignments for each “student” in our groupings versus a randomized group to analyze the diversity of students. This allows us to determine the validity and usefulness of our model assigning group projects over a randomized grouping.

## Works Cited
Di Cursi, F., et al. (2025). Mind reading or misreading? LLMs on the Big Five personality test. arXiv. https://arxiv.org/abs/2511.23101

Dwivedy, D., Tamrakar, G., & Mathur, N. (2025). Team collaboration influence of personality traits among marine biologists. TPM, 32(S3), 806–807.

Gómez-Zará, D., Das, A., Pawlow, B., & Contractor, N. (2022). In search of diverse and connected teams: A computational approach to assemble diverse teams based on members’ social networks. PLOS ONE, 17(11), e0276061. https://doi.org/10.1371/journal.pone.0276061

Lin, Q., et al. (2024). The personality of the intelligent cockpit? Exploring the personality traits of in-vehicle LLMs with psychometrics. Information, 15(11), 679. https://www.mdpi.com/2078-2489/15/11/679

Sorokovikova, A., et al. (2024). LLMs simulate Big Five personality traits: Further evidence. In Proceedings of the 1st Workshop on Personalization of Generative AI Systems (PERSONALIZE 2024). Association for Computational Linguistics. https://aclanthology.org/2024.personalize-1.7/
