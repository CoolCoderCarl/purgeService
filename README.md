# purge service for removing files from dir recursively
# control possible by settings.ini

python3.7 -m PyInstaller --workpath /tmp/build --specpath /tmp -F purgeService.py