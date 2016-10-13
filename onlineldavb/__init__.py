#load browser profile function
from .onlineldavb import *
from .corpus import *

this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "data.txt")
