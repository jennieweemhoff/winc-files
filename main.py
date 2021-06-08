__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os 
import shutil

cache = './cache'
zip = 'data.zip'

def clean_cache(): 
    if os.path.exists(cache): 
        for file in os.scandir(cache): 
            os.remove(file.path)
    else: 
        os.makedirs(cache)

def cache_zip(zip_file, cache_dir): 
    shutil.unpack_archive(zip_file, cache_dir)

def cached_files(): 
    files_list = []
    for entry in os.scandir(cache): 
        files_list.append(os.path.abspath(entry))
    return files_list

def find_password(files_list):
    for file in files_list:
        with open(file,'r') as file: 
            file = file.read()
            if 'password' in file: 
                file_lines = file.split('\n')
                for file_line in file_lines:
                    if "password: " in file_line:
                        password = file_line.split(' ')[1]
                return password

if __name__ == '__main__':
    clean_cache()
    cache_zip(zip, cache)
    files = cached_files()
    find_password(files)


