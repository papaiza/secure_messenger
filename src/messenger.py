import sys
import os.path

if sys.argv[1] == '-b':
    if os.path.isfile(sys.argv[2]):
        with open(sys.argv[2]) as f:
            content = f.readlines()

