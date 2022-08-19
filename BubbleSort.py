# Example of Bubble Sort code 
# given a random list of eight elements (int)

import random

def Bubble(list):
    n = len(list)
    for i in range(n):
        for j in range(0,n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j+1]= list[j+1], list[j]
    return list


if __name__=='__main__':
    randomlist = [random.randint(0,100) for i in range (8)]
    print(randomlist)
    print("Executing Bubble Sort.. ")
    print(Bubble(randomlist))