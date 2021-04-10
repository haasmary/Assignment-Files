__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'
import os
import glob
import zipfile


def clean_cache():
    newfolder = 'cache'
    if not os.path.exists(newfolder):
        os.makedirs(newfolder)
    if os.path.exists(newfolder):
        cachefiles = glob.glob('cache/*')
        for i in cachefiles:
            os.remove(i)


def cache_zip(zipfile_path, cachedir):
    if not os.path.exists(cachedir):
        os.makedirs(cachedir)
    if os.path.exists(cachedir):
        cachefiles = glob.glob(cachedir+'/*')
        for i in cachefiles:
            if os.path.isfile(i):
                os.remove(i)
    
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        x = zip_ref.namelist()
        zip_ref.extractall(cachedir)


def cached_files(x ='/home/potat/files/cache/'):
    list_of_cached_files = os.listdir(x)
    return [x+filename for filename in list_of_cached_files]


def find_password(x):
    keyword = 'password'
    for item in x:
        with open(item, "r") as f:
            read_files = f.readline()
            
            while read_files != '':
                if keyword in read_files:
                    split_line = read_files.split(" ")[1].rstrip()
                    return(split_line)
                read_files = f.readline()


def main(zipfile_path, cachedir="./cache/"):
    clean_cache()
    cache_zip(zipfile_path, cachedir)
    list_of_files = cached_files(cachedir)
    print(find_password(list_of_files))
    

if __name__ == "__main__":
    main("data.zip", cachedir="./cache/")
    
