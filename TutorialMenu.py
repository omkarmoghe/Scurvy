from Globals import *
import os
import subprocess
import sys


def show_tutorial():
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', os.getcwd() + tutorial_movie_file_name))
    elif os.name == 'nt':
        os.startfile(os.getcwd() + tutorial_movie_file_name)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', os.getcwd() + tutorial_movie_file_name))
    else:
        print "The operating system type " + os.name + " that you are using is not supported to display videos."
        assert(False)