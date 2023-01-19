#!/usr/bin/env python3
from colorama import Back, Fore, Style

print(Fore.RED + "Red text")
print(Fore.GREEN + "Green text")
print(Fore.YELLOW + "Yellow text")
print(Fore.BLUE + "Blue text")
print(Fore.MAGENTA + "Magenta text")
print(Fore.CYAN + "Cyan text")
print(Fore.WHITE + "White text")

print(Fore.RED + Back.YELLOW + "Red text on yellow background")
print(Fore.GREEN + Back.CYAN + "Green text on cyan background")
print(Fore.YELLOW + Back.BLUE + "Yellow text on blue background")

print(Fore.RED + Style.BRIGHT + "Bright red text")
print(Fore.GREEN + Style.DIM + "Dim green text")
print(Fore.YELLOW + Style.NORMAL + "Normal yellow text")

print(Fore.RED + Back.YELLOW + Style.BRIGHT + "Bright red text on yellow background")
print(Fore.GREEN + Back.CYAN + Style.DIM + "Dim green text on cyan background")
print(Fore.YELLOW + Back.BLUE + Style.NORMAL + "Normal yellow text on blue background")

print(Fore.RESET + Back.RESET + "Back to normal text and background")
