# %% [markdown]
# # Exploring the North Atlantic Oscillation
# 
# The North Atlantic Oscillation (NAO) is one of the most important climate patterns in the North Atlantic region.
# In the North Atlantic we can observe two main patterns of sea level pressure:
# A high pressure system close to the Azores and a low pressure system near Iceland.
# The NAO-index measures how strong the difference between these two pressure systems is.
# 
# There is no single definition of the NAO-index but two main approaches exist:
# 1. **Station-based approach:** Uses the difference in sea level pressure between specific locations (e.g., Azores and Iceland).
# 2. **Empirical Orthogonal Function (EOF) approach:** Uses statistical methods to identify the dominant pattern of variability in the North Atlantic region.
# We will explore both approaches here.

# %% [markdown]
# # Modules
# %% 
import xarray as xr
import earthkit.plots as ekp
import earthkit.data as ekd
import earthkit.transforms as ekt

# %% [markdown]
# # Loading Mean Sea Level Pressure for the North Atlantic Region
# 
# We base our analysis on the ERA5 mean sea level pressure (MSLP) data.
# I downloaded the data with 6H timesteps between 2015 and 2025. 
# This dataset is quite large: ~31 GB in total. 
# Hence we load it into chunks, which gives us the possibility for parallell computing.
# No worries, xarray and dask will do that for us automatically.

# %%
# Load MSLP data and select North Atlantic region
north_atlantic_box = [-80, 0, 0, 80]  # earthkit expects: [lon_min, lon_max, lat_min, lat_max]
mslp = xr.open_mfdataset("C:/local_desktop/projects/website-coding/data/raw/ERA5/mslp/*.nc")
north_atlantic_mslp = mslp["msl"].sel(
    longitude=slice(north_atlantic_box[0], north_atlantic_box[1]),
    latitude=slice(north_atlantic_box[3], north_atlantic_box[2])
)
north_atlantic_mslp
# %% 
# Compute mean over the reference period
climatology = north_atlantic_mslp.mean(dim="valid_time").compute()
chart = ekp.Map(domain=north_atlantic_box)
chart.contourf(climatology, units="hPa", cmap="seismic")
chart.coastlines()
chart.gridlines()
chart.title("Mean of North Atlantic MSLP (Reference Period: 2015-2025)")
chart.legend(label="{variable_name} ({units})")
chart.show()