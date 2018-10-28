#Standardization of heatmap.py#

approach of rewriting heatmap.py script to more flexible solution that can take different locationdata.
(heatmap.py was a script I wrote a while back, designed for a single run-through based on my locationdata. The goal of this script is to make it applicable to anyone's locationdata.)

##Approach##
1. show distribution for longitude and latitude, to show fitting interval 
2. inside interquartile (IQR = Q3 - Q1) should do the job
3. filter out any coordinates outside determined interval locationdata.json 
4. determine accuracy raster (100x100, 1000x1000 etc)
5. calculate value per rasterfield
6. determine colors of the rasterfields based on value
7. map the raster
