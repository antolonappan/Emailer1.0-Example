import glob
import os
from mymail import *
from sys import stdout
from time import sleep

#################Animated Printing##################
def w_f_f():                                      ##
    stdout.write("\rWaiting for files /")         ##
    stdout.flush()                                ##
    sleep(.2)                                     ##
    stdout.write("\rWaiting for files -")         ##
    stdout.flush()                                ##
    sleep(.2)                                     ##
    stdout.write("\rWaiting for files \\")        ##
    stdout.flush()                                ##
    sleep(.2)                                     ##
    stdout.write("\rWaiting for files |")         ##
    stdout.flush()                                ##
    sleep(.2)                                     ##
####################################################

while True:
  listoffiles = glob.glob("*.txt")
  if 'data0.1.txt' and 'data0.5.txt' and 'data1.0.txt' and 'data1.5.txt' and 'data2.0.txt' in listoffiles:
     stdout.write("\n")
     print('All files found')
     sleep(1)
     print('Plotting')
     os.system('python cornerplot.py 2>/dev/null') 
     break
  w_f_f()

send('antoidicherian@gmail.com','output_file1.pdf')
print('email has been sent')



