#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(len(Belgium)*'-')

print(Belgium.replace(',',': '))

#c) The population of Belgium (the second field) plus the population
# of the capital city (the fourth field). Hint: the answer should be 11183818.

Belgium_split = (Belgium.split(','))
print(int(Belgium_split[1]) + int(Belgium_split[3]))

