"""This script creates an envelope polygon feature class for the Hawaii.shp feature class"""


import arcpy
from arcpy import env

#set env settings
env.workspace = "P:/Python/Book_exer/Data/Exercise08"

#set local variables
inFeatures = "Hawaii.shp"
outFeatureClass = "P:/Python/Book_exer/Data/Exercise08/Results"

#Execute FeatureEnvelopeToPolygon

arcpy.FeatureEnvelopetoPolygon_management(inFeatures, outFeatureClass, "SINGLEPART"

