#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def checkResult(expected, real, input):
  if expected == real:
    print "OK"
  else:
    print "FizzBuzz(%d): %s != %s" % (input, expected, real)

##
# Main app
##
if __name__ == '__main__':
  pass

