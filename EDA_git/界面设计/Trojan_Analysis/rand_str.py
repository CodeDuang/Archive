import random
from time import sleep

from PyQt5.QtCore import QThread


def rand_str():
    z = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K',
         'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V',
         'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '!', '#', '$',
         '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', ';', ':', '[', ']', '\"', '\'', '|', '<', '>', ',',
         '.', '?', '/', '\\', '~', '`']
    x = []
    r2 = random.randint(1, 5)
    for i in range(r2):
        r = random.randint(0, 62)
        a = random.sample(z, r)
        x.extend(a)
        x.append(' ')
    return ''.join(x)

# for i in range(26):
#      print('\''+chr(ord('a')+i)+'\'',end=',')
#      print('\''+chr(ord('A')+i)+'\'',end=',')
# for i in range(10):
#      print('\''+str(i)+'\'',end=',')
