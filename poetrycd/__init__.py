import sys
import os
import subprocess

def poetrycd():
    for filename in sys.argv[1:]:
        dirname = os.path.dirname(filename)
        print(filename, dirname)
        subprocess.run(["poetry", "run", "sync-requirements"], cwd=dirname, check=True, env=os.environ)
