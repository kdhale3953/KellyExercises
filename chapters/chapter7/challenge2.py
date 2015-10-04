mport arcpy
from ar
>>> from arcpy import env
>>> env.workspace = "P:/Python/Book_exer/ex7/results"
>>> fc = "Results/roads/Ferry"
>>> cursor = arcpy.da.InsertCursor(fc, "NAME")

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
      cursor = arcpy.da.InsertCursor(fc, "NAME")
      RuntimeError: cannot open 'Results/roads/Ferry'
      >>> cursor.insertRow(["New", FERRY])

      Traceback (most recent call last):
        File "<pyshell#5>", line 1, in <module>
	    cursor.insertRow(["New", FERRY])
	    NameError: name 'cursor' is not defined
	    >>> cursor = arcpy.da.InsertCursor (fc,"NAME")

	    Traceback (most recent call last):
	      File "<pyshell#6>", line 1, in <module>
	          cursor = arcpy.da.InsertCursor (fc,"NAME")
		  RuntimeError: cannot open 'Results/roads/Ferry'
		  >>> 
		  [DEBUG ON]
		  >>> 
		  [DEBUG OFF]
		  >>> ================================ RESTART ================================
		  >>> import arcpy
		  from arcpy import env
		  env.workspace = "P:/Python?Book_exer/ex7"
		  fc = "Road.shp"
		  cursor = arcpy.da.InsertCursor(fc, "NAME")
		  cursor.insertRow(["FERRY"])
		  del cursor
		  >>> 


