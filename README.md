# Create the Perfect Group Assignments!

## Overview

## Objective
Group work is a critical component of collaborative learning in academic and nonacademic settings alike. In many situations, groups are formed randomly, with little thought put into compatibility. This can lead to mismatches in communication styles, work ethics, and overall interpersonal compatibility. These issues can reduce efficiency and impact learning outcomes. 

The Big 5 Personality Traits are a psychological model that measures personality based on five factors: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. This model has been commonly used to examine individual strengths and weaknesses, which helps people to understand the types of roles that fit their personality traits and the type of people they would want to collaborate with. Through this framework, it can help create more balanced teams, resulting in more efficiency and better productivity. 

Prior research in team based scientific environments demonstrate that personality traits significantly influence collaboration quality, particularly agreeableness and conscientiousness have a large impact on group cohesion and productivity (Dwivedy et al., 2025). Therefore, it is effective to use the Big 5 Personality Traits to create compatible and collaborative teams.

Our goal is to implement a machine learning pipeline that groups individuals into their most optimal and productive team. We will do this by balancing compatibility and diversity of personality traits, rather than clustering the most similar traits together. 


## Data
1. [IPIP300 Kaggle Dataset](https://www.kaggle.com/datasets/edersoncorbari/ipip-neo-big-five-personality-300-item-version)

For our real-world dataset, we chose to use the results of the Big-Five Personality Test, which was compiled for the International Personality Item Pool (IPIP). This inventory of data is used as a means of psychological analysis. The test aims to score each individual’s openness, conscientiousness, extraversion, agreeableness, and neuroticism (OCEAN) on a scale of 1-5 according to their agreement with 300 different statements, also answered on a scale of 1-5. The dataset records 307,313 individuals and their responses to the survey, as well as their final OCEAN attribute ranking.

2. https://huggingface.co/datasets/Fatima0923/Automated-Personality-Prediction 

In addition, for the option of using synthetic and simulated data, we chose to expand upon current literary reviews researching LLM’s ability to predict personality on the Big-Five metrics using input texts. Using this synthetic dataset which predicts the OCEAN personality attributes on a scale of 1-5 based on input text, we can also compare the results of clustering real-world personalities and predicted ones. This specific predictive dataset contains 20,877 rows of text inputs, along with the predicted OCEAN attribute rankings.
