# EDITO Python tutorials 

## About
This project is part of EDITO-INFRA ([Grant agreement ID: 101101473](https://doi.org/10.3030/101101473))
- Task 6.2 Open tools

Authors
- Willem Boone | contact: [willem.boone@vliz.be](willem.boone@vliz.be)
- Samuel Fooks | contact: [samuel.fooks@vliz.be](samuel.fooks@vliz.be)

## Tutorials
These tutorials are an outline of how to interact with the EDITO STAC, and utilize the Analysis-ready and cloud-optimized (ARCO) data products. The tutorials presents some of the more fundamental concepts and methods for being able to find the ARCO datasets in a STAC catalog, take a subset of data of interest, and perform some basic visual analysis. 

### 0. STAC browser
The STAC browser is a useful GUI tool that allows users to visualy search the STAC catalog. Watch the demo video below to learn more.<br>
[![Watch the video](https://img.youtube.com/vi/ZJHcB2fwkIQ/0.jpg)](https://www.youtube.com/watch?v=ZJHcB2fwkIQ)

### 1. Retrieve-CMEMS-dataset.ipynb
Find a dataset from CMEMs using pystac_client. The dataset is offered as ZARR. The ZARR will be sliced and plotted. 
- [Notebook](https://github.com/willem0boone/Edito_python_STAC/blob/main/Retrieve-CMEMS-dataset.ipynb)

[![Watch the video](https://img.youtube.com/vi/vT4fBrzsFPk/0.jpg)](https://www.youtube.com/watch?v=vT4fBrzsFPk)

### 2. Retrieve-eurobis-dataset.ipynb
Find occurrence data from eurobis. The dataset is offered as parquet. The parquet is sliced and plotted.
- [Notebook](https://github.com/willem0boone/Edito_python_STAC/blob/main/Retrieve-eurobis-dataset.ipynb)

### 3. search_biooracle_stac_zarr_assets.py
Connects to a static json STAC and gets ARCO datasets (assets).

### 4. search_edito_stac_zarr_assets.ipynb
Search a STAC conformant API for ARCO datasets (assets).

### 5. subsetting_arco_data.ipynb
Open the CSV file containing the URLs of the ARCO assets.  Open a few ARCO datasets and interactively subset the dataset based on the variables, dimensions, and time range of interest.  Then plot the subsetted rasters to do basic visual analysis.

## Deployment
The notebook is deployed on [Edito Datalab](https://datalab.dive.edito.eu/) as a tutorial. 

