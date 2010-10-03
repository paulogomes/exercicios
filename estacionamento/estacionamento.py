#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

class carro:
    def __init__(self, placa):
        pass

class bilheteria:
  def __init__(self):
      self.contador = 0
      self.controle = dict()
      
  def gerar(self, carro, entrada = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())):
    self.entrada = entrada
    self.contador += 1
    self.controle[self.contador] = [self.entrada, None, 'Aberto']
    return self.contador

  def encerrar(self, bilhete, saida = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())):
    self.controle[bilhete][1] = '1' #saida
    self.controle[bilhete][2] = 'Fechado'