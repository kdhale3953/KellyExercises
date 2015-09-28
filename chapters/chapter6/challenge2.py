"""This code reads all the feature classes and in a geodatabase copies only the polygon features to a new file geodatabase"""


import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P://Python/Book_exer/Data/Exercise06"
arcpy.CreateFileGDB_management("C:/EsriPress/Python/Data/Exercise06/
Results", "MY.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
fcdesc = arcpy.Describe(fc)
    if:
        fc in fclist == "Polygon"
	copy to MY.gdb
    


arcpy.CopyFeatures_management(fc, "C:/EsriPress/Python/Data/
Exercise06/Results/MY.gdb/" + fcdesc.basename)


