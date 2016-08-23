from distutils.core import setup
import py2exe
from timerulex.main import __version__ as VERSION




PACKAGE = "timerulex"
NAME = "timerulex"
DESCRIPTION = "timerulex - time rules gui, based on PySide writed on Python."
LONG_DESCRIPTION = '''timerulex - time rules gui, based on PySide writed on Python. Licensed by GPL3.'''
AUTHOR = "1_0"
AUTHOR_EMAIL = "1_0@usa.com"
URL = r"https://github.com/1-0/timerulex"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords='pyside',
    license="GPL3",
    url=r'https://github.com/1-0/timerulex',
    install_requires = ['PySide', ],
#    scripts = [r'timerulex.py',],
    py_modules=['pyside',],
#    namespace_packages=['timerulex',],
    packages=['timerulex',],
    #packages=[PACKAGE,],
    #packages=find_packages(exclude=["tests.*", "tests"]),
    #package_data=find_package_data(
#           PACKAGE,
#           only_in_packages=False
#     ),
    #extras_require={
    #"PySide": ['PySide>=1.0'],
#},
    #entry_points={
        #'console_scripts': [
            #'ftpservx = timerulex.py:_main',
        #],
#},
    #~ entry_points={
        #~ 'console_scripts': [
            #~ 'timerulex = timerulex.main:main'
        #~ ]
        #~ },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Developers",
        'Intended Audience :: End Users/Desktop',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
#~ )

#~ setup(
    options = {
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
        }
    },
    windows=['timerulex.py'])
