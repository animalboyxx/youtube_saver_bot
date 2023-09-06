import os

for rootdir, dirs, files in os.walk('.'):
    for file in files:
        if (file.split('.')[-1]) == 'mp3':
            print(os.path.join(rootdir, file))
