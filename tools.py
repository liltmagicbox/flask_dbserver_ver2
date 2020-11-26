from os import listdir, mkdir, rename
from os.path import isdir, join, splitext

from randname import barrand6

for f in listdir( noDir ):
          if isdir(f):
              continue
          name,ext = splitext(f)
          if ext.lower() =='.txt':
              txtfiles.append(f)
