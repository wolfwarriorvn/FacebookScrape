import glob, os
import subprocess
import os.path, time
import pickle
from typing import List, Dict

BACKUP_FILE = 'backup.pkl'
def run(cmd):
    # completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    completed = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess. STDOUT, shell=True)
    return completed

def load_backup_info():
    if not os.path.exists(BACKUP_FILE):
        return {}
    
    return pickle.load(open(BACKUP_FILE, "rb"))
def rewrite_backup(backup_info):
    a_file = open(BACKUP_FILE, "wb")
    pickle.dump(backup_info, a_file)
    a_file.close()

def convert_action(backup_info, filename):
    status = False
    new_time = os.path.getmtime(filename)
    if filename in backup_info.keys():
        old_time = backup_info[filename]
        if new_time != old_time:
            status = True
    else:
        status = True

    backup_info[filename] = new_time
    return status

def convert_ui_to_py():
    backup_info = load_backup_info()
    for filename in glob.iglob('views/**', recursive=True):
        # if os.path.isfile(filename): # filter dirs
        if filename.endswith(".ui"):
            # new_py = os.path.dirname(filename)  + os.path.basename(filename).removesuffix('.ui')
            py_convert = "{0}\\{1}_ui.py".format(os.path.dirname(filename), os.path.basename(filename).removesuffix('.ui'))
            shell_uic = "pyside6-uic .\{0} -o .\{1}".format(filename, py_convert)
            print(shell_uic)
            if convert_action(backup_info, filename):
                print(filename)
                #TODO: check status was completed when excute command
                run_status = run(shell_uic)
                # print(run_status)
        elif filename.endswith(".qrc"):
            py_convert = "{0}\\{1}_rc.py".format(os.path.dirname(filename), os.path.basename(filename).removesuffix('.qrc'))
            shell_uic = "pyside6-rcc .\{0} -o .\{1}".format(filename, py_convert)
            print(shell_uic)
            if convert_action(backup_info, filename):
                print(filename)
                #TODO: check status was completed when excute command
                run_status = run(shell_uic)
                # print(run_status)

    rewrite_backup(backup_info)

convert_ui_to_py()