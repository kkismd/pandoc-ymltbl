#! /usr/bin/env python

from pandocfilters import toJSONFilter, Emph, Para

def behead(key, value, format, meta):
  print(key)

if __name__ == "__main__":
  toJSONFilter(behead)
