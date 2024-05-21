# carbon_nbs
This is the repository containing the main codes developed so far regarding the Carbon-Nature Based Solutions field. Inside, there are two scripts (Python):
1. Satlas Super Resolution pre-trained Nerual Network code based to improve the spatial resolution of Sentinel-2 images (only for RGB channels) from their native spatial resoluion (10 meters) to 1 meter. The Neural Network was trained on NAIP images, and it was used the ESRGAN model that is an adaptation of the original ESRGAN, with changes that allow the input to be a time series of Sentinel-2 images. The ESRGAN network is saved on an external file, that cannot be uploaded on GITHUB because off the file size, to download it will be shared a google drive folder (https://drive.google.com/file/d/1qjaNoomj_5ZRTZdpdT9TflcTVdCwFU-H/view?usp=sharing).
2. AboveGround Biomass estimation from satellite imageries. The prediction is based using Sentinel-1 (SAR), Sentinel-2 (MSI), Elevation, Slope and Canopy Height Model (META) compairing it with GEDI aboveground biomass data. The model used is Random Forest provided by Google Earth Engine.
