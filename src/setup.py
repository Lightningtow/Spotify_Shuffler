import os
import sys

from cx_Freeze import setup, Executable



# Dependencies are automatically detected, but it might need
# fine tuning.
includefiles = ['playlists.txt']
build_options = {'packages': [], 'excludes': [], 'include_files': includefiles}


executables = [
    Executable('main.py', base='console', target_name='spotify_shuffler')
    # Executable('main.py', base=None, target_name='spotify_shuffler')

]
setup(name='spotify_shuffler',
      version='1.0',
      description='Spotify Shuffler by Lightningtow',
      options={'build_exe': build_options},
      executables=executables)

#    PycharmProjects\spotify_shuffler\venv\Scripts\activate.bat
#    cd PycharmProjects\spotify_shuffler\src

#    python setup.py build
#    build\exe.win-amd64-3.9\spotify_shuffler.exe

