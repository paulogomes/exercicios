#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class Romanos():
  '''
  Classe para trabalhar com números romanos
  '''

  def __init__(self):
    self.unidade = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    self.dezena  = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    self.centena = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    self.milhar  = ['', 'M', 'MM', 'MMM']

    self.lista = [self.unidade, self.dezena, self.centena, self.milhar]

  def converte(self, numero):
    '''
    Converte número Decimal para Romano
    '''

    casas = str(numero)[::-1]
    resultado = ''

    for i in range(len(casas)):
      resultado = self.lista[i][int(casas[i])] + resultado

    return resultado