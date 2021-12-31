import zipfile
import os


def unzip(file_name):
    # 解压后文件放置的目录
    unzip_dir = r'.'
    # 解压前文件的zip目录
    zip_file2_path = fr'{file_name}'
    unzip_files = zipfile.ZipFile(zip_file2_path, mode='r', compression=zipfile.ZIP_DEFLATED)
    unzip_files.extractall(unzip_dir)
    unzip_files.close()


def walk_file(file):
    file_names = []
    for root, dirs, files in os.walk(file):
        # 遍历文件
        for f in files:
            file_names.append(os.path.join(root, f))
    return file_names


file_nams = walk_file(".")
for file_nam in file_nams:
    if file_nam.split(".")[-1] == "zip":
        unzip(file_nam)
