import sys
import os
import subprocess

def poetrycd():
    for filename in sys.argv[1:]:
        dirname = os.path.dirname(filename)
        subprocess.run("python -c 'import commands; commands.sync_requirements()'", cwd=dirname, shell=True, check=True, env=os.environ)
