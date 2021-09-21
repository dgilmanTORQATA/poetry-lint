import sys
import os
import subprocess

def poetrycd():
    for filename in sys.argv[1:]:
        dirname = os.path.dirname(filename)
        print(filename, dirname)
        raise Exception()
        subprocess.run("echo pwd; poetry run sync-requirements", cwd=dirname, shell=True, check=True, env=os.environ)
