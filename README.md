# CS-GY 6513 Big Data Project

## Project Participants:

### Group 10
- Vin Liu
- Lillian Zhang
- Hang Zhang

## Project Description

We began with the question, “How has COVID-19 impacted our life?”. After looking at several potential areas, including but not limited to remote learning, economy, stock market, traffic, and urban migration, we settled on exploring the change of air quality correlated with the COVID-19 pandemics in major cities around the world. We intend to obtain a variety of data, including Air Quality Index, CO, NO2, PM2.5, PM10, and Ozone to measure air quality. We analyze the data and map them to major events during the COVID-19 pandemics, such as major lockdowns and curfews in the cities. Through data gathering, processing, and analysis, we might be able to answer the following questions:

- Is there a significant change in the air quality since the COVID-19 onset?
- Did air quality get better or worse during the pandemic across major cities in the world? What’s the possible reason behind such change? 
- Does the air quality change in a similar pattern among cities around the world? 
- Which areas exhibited a significant reduction of certain pollutants during the lockdowns?
- Were there other factors that influenced air quality during the time periods studied?


## Approach Overview

This project is divided into three stages:

- Data Hunting
    - Background knowledge for shaping the questions
    - Air quality data from reliable sources
    - Policy data from reliable sources
- Data Cleaning & Integration
    - Examine the quality and availability of datasets
    - Extract and clean data for selected cities
- Data Analysis & Visualization
    - Create visualizations to support and illustrate the results
    - Analyze the data to answer the questions

## Cleaning and Integration

Before the analysis stage, we performed a series of data cleaning steps using [OpenRefine](https://openrefine.org/). The details are documented in the Project Report. The resulting data are in the `primitive_cleaned_data` directory. 

During the analysis, we did further data wrangling to assist our analysis in [Deepnote](https://deepnote.com/). The details are documented in the Project Report, and the codes are inside .ipynb notebooks for quick reproduction. The resulting data are split into city datasets and located in `city_cleaned_data` directory.

## Visualization and Analysis

We created heatmaps, treemaps and bar charts for each selected city to explore the datasets. They are put into individual `${city}_visual_generated` directories. The detailed analysis is in the Project Report.

## Deliverables

The Project Report can be found in the `deliverables` directory.

## How to Reproduce

All the steps done in OpenRefine and Deepnote are documented in the Project Report. To run the python code, please access the following `.ipynb` files in Deepnote:
- For data cleaning: [https://deepnote.com/project/Big-Data-Project-Group10-c7oq5BK8RFShmz6Y2ShH8w/%2Fdata_cleaning_code.ipynb](https://deepnote.com/project/Big-Data-Project-Group10-c7oq5BK8RFShmz6Y2ShH8w/%2Fdata_cleaning_code.ipynb)
- For data visualization: [https://deepnote.com/project/Big-Data-Project-Group10-c7oq5BK8RFShmz6Y2ShH8w/%2Fdata_visualization_code.ipynb](https://deepnote.com/project/Big-Data-Project-Group10-c7oq5BK8RFShmz6Y2ShH8w/%2Fdata_visualization_code.ipynb)

The `.ipynb` notebooks rely on `python 3.7`, `numpy 1.19.5`, `pandas 1.2.4`, `seaborn 0.11.1`, `matplotlib 3.4.1` and `squarify 0.4.3`.

## Datasets Used
Air Quality Open Data PlatformWorldwide COVID-19 dataset: [https://aqicn.org/data-platform/covid19/](https://aqicn.org/data-platform/covid19/)

EPA Outdoor Air Quality Data: [https://www.epa.gov/outdoor-air-quality-data/downloaddaily-data](https://www.epa.gov/outdoor-air-quality-data/downloaddaily-data)

China Air Quality Historical Data: [https://quotsoft.net/air/](https://quotsoft.net/air/)

Air Quality Improvement under COVID Visualized: [https://github.com/ncydexter/AirQuality-Improvement-under-COVID-Visualized](https://github.com/ncydexter/AirQuality-Improvement-under-COVID-Visualized)

Qualità dell’aria: [https://www.epidata.it/Italia/AQI.html](https://www.epidata.it/Italia/AQI.html)

Oxford Covid Policy Tracker / USA Covid Policy: [https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/OxCGRT_latest_withnotes.csv](https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/OxCGRT_latest_withnotes.csv)