# import os
# import sys
#
# from cx_Freeze import setup, Executable
# from glob import glob
#
# files = glob('src/*')  # No files in ../sql/ root
#
# build_options = {
#     'include_files': list(zip(files, files)),
#     'excludes': ["tkinter", "unittest"]
# }
#
# executables = [
#     Executable('main.py', base='console', target_name='spotify_shuffler')
#
# ]
# setup(name='spotify_shuffler',
#       version='1.0',
#       description='Spotify Shuffler by Lightningtow',
#       options={'build_exe': build_options},
#       executables=executables)
#
# # Dependencies are automatically detected, but it might need
# # fine tuning.
#
# # build_options = {'packages': [],
# #                  'excludes': ["tkinter", "unittest"],
# #                  'include_files': includefiles}
#
# #    PycharmProjects\spotify_shuffler\venv\Scripts\activate.bat
# #    cd PycharmProjects\spotify_shuffler\src
#
# #    python setup.py build
# #    build\exe.win-amd64-3.9\spotify_shuffler.exe
#
