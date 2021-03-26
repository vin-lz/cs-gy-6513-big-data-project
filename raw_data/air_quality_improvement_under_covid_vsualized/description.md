# Source
ncydexter/Air-Quality-Improvement-under-COVID-Visualized

# URL
https://github.com/ncydexter/Air-Quality-Improvement-under-COVID-Visualized

# Data Range
| Filename | Range |
| ----------- | ----------- |
**TODO**



**Cleaning**
1. delete rows where more than 3 columns are missing

2. pad 0 for all blank cells of SO2

3. in Beijing dataset, I want to use Mean substitution to fill in missing value of pm25, pm10, but I don't know how to calculate three day moving average with OpenRefine...

4. in Shanghai dataset, missing 99 o3 values, haven't decided how to handle - pad zero or mean substitution

5. in London dataset, from 2014/10/22 - 2014/11/24, missing o3 and no2, haven't decided how to handle