# Source
ncydexter/Air-Quality-Improvement-under-COVID-Visualized

# URL
https://github.com/ncydexter/Air-Quality-Improvement-under-COVID-Visualized

# Data Range
| Filename | Range |
| ----------- | ----------- |
**TODO**



**Cleaning Decision**
1. for all datasets, delete rows where more than 3 columns are missing

2. for all datasets, pad 0 in blank cells of SO2

3. in Beijing dataset, I want to use Mean substitution to fill in missing value of pm25, pm10, but I don't know how to calculate three day moving average with OpenRefine...

4. in Shanghai dataset, missing 99 o3 values, haven't decided how to handle - pad zero or mean substitution

5. in London dataset, from 2014/10/22 - 2014/11/24, missing o3 and no2, haven't decided how to handle

6. in Paris dataset, miss 1665 cells of so2, miss 662 cells of co, therefore decide to exclude entirely.

7. in Singapore dataset, miss 898 cells of no2, miss 176 cells of co, howerver has 1427 cells of psi, which other city's datasets don't have, therefore decide to exclude entirely.

8. in seoul dataset, about 150 rows of data missing pm2.5, they are mostly from year 2014, therefore I deleted those 150 rows. If you think that could create bias please roll back. 