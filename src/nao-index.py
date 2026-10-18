# %% [markdown]
# # NAO Index Analysis
# 
# Today we will explore the North Atlantic Oscillation and its corresponding index.
# For this analysis, we use mean sea level pressure from the ERA5 dataset.
#

# %% [markdown]
# # Modules
# %% 
import xarray as xr
import earthkit.plots as ekp
import earthkit.data as ekd

# %% [markdown]
# # Loading Mean Sea Level Pressure
# 
# We start by loading the MSLP for the North Atlantic region.

# %%
mslp = xr.open_dataset("path/to/your/mslp/file.nc")