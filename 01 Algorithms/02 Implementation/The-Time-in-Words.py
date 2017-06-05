#!/bin/python3

import sys

def timeInWords(h, m):
    l_m=['one minute', 'two minutes', 'three minutes', 'four minutes', 'five minutes', 'six minutes', 'seven minutes', 'eight minutes', 'nine minutes', 'ten minutes',
         'eleven minutes', 'twelve minutes', 'thirteen minutes', 'fourteen minutes', 'quarter', 'sixteen minutes', 'seventeen minutes', 'eighteen minutes', 'nineteen minutes', 'twenty minutes',
         'twenty one minutes', 'twenty two minutes', 'twenty three minutes', 'twenty four minutes', 'twenty five minutes', 'twenty six minutes', 'twenty seven minutes', 'twenty eight minutes', 'twenty nine minutes', 'half']
    l_h = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve']

    if m == 0:
        return "{0} o' clock".format(l_h[h-1])
    elif m <= 30:
        return "{0} past {1}".format(l_m[m-1],l_h[h-1])
    else:
        return "{0} to {1}".format(l_m[60-m-1],l_h[h])


h = int(input().strip())
m = int(input().strip())
print(timeInWords(h, m))