#!/usr/bin/env python

# script para determinar as escalas de um tema mediante
# o numero de sustenidos ou bemois numa pauta / partitura

import os

# intro do programa

os.system("clear")
os.system("echo Ola $USER")
os.system("date")
os.system("toilet -f mono9 -F metal PyScales")
os.system("figlet -f digital bybelaLobo")


print ("Programa para determinar escalas")

# prompt do programa

try:
	acc = raw_input("Insira ---> 1 para armadura de sustenidos (#) ou ---> 2 para armadura de bemois(b): ")
	accident = int(acc)
	
	if accident > 2:
		print ("Insira um numero entre 1 e 2")
	else:
		os.system("clear")
		print ("Define a escala a partir do numero de acidentes numa armadura")


	# MAIN PROGRAM

	# ARMADURA DE SUSTENIDOS

	if accident == 1:
		print ("Armadura de sustenidos")
		susnum = raw_input("Insira numero de sustenidos (1-7): ")
		sus = int(susnum)

		if sus == 1:
			os.system("clear")
			print ("Escala Sol maior e Mi menor")
			print ("Numero de sustenidos:",sus)
		if sus == 2:
			os.system("clear")
			print ("Escala Re maior e Si menor")
			print ("Numero de sustenidos:",sus)
		if sus == 3:
			os.system("clear")
			print ("Escala La maior e Fa# menor")
			print ("Numero de sustenidos:",sus)
		if sus == 4:
			os.system("clear")
			print ("Escala Mi maior e Do# menor")
			print ("Numero de sustenidos:",sus)
		if sus == 5:
			os.system("clear")
			print ("Escala Si maior e Sol# menor")
			print ("Numero de sustenidos:",sus)
		if sus == 6:
			os.system("clear")
			print ("Escala Fa# maior e Re# menor")
			print ("Numero de sustenidos:",sus)
		if sus == 7:
			os.system("clear")
			print ("Escala Do# maior e La# menor")
			print ("Numero de sustenidos:",sus)
		if sus > 7: 
			print ("Insira um numero entre 1 e 7")

	# ARMADURA DE BEMOIS

	if accident == 2:
		print ("Armadura de bemois")
		bemnum = raw_input("Insira numero de bemois (1-7): ")
		bem = int(bemnum)

		if bem == 1:
			os.system("clear")
			print ("Escala de Fa maior e Re menor",bem)
			print ("Numero de bemois",bem)	
		if bem == 2:
			os.system("clear")
			print ("Escala de Sib maior e Sol menor",bem)
			print ("Numero de bemois",bem)
		if bem == 3:
			os.system("clear")
			print ("Escala de Mib maior e Do menor",bem)
			print ("Numero de bemois",bem)
		if bem == 4:
			os.system("clear")
			print ("Escala de Lab maior e Fa menor",bem)
			print ("Numero de bemois",bem)
		if bem == 5:
			os.system("clear")
			print ("Escala de Reb maior e Sib menor",bem)
			print ("Numero de bemois",bem)
		if bem == 6:
			os.system("clear")
			print ("Escala de Solb maior e Mib menor",bem)
			print ("Numero de bemois",bem)
		if bem == 7:
			os.system("clear")
			print ("Escala de Dob maior e Lab menor",bem)
			print ("Numero de bemois",bem)
		if bem > 7:			
			print ("Insira um numero entre 1 e 7")
# MENSAGEM DE ERRO
except:
	os.system("clear")
	print ("Insira um valor de forma numerica ex: 1,2,4,6,7")

# PROGRAM EXIT
print ("Finit!")

# This program uses the programs toilet and figlet for the intro
# script by staxxx aka belalobo 2015
