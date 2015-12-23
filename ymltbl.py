#! /usr/bin/env python
# coding: utf-8

import pandocfilters as pandoc
import yaml

def walk(key, value, format, meta):
  if key == 'CodeBlock':
    [[ident, classes, keyvals], code] = value
    if ident == u'ymltbl':
      data = yaml.load(code)
      return array2tbl(data)

def array2tbl(data):
  colsize = len(data[0])
  head = data[0]
  body = data[1:]
  return pandoc.Table(
    caption(),
    aligns(colsize),
    widths(colsize),
    headers(head),
    rows(body))

def caption():
  "テーブルのキャプション"
  return []

def aligns(size):
  "各カラムのアライン"
  def alignDefault(): return { "t": "AlignDefault",  "c": [] }
  return [alignDefault() for x in range(size)]

def widths(size):
  "各カラムの幅"
  return [0 for x in range(size)]

def headers(cols):
  return [parse(col) for col in cols]

def rows(data):
  def plainStr(s): return [pandoc.Plain([pandoc.Str(s)])]
  return [ [ parse(col) for col in cols] for cols in data]

def parse(string):
  result = []
  tokens = unicode(string).split(" ")
  objects = [pandoc.Str(token) for token in tokens]
  for obj in objects:
    result.append(obj)
    result.append(pandoc.Space())
  result = result[:-1]
  return [pandoc.Plain(result)]

if __name__ == "__main__":
  pandoc.toJSONFilter(walk)
