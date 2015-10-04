Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
n 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "P:/Python/Book_exer/ex7"

# Set local variables
inCover = "airports"
outCover = "P:/Python/Book_exer/ex7/airportbuf"
featureType = "LINE"
bufferDistance = 15,000
bufferShape = "ROUND"
bufferSide = "FULL"

# Execute Buffer
arcpy.Buffer_arc(inCover, outCover, featureType, "", "", bufferDistance, "",
                 bufferShape, bufferSide)
		 >>> # Set local variables
		 inCover = "airports"
		 outCover = "P:/Python/Book_exer/ex7/airportbuf"
		 featureType = "Seaplane"
		 bufferDistance = 7500
		 bufferShape = "ROUND"
		 bufferSide = "FULL"

Type "copyright", "credits" or "license()" for more information.
>>> 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "P:/Python/Book_exer/ex7"

# Set local variables
inCover = "airports"
outCover = "P:/Python/Book_exer/ex7/airportbuf"
featureType = "LINE"
bufferDistance = 15,000
bufferShape = "ROUND"
bufferSide = "FULL"

# Execute Buffer
arcpy.Buffer_arc(inCover, outCover, featureType, "", "", bufferDistance, "",
                 bufferShape, bufferSide)
>>> # Set local variables
inCover = "airports"
outCover = "P:/Python/Book_exer/ex7/airportbuf"
featureType = "Seaplane"
bufferDistance = 7500
bufferShape = "ROUND"
bufferSide = "FULL"

