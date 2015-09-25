"""The code to add the xy features on the hospital.shp in stand alone mode """


# Import system modules
import arcinfo
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "P://Python/Book_exer/Data/Exercise05/Results"

# Set local variables
inCover = "hospitals"
featureType = "POINT"

#Execute AddXY
arcpy.AddXY_arc(inCover, featureType)

