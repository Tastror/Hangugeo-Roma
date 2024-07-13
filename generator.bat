rd /s /q "dist/"
call conda activate
pyinstaller -F -w hangugeo-UI.py -n hangugeo-roma.exe
cp hangugeo.json dist/