import os
import datetime

def file_path():
    """check filder in current directory """
    path = "."
    files=os.listdir(path)
    file_dir = []
    for file in files:
        if not file.startswith(".") and os.path.isdir(os.path.join(path,file)):
            file_dir.append(file)
    return file_dir
def filenamechange(file_dir):
    """filename add st_ctime """
    for dir_name in file_dir:
        files = os.listdir(os.path.join(path,dir_name))
        for file in files:
            if not file.startswith(".") and file.find(".") != -1: # secret file or dir
                file_name = file.split(".")[0]
                ext = file.split(".")[1]
                created_time = os.stat(os.path.join(path,dir_name,file)).st_ctime
                date = datetime.datetime.fromtimestamp(created_time)
                date = date.strftime("%Y%m%d")
                if file_name[0:8] != date:  #prevent double write
                    new_file = "{0}_{1}.{2}".format(date, file_name, ext)
                    os.rename(os.path.join(path,dir_name,file),os.path.join(path,dir_name,new_file))

def main():
    file_dir = file_path()
    filenamechange(file_dir)

if __name__ == "__main__":
    main()
