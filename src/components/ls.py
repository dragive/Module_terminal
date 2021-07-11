from os import listdir
from os.path import isfile, join
MODULE_DIR = ''
def main(args):
    global MODULE_DIR
    MODULE_DIR=args['Global']['MODULE_DIR']
    ListOfModules()
    
def ListOfModules():
    global MODULE_DIR
    print( '\n'.join([f[:-3] for f in listdir(MODULE_DIR)
            if isfile(join(MODULE_DIR, f)) and f[-3:] == '.py' and len(f)>=4]))


