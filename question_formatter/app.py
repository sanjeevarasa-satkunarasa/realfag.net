import os
from math import *

def sorted_directory_listing_with_os_listdir(directory):
    items = os.listdir(directory)
    sorted_items = sorted(items, reverse=True)
    return sorted_items

sorted_array = sorted_directory_listing_with_os_listdir("eksamensoppgaver/R1") # Set file directory

full_list = []

f = open("list.txt", "a")

for i in sorted_array:
    full_list.append("""<li><a href="/eksamensoppgaver/R1/""" + i + """" target="_blank" download> Oppgave </a></li>\n""") # Remember to correct the file directory here as well

f.writelines(full_list)
f.close()