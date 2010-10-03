import unittest
from estacionamento import *
import time

class TesteEstacionamentoNormal(unittest.TestCase):
  def setUp(self):
    self.fusca = carro("XYZ-1234")
    self.entrada = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
    self.saida = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
    self.caixa = bilheteria()

  def teste_entra_um_carro(self):
    self.bilhete = self.caixa.gerar(self.fusca, self.entrada)
    self.assertEqual(self.bilhete, 1)

  def teste_entra_sai_um_carro(self):
    self.bilhete = self.caixa.gerar(self.fusca, self.entrada)
    self.caixa.encerrar(self.bilhete, self.saida)
    self.assertEqual(self.caixa.controle[self.bilhete][2], 'Fechado')

if __name__ == '__main__':
    unittest.main()