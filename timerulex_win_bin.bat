::pyi-makespec  --onefile --windowed --noupx --icon=.\folder-remote.ico --hidden-import=PySide timerulex.py
::pyinstaller timerulex.spec
python setup.py py2exe
