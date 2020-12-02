#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

FIZZ = 'fizz'
BUZZ = 'buzz'
FIZZ_BUZZ = FIZZ + ' ' + BUZZ

def checkResult(expected, real, input):
  if expected == real:
    print "OK"
  else:
    print "FizzBuzz(%d): %s != %s" % (input, expected, real)

def fizzBuzz(input):
  if input % 3 == 0 and input % 5 == 0:
    return FIZZ_BUZZ
  elif input % 3 == 0:
    return FIZZ
  elif input % 5 == 0:
    return BUZZ
  else: 
    return input
  
##
# Main app
##
if __name__ == '__main__':
  checkResult(FIZZ_BUZZ, fizzBuzz(0), 0);
  checkResult(1, fizzBuzz(1), 1);
  checkResult(2, fizzBuzz(2), 2);
  checkResult(FIZZ, fizzBuzz(3), 3);
  checkResult(4, fizzBuzz(4), 4);
  checkResult(BUZZ, fizzBuzz(5), 5);
  checkResult(FIZZ, fizzBuzz(6), 6);
  checkResult(7, fizzBuzz(7), 7);
  checkResult(8, fizzBuzz(8), 8);
  checkResult(FIZZ, fizzBuzz(9), 9);
  checkResult(BUZZ, fizzBuzz(10), 10);
  checkResult(11, fizzBuzz(11), 11);
  checkResult(FIZZ, fizzBuzz(12), 12);
  checkResult(13, fizzBuzz(13), 13);
  checkResult(14, fizzBuzz(14), 14);
  checkResult(FIZZ_BUZZ, fizzBuzz(15), 15);
