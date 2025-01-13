import pystac
import xarray as xr
import pandas as pd
from datetime import datetime, date
from pystac_client import Client
from matplotlib import pyplot as plt
import numpy as np
import cartopy.crs as ccrs
# STAC API root URL
URL = 'https://s3.waw3-1.cloudferro.com/emodnet/bio_oracle/stac/catalog.json'

# custom headers
headers = []

# Open the STAC catalog root
cat = Client.open(URL, headers=headers)
print(cat)

# Get all collections
collections = list(cat.get_all_collections())
print(f'Found {len(collections)} collections')

# Search for collections with chlorophyll in the ID, these will be the collections with the data we are interested in
for collection in collections:
    if 'chl' in collection.id:
        print(collection.id)
        for item in collection.get_all_items():
            print(item.id)
            print(item.assets)
            break

# Get all items and assets from the collections, specifically looking for zarr assets
all_items_assets = []
for collection in collections:
    if 'chl' in collection.id:
        for item in collection.get_items():
            assets_list = []
            for asset_key, asset in item.assets.items():
                if asset.href.endswith('.zarr') or asset.href.endswith('.zarr/') or asset.href.endswith('.parquet'):
                    # Append asset information to the list
                    assets_list.append({'Collection ID': collection.id, 'Item ID': item.id, 'start_datetime': item.properties['start_datetime'], 'end_datetime': item.properties['end_datetime'], 'Asset Key': asset_key, 'Asset Href': asset.href})
            
            # Append item information to the list
            all_items_assets.extend(assets_list)

# Create a pandas dataframe from the list
df = pd.DataFrame(all_items_assets)
print(df.head())

# Function to subset a zarr asset, and plot the data
# you will be prompted to select the dimension index and variable to plot
def subset_zarr_asset(asset_href):
    ds = xr.open_dataset(asset_href, engine='zarr')
    selections = {}

    # look at the dimensions in the dataset
    for dim in ds.dims:
        dim_extent = ds[dim].values[0], ds[dim].values[-1]
        dim_index_range = [0, len(ds[dim]) - 1]
        print(f" 0 {dim_extent} {dim_index_range}")

        if 'lat' in dim or 'lon' in dim:
            # Ask if the user wants to select by lat/lon
            select_lat_lon = input(f"Do you want to select a range for {dim}? (yes/no): ").strip().lower()
            if select_lat_lon == 'yes':
                # For lat and lon, ask for a range
                selected_range = input(f"Select range for {dim} from {dim_extent} (e.g., min,max): ")
                min_val, max_val = map(float, selected_range.split(','))
                selections[dim] = slice(min_val, max_val)
            else:
                selections[dim] = slice(None)  # Select all values
        else:
            # For other dimensions, ask for a single index
            selected_index = input(f"Select dim index for {dim} from {dim_extent}: ")
            selections[dim] = ds[dim].values[int(selected_index)]

    # look at the variables in the dataset
    for var in ds.data_vars:
        varindex = 0
        print(f"{varindex} {ds[var]}")
        varindex += 1
    
    # select the variable to plot
    selected_var = input("Select variable: ")
    if selected_var in ds.data_vars:
        print(ds[selected_var].sel(selections))
        print('plotting')
        fig, ax = plt.subplots()
        ax = plt.axes(projection=ccrs.PlateCarree())
        ds[selected_var].sel(selections).plot(ax=ax)
        ax.coastlines()

        # Set labels and format ticks
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        gl = ax.gridlines(draw_labels=True)
        gl.top_labels = False
        gl.right_labels = False
        plt.show(block=True)

# select STAC items with start_datetime > 2010, and subset the zarr asset
for index, row in df.iterrows():
    if pd.to_datetime(row['start_datetime']).year > 2010:
        print(row['Asset Href'])
        subset_zarr_asset(row['Asset Href'])
        break

