__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os 
import glob
import shutil
import io


def clean_cache(): 
    if os.path.exists('c:/Users/Jennie/files/cache'): 
        cache = 'c:/Users/Jennie/files/cache'
        for file in os.scandir(cache): 
            os.remove(file.path)
    else: 
        os.makedirs('C:/Users/Jennie/files/cache')

def cache_zip(zip_file, cache_dir): 
    shutil.unpack_archive(zip_file, cache_dir)

def cached_files(): 
    files_list = []
    for entry in os.scandir(r'C:\Users\Jennie\files\cache'): 
        files_list.append(entry.path)
    return files_list

def find_password(files_list):
    for file in files_list:
        with open(file,'r') as file: 
            file = file.read()
            if 'password' in file: 
                file_lines = file.split('\n')
                password_line = file_lines[5]
                password = password_line.split(' ')[1]
                return password 
                

#zip = 'C:/Users/Jennie/files/data.zip'
#cache = 'C:/Users/Jennie/files/cache'

if __name__ == '__main__':
    #cache_zip(zip, cache)
    #clean_cache()
    files = cached_files()
    find_password(files)