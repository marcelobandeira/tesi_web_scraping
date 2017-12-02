# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from scrap.models import *
# Create your views here.

def index(request):	
	return render(request,'index.html')

def questao1(request):
	items = Questao1.objects.all()
	return render(request,'questao1.html', {'items' : items})

def questao2(request):
	items = Questao2.objects.all()
	return render(request,'questao2.html', {'items' : items})

def questao3(request):
	scrap_questao3()
	items = Questao3.objects.all().order_by('-id')[:5]
	return render(request,'questao3.html', {'items' : items})

def questao4(request):
	items = Questao4.objects.all()
	return render(request,'questao4.html', {'items' : items})


import requests
from bs4 import BeautifulSoup

def download(url, num_retries=2):
	# print('Downloading:', url)
	page = None
	try:
		response = requests.get(url)
		page = response.text
		if response.status_code >= 400:
			print('Download error:', response.text)
		if num_retries and 500 <= response.status_code < 600:
			return download(url, num_retries - 1)
	except requests.exceptions.RequestException as e:
		print('Download error:', e.reason)
	return page


from selenium import webdriver
from decimal import Decimal
from re import sub
def scrap_questao1():

	browser = webdriver.Chrome('/home/asus/Documents/tesi/chromedriver')
	browser.get('https://www.rottentomatoes.com/browse/tv-list-1')
	movies = browser.find_elements_by_css_selector('.movie_info')

	for m in movies:
		print("aqui de novo")
		title = m.find_element_by_css_selector('.movieTitle')
		print(title.text)
		score_to_insert = ''
		try:
			score = m.find_element_by_css_selector('.tMeterScore')
			score_to_insert = score.text
			print(score.text)
		except:
			print("no score")

		Questao1.objects.create(
                            movie=title.text,
                            rating=score_to_insert)




def scrap_questao2():
	url ='http://www.imdb.com/chart/boxoffice'
	html = download(url)
	soup = BeautifulSoup(html, 'html.parser')
	table = soup.find(attrs={'class':'chart'})
	trs = table.find_all('tr')
	length = len(trs)
	index = 1
	while index < length:
		title = trs[index].find(attrs={'class':'titleColumn'})
		print(title.text)
		gross = trs[index].find_all(attrs={'class':'ratingColumn'})
		print(gross[0].text)
		print(gross[1].text)
		weeks = trs[index].find(attrs={'class':'weeksColumn'})
		print(weeks.text)
		index+=1

		Questao2.objects.create(
                            movie=title.text,
                            gross=gross[0].text,
                            gross_total=gross[1].text,
                            weeks=weeks.text)


def scrap_questao3():
	url ='https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi'
	html = download(url)
	soup = BeautifulSoup(html, 'html.parser')

	temperatura = soup.find(attrs={'id': 'momento-temperatura'})
	print(temperatura.text)
	condicao = soup.find(attrs={'id': 'momento-condicao'})
	print(condicao.text)
	sensacao = soup.find(attrs={'id': 'momento-sensacao'})
	print(sensacao.text)
	humidade = soup.find(attrs={'id': 'momento-humidade'})
	print(humidade.text)
	pressao = soup.find(attrs={'id': 'momento-pressao'})
	print(pressao.text)
	atualizacao = soup.find(attrs={'id': 'momento-atualizacao'})
	print(atualizacao.text)

	if not Questao3.objects.filter(updated_at=atualizacao.text).exists():

		Questao3.objects.create(
                            temperature=temperatura.text,
                            condition=condicao.text,
                            sensation=sensacao.text,
                            humidity=humidade.text,
                            pressure=pressao.text,
                            updated_at=atualizacao.text)

import time
import re
def scrap_questao4():
	for i in range(25):
		print i
		url ='http://example.webscraping.com/places/default/index/' + str(i)
		html = download(url)
		soup = BeautifulSoup(html, 'html.parser')
		results = soup.find(attrs={'id': 'results'})
		for a in results.find_all('a', href=True):
			print "Found the URL:", a['href']
			time.sleep(3)
			country_url ='http://example.webscraping.com' + a['href']
			country_html = download(country_url)
			country_soup = BeautifulSoup(country_html, 'html.parser')

			country_name_row = country_soup.find(attrs={'id': 'places_country__row'})
			country_name = country_name_row.find(attrs={'class': 'w2p_fw'})
			print(country_name.text)

			country_area_row = country_soup.find(attrs={'id': 'places_area__row'})
			country_area = country_area_row.find(attrs={'class': 'w2p_fw'})
			print(country_area.text)
			area = re.sub(r'[^0-9]', '', country_area.text)
			print(area)

			country_population_row = country_soup.find(attrs={'id': 'places_population__row'})
			country_population = country_population_row.find(attrs={'class': 'w2p_fw'})
			population = re.sub(r'[^0-9]', '', country_population.text)
			print(population)
			if float(area) == 0:
				density = population
			else:
				density = float(population) / float(area)
			print(density)

			Questao4.objects.create(
                            country=country_name.text,
                            density=density)

def scrap_questao5():
	url ='http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento'
	html = download(url)
	soup = BeautifulSoup(html, 'xml')

	empreendimentos = soup.find_all('copa:empreendimento')
	
	total_previsto = 0
	total_executado = 0
	for empreendimento in empreendimentos:
		if empreendimento.ativo.text == 'true':
			try:
				valor_previsto = float(empreendimento.valorTotalPrevisto.text)
			except:
				valor_previsto = 0

			try:
				valor_executado = float(empreendimento.valorPercentualExecucaoFisica.text) * valor_previsto/100
			except:
				valor_executado = 0

			total_previsto += valor_previsto
			total_executado += valor_executado 

	print(total_previsto)
	print(total_executado)


# def scrap_questao6():
# 	url ='http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento'
# 	html = download(url)
# 	soup = BeautifulSoup(html, 'xml')
	
# 	empreendimentos = soup.find_all('copa:empreendimento')
# 	total_previsto = 0
# 	total_executado = 0

# 	cidades = []
# 	for empreendimento in empreendimentos:
# 		cidade_id = empreendimento.cidadeSede.id.text
# 		if cidade_id not in cidades:
# 			cidades.append(cidade_id)
# 	print(cidades)
	
# 	for empreendimento in empreendimentos:
# 		if empreendimento.ativo.text == 'true':
# 			try:
# 				valor_previsto = float(empreendimento.valorTotalPrevisto.text)
# 			except:
# 				valor_previsto = 0

# 			try:
# 				valor_executado = float(empreendimento.valorPercentualExecucaoFisica.text) * valor_previsto/100
# 			except:
# 				valor_executado = 0

# 			sedeIndex = cidades.index(empreendimento.cidadeSede.id.text))
				
# 			if()
# 			total_previsto += valor_previsto
# 			total_executado += valor_executado

# 			print(total_previsto)
# 			print(total_executado)


