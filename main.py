# Sorts and de-dupes .bash_aliases

aliases = 'aliases.txt'

with open(aliases,'r') as aka:
    original = aka.readlines()
# Turn the list of lines into a set, then back    
    no_dupe = list(set(original))
    no_dupe.sort()
     
with open(aliases,'w') as aka:
    aka.writelines(no_dupe)
