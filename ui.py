import os

def clear_screen():
    os.system("cls")

def header(title):
    clear_screen()
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)

def pause():
    input("\nPress Enter to continue...")