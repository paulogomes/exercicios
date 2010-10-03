#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from  DecimalRomano import Romanos
import re

romanos = Romanos()

massa = file('../teste.txt')
massa = massa.readlines()

class TesteNumerosRomano(unittest.TestCase):
  def testa_1_1449(self):
    for valores in massa:
      i = valores.split('=')
      self.assertEqual(romanos.converte(i[0]), re.sub("\n", '', i[1]))

if __name__ == "__main__":
  unittest.main()