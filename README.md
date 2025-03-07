# Readme

## About

This tutorial is an outline of how to interact with the EDITO STAC, and utilize the ARCO data products.  This tutorial presents some of the more fundamental concepts and methods for being able to find the ARCO datasets in a STAC catalog, take a subset of data of interest, and perform some basic visual analysis.  

## Content
Retrieve-CMEMS-dataset.ipynb: Retrieve a dataset from CMEMs using pystac_client, and subset a zarr dataset. 

search_biooracle_stac_zarr_assets.py: Connects to a static json STAC and gets ARCO datasets (assets).

search_edito_stac_zarr_assets.ipynb: Search a STAC conformant API for ARCO datasets (assets).

subsetting_arco_data.ipynb:  Open the CSV file containing the URLs of the ARCO assets.  Open a few ARCO datasets and interactively subset the dataset based on the variables, dimensions, and time range of interest.  Then plot the subsetted rasters to do basic visual analysis.

## Deployment
The notebook is deployed on [Edito Datalab](https://datalab.dive.edito.eu/) as a tutorial. 

# License

CC-BY-4.0

