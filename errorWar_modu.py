#!/usr/bin/python3
from traceback import format_exception
from datetime import datetime
import sys

def errors_run_log():
    '''
    该函数记录的信息和输出的信息有问题
    :return:
    '''
    nows_date=str(datetime.now().strftime('''%Y-%m-%d %H:%M:%S'''))
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_list=format_exception(exc_type, exc_value,exc_traceback)
    for infos in exc_list:
        if infos.startswith("Traceback"):
            reps=infos.replace('\n',nows_date)
        elif "Error" in infos:
            ends=infos.replace('\n',nows_date)
        else:
            errors=infos.replace('\n','')
    with open("error_{}_debug.log".format(datetime.now().strftime('''%Y-%m-%d''')),"a") as eDebug:
        eDebug.write(reps+'\n')
        eDebug.write(errors+'\n')
        eDebug.write(ends+'\n')
        eDebug.write('------------------------log_info--------------------------------\n')

def print_debug_info():
    nows_date=str(datetime.now().strftime('''%Y-%m-%d %H:%M:%S'''))
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_list=format_exception(exc_type, exc_value,exc_traceback)
    for infos in exc_list:
        if infos.startswith("Traceback"):
            reps=infos.replace('\n',nows_date)
        elif "Error" in infos:
            ends=infos.replace('\n',nows_date)
        else:
            errors=infos.replace('\n','')
    print(reps)
    print(errors)
    print(ends)

def result_debug_type():
    nows_date=str(datetime.now().strftime('''%Y-%m-%d %H:%M:%S'''))
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_list=format_exception(exc_type, exc_value,exc_traceback)
    for infos in exc_list:
        if infos.startswith("Traceback"):
            reps=infos.replace('\n',nows_date)
        elif "Error" in infos:
            ends=infos.replace('\n',nows_date)
        else:
            errors=infos.replace('\n','')
    print(ends.split(':')[0])

def main():
    try:
        1/0
    except:
        result_debug_type()
        errors_run_log()
if __name__ == "__main__":
    main()