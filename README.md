# Diversity Impact on Movie Success

## Abstract

The world is diverse, and so should cinema be to accurately represent us. Unfortunately, we still see problems arise when a more diverse cast is chosen. For example, when Halle Bailey, a black actress, was chosen as the Little Mermaid, word of boycotting emerged. Has this choice influenced the success of the movie, or is it just a loud minority? Our study delves into the influence of diversity on the success of films. By focusing on a wide range of movies from different genres, timestamps, and cultural backgrounds, we aim to provide insight into the correlation between cast diversity and movie success. The motivation behind our project is to reveal, perhaps, or predict whether a future movie will be successful based on the heterogeneity of its cast. This information can be useful for movie directors who are contemplating adding diverse crew members to their teams.

## Research Questions
In this research, we plan to address the following questions:
- To what extent does ethnicity (or gender) diversity in lead roles impact box office revenue?
- Does increased ethnic representation contribute to higher audience ratings?
- Do certain movie genres benefit more from specific types of diversity?
- Can we compute a “success” score based on different movie indicators?

## A Note on Ethical Risk
Our study is purely based on our curiosity to see whether having a diverse cast improves the overall movie experience for users; does it give the audience a more exciting and engaging experience?

However, although it is not our intention, we are aware that this analysis can be viewed as an ethical risk. For instance, we could end up with conclusions that may harm certain populations. Because of this, we have implemented a solution to group ethnicities into larger ethnic groups. This way, we cannot infer any conclusions about a specific population since they would be part of a much larger group.

Finally, we cannot stress enough that this project is in the scope of a data analysis course and is thus for academic purposes. Any potentially harmful result should be investigated significantly more closely and thoroughly in order to draw a meaningful conclusion.

## Proposed Additional Datasets
Since the CMU movie database contains limited amounts of information, we propose to expand our data using the full MovieLens Dataset found on Kaggle ([link](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)). This 239 MB dataset contains metadata on a collection of 45000 movies and, as such, contains relevant data for our task. In particular, these include:
- Budget
- Box office revenue
- Movie runtime
- Vote average (the equivalent of user rating)

This dataset is not only useful for adding additional columns to our dataset (such as Budget or Vote average) but also helps in filling in missing information in existing columns (such as Box office revenue or Movie runtime). Adding the Kaggle dataset into our original dataset is relatively straightforward as we simply merge it according to the movie name and its release date.

## Methods
In order to address our questions, our initial areas of research are listed in the following:

### Step 1: Preprocessing of the Data
- CMU Movie Metadata
  - Changing the formatting of columns with dictionaries to lists
  - Changing “Movie release date” columns to datetime type and creating a new column with the extracted year
  - Remove movies released in 2013 as the data is incomplete for that year
  - Remove duplicated movies while conserving all the information
- Character Data
  - Remove actors whose ethnicity or gender is not specified
  - Remove actors from movies where their age is negative
  - Remove columns that aren’t of interest such as “Freebase Movie ID”

### Step 2: Ethnicity Exploration
- Extract the ethnicity Freebase IDs and get the name of each ethnicity
- Group ethnicities according to the UK’s list of ethnic groups

### Step 3: Feasibility analysis and first approaches to analysis
- Look at the size of the data after pre-processing
- Visualize the ethnic distributions both by considering unique actors and by the number of apparitions of each ethnicity (i.e. one actor is counted multiple times if they play in multiple movies)
- Visualize the distribution over time
- For each ethnic group visualize gender differences and the proportion of unnamed roles
- Visualize revenues under different considerations and perform first correlation and t-tests

### Step 4: Plot Summary Analysis
- Extract the main roles using the apparition of the names in the plot
- Analyze this under the light of ethnic and gender diversity
- Get the proportion of minor roles and perform similar analyses

### Step 5: Analyze Ratings and Revenues
- Match movies using propensity scores once for ratings and once for revenues
- Do statistical and causality analysis

### Step 6: Create a “success score”
- Once (non-)causality is established we can delve into the creation of a success score
- Decide on weights given ethnic gender variety, especially in leading roles

### Step 7: Create the Data Story webpage
- Develop a cohesive and accessible Data Story webpage to communicate project findings.

## Proposed Timeline
The general idea is to finish all our analyses and plots at least one week before the Milestone 3 deadline. This will be our main priority. We also plan to create a webpage to present our story and results. However, due to Homework 2 coming up, there might be limited progress in the project because most of the time will be invested in the Homework. Nevertheless, from December 1st onwards (or earlier if we finish the homework in advance) we will all work actively on the project.

- **up to 17.11.2023:** Steps 1 to 3
- **17.11.2023-01.12.2023:** Pause (Homework 2)
- **01.12.2023-08.12.2023:** Steps 4 and 5
- **08.12.2023-15.12.2023:** Step 6 and making sure the analyses are all well done
- **15.12.2023-22.12.2023:** Step 7 and final revision of all the previous steps

## Organization within the team
Our team, composed of Ali, Romain, Océane, Diana, and Clement, is collectively engaged in a comprehensive exploration of the correlation between diversity and the success of films. Romain is leading the charge on data collection and preprocessing, ensuring the seamless integration of information from the CMU Movie Metadata and Kaggle MovieLens Dataset. Océane's focus lies in ethnicity exploration, categorizing Freebase IDs based on the UK's ethnic groups. Diana is conducting a thorough feasibility analysis, delving into data sizes, distributions, and initial correlations. Clement is dedicated to plot summary analysis, extracting main roles, and examining diversity within them. Ali and Romain are collaborating on the analysis of ratings and revenues, exploring potential correlations and causality. Océane and Diana are jointly crafting a success score, meticulously assigning weights to ethnic and gender diversity factors. The entire team is actively contributing to the development of a comprehensive data story webpage to present our findings. The timeline is strategically planned, allowing for synchronized progress and periodic pauses to accommodate individual tasks and ensure a cohesive project outcome.
