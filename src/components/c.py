def main():
    from platform import system
    import os
    if system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
