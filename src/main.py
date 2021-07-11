#!/usr/bin/python3
from os import listdir
from os.path import isfile, join
from time import sleep
import threading as th
from importlib import import_module,__import__, reload
from shlex import split
Command_list=[]
Modules = {}
MODULE_DIR = 'components'
def main():
    CommandListUpdate()
    Terminal()

def CommandListUpdate():
    global Command_list
    temp = ListOfModules()
    Command_list = temp
    # print(Command_list)

def ImportModule(module_name: str):
    global Modules
    assert len(module_name) >0
    try:
        if module_name in Modules.keys():
            Modules[module_name] = reload(Modules[module_name])
            return Modules[module_name]
        Modules[module_name] = import_module(f'{MODULE_DIR}.{module_name}')
        return Modules[module_name]
    except FileNotFoundError as ex:
        raise ex
    except Exception as ex:
        raise ex
    
def RunModule(module_name:str,args:object=[]):
    global MODULE_DIR
    assert len(module_name)>0
    ImportModule(module_name).main(CompileArgs(module_name,args))

def ListOfModules():
    global MODULE_DIR
    return [f[:-3] for f in listdir(MODULE_DIR) if isfile(join(MODULE_DIR, f)) and f[-3:] == '.py' and len(f)>=4]

def Command(arguments):
    global Command_list
    if not arguments[0] in Command_list:
        raise NoCommandException('')
    else:
        RunModule(arguments[0],arguments[1:])

def Terminal():
    IDENTYFIER = '~~ '
    cmd = []
    def GetCommand():
        raw = input(IDENTYFIER)
        if raw in ('q','quit','exit','\x04'):
            raise ExitException('exit')
        if len(raw)==0:
            return None
        return split(raw)

    def NoCommand():
        print(f'Unknown command \'{cmd[0]}\'')

    while True:
        try:
            cmd = GetCommand()
            CommandListUpdate()
            if cmd is None:
                continue
            Command(cmd)
        except ExitException as ex:
            break
        except NoCommandException as ex:
            NoCommand()
        except Exception as ex:
            print("Error Occured!")
            print(ex)

def CompileArgs(module_name,args):
    def CompileArgs_GlobalVariables():
        global MODULE_DIR
        return {'MODULE_DIR':MODULE_DIR}
    def CompileArgs_CommandFields(args):
        return args
    
    return {
        'Module_name': module_name,
        'Global':CompileArgs_GlobalVariables(),
        'Command': CompileArgs_CommandFields(args)
    }

class NoCommandException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ExitException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

if __name__ == '__main__':
    main()
