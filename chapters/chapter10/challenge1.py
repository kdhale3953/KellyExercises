mport arcpy

mxd = arcpy.mapping.MapDocument("P:/Python/Book_exer/Data/Exercise10/Austin_TX.mxd")

for df in arcpy.mapping.MapDocument (mapdoc):
	print "Data Frame" + df.name + "Contains the following layers:"
	lyrlist = arcpy.mapping.ListLayers (mapdoc, "", df)
	for lyr in lyrList:
		print lyr.name


df = arcpy.mapping.ListDataFrames(mxd, "New Data Frame")[1:]
addLayer = arcpy.mapping.Layer("P:/Python/Book_exer/Data/Exercise10/Austin/parks.shp")
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")

del mxd, addLayer


