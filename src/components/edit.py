def main(args):
    from platform import system
    import os
    windows = (system() == 'Windows')
    if windows:
        path = '\\'.join((os.getcwd()+'/components').split('/'))
        os.system('start '+path)
