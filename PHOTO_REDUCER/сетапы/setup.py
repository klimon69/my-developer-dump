

from cx_Freeze import setup, Executable
import sys
import os


base = None

if sys.platform == 'win32':
    base = "Win32GUI"


executables = [Executable("photo_reduser_and_crop.py", base=base)]

packages = ["tkinter"]
options = {
    'build_exe': {
        'includes': ["os", "tkinter", "PIL"],
        'include_files': ["tcl86t.dll", "tk86t.dll"]
    },

}

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35\tcl\tk8.6'

setup(
    name="RESIZE_AND_CROP",
    version="1.0",
    description="Test",
    options=options,
    executables=executables
)