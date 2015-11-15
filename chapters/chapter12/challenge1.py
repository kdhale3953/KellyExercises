
import arcpy
arcpy.env.workspace = "P:/Python/Book_exer/Data/Exercise12"
fields = arcpy.Listfields("Streets.shp")
print fields


fields = arcpy.ListFields()
namelist = []
for field in fields:
    namelist.append(field.name)
print namelist


def count_string_fields():
    fieldtype = "String"
        return fieldtype
	    count = 0
	        return fieldtype.count

