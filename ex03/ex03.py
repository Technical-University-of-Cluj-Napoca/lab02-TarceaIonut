import datetime
from distutils.file_util import write_file
from colorama import *

def smart_log(*args, **kwargs) -> None:
    timestamp:bool = True
    color = True
    save_to:str = "log.txt"
    level = ""
    date = True
    res_str:str = ""
    for key, value in kwargs.items():
        if key == "timestamp":
            timestamp = value
        if key == "color":
            color = value
        if key == "save_to":
            save_to = value
        if key == "Level":
            level = value
        if key == "date":
            date = value
    if timestamp:
        res_str = res_str + datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S ")
    if date:
        res_str = res_str + datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d ")

    write_file(save_to, res_str)
    actual_color = None
    if level == "info":
        res_str += "[INFO] "
        actual_color = Fore.BLUE
    if level == "debug":
        res_str += "[DEBUG] "
        actual_color = Fore.LIGHTBLACK_EX
    if level == "warning":
        res_str += "[WARNING] "
        actual_color = Fore.YELLOW
    if level == "error":
        res_str += "[ERROR] "
        actual_color = Fore.RED

    for args in args:
        res_str = res_str + args
    if actual_color is not None and color:
        print(actual_color + res_str)
    else:
        print(res_str)

    write_file(save_to, res_str)

    pass

#smart_log("System star" ,date=True, Level="error", color=True)