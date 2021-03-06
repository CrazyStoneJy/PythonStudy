#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, time  
# for i in range(5):  
#    sys.stdout.write('{0}\r'.format(i + 1))  
#    sys.stdout.flush()  
#    time.sleep(1)  

# for i in range(5):  
#     sys.stdout.write(str(i) * (5 - i) + '\r')  
#     sys.stdout.flush()  
#     time.sleep(1)

# for i in range(5):  
#     sys.stdout.write(' ' * 10 + '\r')  
#     sys.stdout.flush()  
#     print(i)  
#     sys.stdout.write(str(i) * (5 - i) + '\r')  
#     sys.stdout.flush()  
#     time.sleep(1)  


class ProgressBar:  
    def __init__(self,count = 0,total = 0,width = 50):  
        self.count = count  
        self.total = total  
        self.width = width  
    def move(self):  
        self.count += 1  
    def log(self,s):  
        sys.stdout.write(' ' * (self.width + 9) + '\r')  
        sys.stdout.flush()  
        print(s)  
        progress = self.width * self.count / self.total  
        print('progress:'+str(progress))
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count,self.total))  
        sys.stdout.write('#' * int(progress) + '-' * int(self.width - progress) + '\r')  
        if progress == self.width:  
            sys.stdout.write('\n')  
        sys.stdout.flush() 

bar = ProgressBar(total = 10)  
for i in range(10):  
    bar.move()  
    bar.log('We have arrived at: ' + str(i + 1))  
    time.sleep(1)  
    