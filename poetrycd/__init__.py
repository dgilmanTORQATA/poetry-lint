import sys
import os

def poetrycd():
    for filename in sys.argv[1:]:
        dirname = os.path.dirname(filename)
        os.chdir(dirname)
        os.system("poetry run sync-requirements")
