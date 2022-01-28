# coding: utf-8
import arcpy
from arcpy.sa import *
baseRaster = Raster('DEM_elkhorn.tif')
falconHabitat = (Slope(baseRaster, 'DEGREE') > 40) & ((baseRaster-baseRaster.mean) > 160)
falconHabitat.save('C:\\PythonScriptsRaster\\Data\\HabitatOutput.tif')