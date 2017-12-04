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

class Cuchilla(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.giro = ['Cuchilla2.png', 'Cuchilla3.png', 'Cuchilla4.png', 'Cuchilla5.png', 'Cuchilla6.png','Cuchilla7.png']
		self.image = pygame.image.load('Cuchilla1.png').convert_alpha()
		self.i=0
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		self.image = pygame.image.load(self.giro[self.i]).convert_alpha()
		self.i+=1
		if self.i>5:
			self.i=0



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
	fondo1=pygame.image.load('Fondo1.jpg')
	barra=pygame.image.load('Barra.png')
	nada=pygame.image.load('inv.png')
	bloque=pygame.image.load('Bloque.png')
	dicc={}
	for seccion in interprete.sections():
		descripcion=dict(interprete.items(seccion))
		dicc[seccion]=descripcion
	reloj=pygame.time.Clock()
	general = pygame.sprite.Group()
	cuchillas = pygame.sprite.Group()
	general.add(cuchillas)

	inicio=pygame.time.get_ticks()
	mapa=dicc['nivel1-tutorial']['mapa']
	lineas=mapa.split()
	temporizador=5
	j=0
	fin=False
	x=30
	x1=0
	in_game=True
	vel=True
	while not fin:
		pantalla.blit(fondo1,(x1,-250))
		tiempo=(math.floor((pygame.time.get_ticks()-inicio)/1000))
		#print(tiempo%10)

		if tiempo%5==0 and tiempo!=0 and vel and x >= 0:
			x-=5
			vel=False
		else:
			vel = True
		for i in range(len(lineas)):
			j=0
			for o in lineas[i]:
				if j>21:
					lineas[i]=drop_string(lineas[i])
					break
				if o =='.':
					pantalla.blit(nada,(j*36,i*36))
				if o =='$':
					pantalla.blit(barra,(j*32,i*32))
				if o =='#':
					pantalla.blit(bloque,(j*32,i*32))
				if o =='&':
					cu=Cuchilla(j*32,i*32)
					cuchillas.add(cu)
					general.add(cu)	
				j+=1
		general.update()
		general.draw(pantalla)
		pygame.display.flip()
		for cu in cuchillas:
			cuchillas.remove(cu)
			general.remove(cu)
		pygame.time.delay(50)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		if not(in_game) or x <=0:
			reloj.tick(60)
		else:
			pygame.time.delay(x)
			#reloj.tick(60)
		x1-=1