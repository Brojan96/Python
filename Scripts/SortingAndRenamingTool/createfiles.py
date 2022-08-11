import os

for i in range(10000):
    open(os.getcwd() + '/test/file_' + str(i) +'.txt', 'w')
    #print(os.getcwd())

