
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from ast import Return
from importlib.resources import path


def clean_cache():
    import os
    if os.path.isdir('files\\cache'):
        for file in os.scandir('cache'):
            os.remove(file.path)
    else:
        os.mkdir('files\\cache')
    return


def cache_zip(zip_file_path, cache_dir_path):
    import zipfile
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
        return zip_ref


def cached_files():
    import os
    list = []
    path = os.scandir(os.path.abspath('cache'))
    for entry in path:
        list.append(entry.path)
    return list


def find_password(list):
    for file_name in list:
        with open(file_name, 'r') as f:
            contents = f.readlines()
            for line in contents:
                if 'password' in line:
                    return line.strip()[10:]


clean_cache()
cached_files()
Zippath = 'D:\\Winc\\Backend Development\\files\\data.zip'
Cachepath = 'cache'
cache_zip(Zippath, Cachepath)
find_password(cached_files())
