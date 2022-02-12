# Project Overview : Prediction of Data Science salary
* Created a tool that predicts salaries for the data science field (MAE - $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from Glassdoor using python and selenium scraper
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, Ridge and Random Forest Regressors using GridsearchCV in order to select the best model.
* Built a client facing API using flask

## Code & Resources Used
Python Version: 3.10.2

Packages : pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

For Web Framework Requirements: ```pip install -r requirements.txt```

For scraper github : https://github.com/arapfaik/scraping-glassdoor-selenium

For scraper article : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping 
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning
The next step after scraping data was to clean the data so that we can use it for the model.Made some following changes and also created couple of following variables:
* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for company state
* Added a column for if the job was at the company’s headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
    *  Python
    * R
    * Excel
    * AWS
    * Spark
* Column for simplified job title and Seniority
* Column for description length

## Exploratory Data Analysis *(EDA)*
Examined the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

![alt text](https://github.com/Aakanksha3010/ds_salary_project/blob/main/Heatmap.png "Seaborn correlation Heatmap")

![alt text](https://github.com/Aakanksha3010/ds_salary_project/blob/main/Heatmap-2.png "Seaborn correlation Heatmap_2")

![alt text](https://github.com/Aakanksha3010/ds_salary_project/blob/main/Location.png "Job opportunities by Location")

![alt text](https://github.com/Aakanksha3010/ds_salary_project/blob/main/Sector.png "Job opportunities by Sector")

![alt text](https://github.com/Aakanksha3010/ds_salary_project/blob/main/pivot.png "Salary by position")

![alt text](https://github.com/Aakanksha3010/ds_salary_project/blob/main/word-cloud.png "graphical representation of the frequency of keywords searched")
## Model Building
In this section, first step was to transform the categorical variables inot dummy variables.Also, split the data into train & tests sets with a test_size = 0.2.

Tried 4 different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

Four different models which I tried:
* *Multiple Linear Regressio* – Baseline for the model
* *Lasso Regression* – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
* *Ridge Regression* - Because linear regression wasn't providing expected results so had to regularize the data by shrinking the input coefficients and minimising the cost function using ```L2 regularization```
* *Random Forest Regressor* – Again, with the sparsity associated with the data, I thought that this would be a good fit

## Model Performance
The Random Forest model far outperformed the other approaches on the test and validation sets.
* *Random Forest* : MAE = 11.09
* *Linear Regression*: MAE = 24.07
* *Ridge Regression*: MAE = 18.88
* *Lasoo Regression*: MAE = 19.67

## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
