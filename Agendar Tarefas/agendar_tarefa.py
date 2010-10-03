#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from elixir import *

metadata.bind = "sqlite:///teste.bd"

class Tarefa(Entity):
	using_options(tablename="tarefas")
	nome = Field(String)
	comando = Field(String)
    
	def __repr__(self):
		return '<"%s" (%s)>' % (self.nome, self.comando)

setup_all()
#create_all()

Tarefa(nome='Teste_paulo',comando='Comando_2')

session.commit()
