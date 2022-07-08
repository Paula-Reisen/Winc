
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os
import zipfile

def clean_cache():
    JoinedPath = os.path.join(os.getcwd(), "files", "cache")
    if os.path.isdir(JoinedPath):
        for file in os.scandir(JoinedPath):
            os.remove(file.path)
    else:
        os.mkdir(os.path.join(os.getcwd(), "files", "cache"))
    return


def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)
        return zip_ref


def cached_files():
    list = []
    path = os.scandir(os.path.abspath())
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


if __name__ == "__main__":
    pass
    # Zippath = 'D:\\Winc\\Backend Development\\files'
    # Cachepath = 'cache'
    # cache_zip(Zippath + '\\data.zip', Cachepath)
    # find_password(cached_files())