"""This code runs the dissolve tool on the parks.shp feature class using the PARK_TYPE field as the field for aggregating features. Multi-part features are not allowed"""


# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inCover = "parks"
outCover = "P://Python/Book_exer/Data/Exercise05/Results/Parks_dissolve"
dissolveItem = "PARKS_TYPE"
featureType = "POLY"

# Execute Dissolve
arcpy.Dissolve_arc(inCover, outCover, dissolveItem, featureType)

