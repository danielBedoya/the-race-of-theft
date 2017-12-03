import configparser
import pygame
import sys
import time
import math

ALTO=550
ANCHO=700
ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
AZUL=(59,131,189)
centro=[ANCHO/2,ALTO/2]

def drop_string(cad):
	i=0
	ncad=''
	for c in cad:
		if i == 0:
			i+=1
		else:
			ncad= ncad + c
	return ncad


if __name__== '__main__':
	pygame.init()
	pygame.display.set_caption('Mapas')
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	pantalla.fill(NEGRO)
	interprete=configparser.ConfigParser()
	interprete.read('mapa.map')
	barra=pygame.image.load('Barra.png')
	nada=pygame.image.load('inv.png')
	dicc={}
	for seccion in interprete.sections():
		descripcion=dict(interprete.items(seccion))
		dicc[seccion]=descripcion
	reloj=pygame.time.Clock()

	inicio=pygame.time.get_ticks()
	mapa=dicc['nivel1-tutorial']['mapa']
	lineas=mapa.split()
	j=0
	fin=False
	while not fin:
		tiempo=pygame.time.get_ticks()
		pantalla.fill(NEGRO)
		for i in range(len(lineas)):
			j=0
			for o in lineas[i]:
				if j>21 and tiempo%3<=1:
					lineas[i]=drop_string(lineas[i])
					break
				if o =='.':
					pantalla.blit(nada,(j*36,i*36))
				if o =='$':
					pantalla.blit(barra,(j*32,i*32))
				'''
				if o =='&':
					pantalla.blit(agua,(j*32,i*32))'''
				j+=1
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		reloj.tick(60)