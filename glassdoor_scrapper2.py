import glassdoor_scrapper as gs
import pandas as pd 

path = "D:/Work Space/Projects/Data Science/Glassdoor Project/chromedriver.exe"

df = gs.get_jobs("data scientist",15,False,path,15)
df