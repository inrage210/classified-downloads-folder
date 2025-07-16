from pathlib import Path
import shutil
import time

class ClassifiedDirectories:
    def __init__(self,source):
        self.source = Path(source)
        self.primary_downloads_folders = ['Music','Video','Compressed','Pictures','Programs','Others','Documents']

    # a function to calculate how many folders and files contained inside download directory
    def read_dir(self):
        numb_folders = 0
        numb_files = 0
        for files_folder in self.source.iterdir():
            if files_folder.is_file():
                numb_files += 1
            if files_folder.is_dir():
                numb_folders += 1
        return numb_folders, numb_files
    
    # a function to delete folders if not suitable to primary downloads folders tree
    def del_dir(self):
        for folders in self.source.iterdir():
            if folders.is_dir():
                if folders.name not in self.primary_downloads_folders:
                    shutil.rmtree(folders)
    
    # a function to replace files if existed
    def del_file(self):
        destinations_path = [
        self.source / 'Music',
        self.source / 'Documents',
        self.source / 'Video',
        self.source / 'Compressed',
        self.source / 'Pictures',
        self.source / 'Programs',
        self.source / 'Others']
        file_list = []
        for file in self.source.iterdir():
            if file.is_file():
                file_list.append(file)
        for destination in destinations_path:
            for file in destination.iterdir():
                for item in file_list:
                    if item.name == file.name:
                        file.unlink()

    # a function to move files based on its formatted type file
    def move_file(self):
        music_extensions = [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"]
        program_extensions = [".exe", ".msi", ".bat", ".cmd", ".com", ".scr", ".dll",".app", ".sh", ".bin", ".run", ".so", ".dmg", ".pkg",".py", ".js", ".php", ".rb", ".pl", ".vbs", ".ps1",".apk", ".ipa", ".jar", ".class", ".dex"]
        image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff",".tif", ".psd", ".raw", ".svg", ".ico", ".heic", ".eps",".ai", ".cdr", ".dng", ".ppm"]
        compressed_extensions = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso"]
        video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",".mpeg", ".mpg", ".3gp", ".ogv", ".m4v", ".ts", ".m2ts",".vob", ".divx", ".xvid", ".prores", ".mxf", ".braw", ".dng"]
        documents_extensions = [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls",".xlsx", ".csv", ".ods", ".ppt", ".pptx", ".odp", ".epub",".mobi", ".azw", ".djvu"]

        for file in self.source.iterdir():
            if file.is_file():
                time.sleep(1)
                if file.suffix in music_extensions:
                    shutil.move(file,self.source / 'Music')
                    print(f"Moving {file.name}")
                elif file.suffix in program_extensions:
                    shutil.move(file,self.source / 'Programs')
                    print(f"Moving {file.name}")
                elif file.suffix in image_extensions:
                    shutil.move(file,self.source / 'Pictures')
                    print(f"Moving {file.name}")
                elif file.suffix in compressed_extensions:
                    shutil.move(file,self.source / 'Compressed')
                    print(f"Moving {file.name}")
                elif file.suffix in video_extensions:
                    shutil.move(file,self.source / 'Video')
                    print(f"Moving {file.name}")
                elif file.suffix in documents_extensions:
                    shutil.move(file,self.source / 'Documents')
                    print(f"Moving {file.name}")
                else:
                    shutil.move(file,self.source / 'Others')
                    print(f"Moving {file.name}")