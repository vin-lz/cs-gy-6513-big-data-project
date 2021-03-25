# Source
ncydexter/Air-Quality-Improvement-under-COVID-Visualized

# URL
https://github.com/ncydexter/Air-Quality-Improvement-under-COVID-Visualized

# Data Range
| Filename | Range |
| ----------- | ----------- |
**TODO**



**Cleaning**
1. At first I want to delete rows where more than 3 columns are missing, then I realized that date is the primary key of this dataset. In order to maintain temporal data's continuity and integrity, I shall keep all rows, however handle the missing columns. for example on 2020/9/2, among all 6 columns, we only have data of pm2.5. 

2. pad 0 for all blank cells of SO2

3. I want to use Mean substitution to fill in missing value of pm25, pm10, but I don't know how to calculate three day mean with OpenRefine...

