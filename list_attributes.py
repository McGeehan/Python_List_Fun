list = ['larry', 'curly', 'moe']
list.append('shemp') #adds a single element to a list
list.insert(0, 'xxx') #insert xxx to 1st point in list
list.extend(['yyy', 'xxx']) #add these values to end of list
print(list) #xxx, larry, curly, moe, shemp, yyy, xxx
print(list.index('curly')) #2

list.remove('curly') #search and remove
list.pop(1) #removes and return larry
print(list)



