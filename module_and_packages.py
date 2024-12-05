# Module
# A module is a single Python file that contains code (functions, classes, variables, etc.). 
# It is a way to organize related code into one file, making it easier to reuse and manage. 
# Modules are imported into other Python programs using the import statement. 
# A module can be created by saving a Python script with a .py extension. 


import numpy 
import pandas 
import math


# Package
# A package is a collection of Python modules organized in a directory structure.
# A package is essentially a folder that contains multiple module files and a special __init__.py file to mark it as a package (though the __init__.py file is optional in Python 3.3+).
# Packages allow you to organize related modules into subdirectories for better project organization.
# A package can also contain subpackages (nested packages).

from math import sum
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
