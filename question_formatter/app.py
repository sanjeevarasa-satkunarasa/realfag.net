# Note if you get an error it is due to the program not being outside of the question formatter folder.

import os
from math import *

def sorted_directory_listing_with_os_listdir(directory):
    items = os.listdir(directory)
    sorted_items = sorted(items, reverse=True)
    return sorted_items

sorted_array = sorted_directory_listing_with_os_listdir("eksamensoppgaver\Rettslære 2") # Set file directory

full_list = []
heading_list= []

i = 0
while i <= floor(len(sorted_array)/2):
    år = 2024-i
    år_str = str(år)
    heading_list.append("H"+år_str)
    heading_list.append("V"+år_str)
    i+=1
    
heading_list.pop(0)

file = open("output.txt", "w")
p = 0
for i in sorted_array:
    full_list.append("<li><h3>" + heading_list[p] + "</h3></li>\n")
    full_list.append("""<li><a href="/eksamensoppgaver\Rettslære 2/""" + i + """" target="_blank" download> Oppgave </a></li>\n""") # Remember to correct the file directory here as well
    p+=1    

print(full_list)
file.writelines(full_list)
file.close()