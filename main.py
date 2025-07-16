import classified_directory as cd
import time

# CHANGE YOUR DOWNLOADS DIRECTORY HERE !!
source = r'C:\Users\sustainability\Downloads'
classified_app = cd.ClassifiedDirectories(source)

print('reading downloads directory...'.title())
print('check your important folders and files!'.title())
time.sleep(2)

result = classified_app.read_dir()
folders_deleted = result[0] - len(classified_app.primary_downloads_folders)
files_deleted = result[1]
deleted_things = folders_deleted + files_deleted

if deleted_things:
    print(f"{folders_deleted} folders will be deleted and {files_deleted} files will be moved".title())
    confirmation = input('are you sure (y/n): '.title())
    time.sleep(2)
    if confirmation.lower() == 'y':
        print('the organization of the downloads directory will begin\n'.title())
        while deleted_things:
            deleted_things -= 1
            classified_app.del_dir()
            classified_app.del_file()
            classified_app.move_file()
        else:
            print('\nall folders and files are organized'.title())
    else:
        print('exit script'.title())
else:
    print('the downloads directory is already clean'.title())
print('done'.title())
