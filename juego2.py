import random
import pygame
from pygame.locals import QUIT

ventana_hori=800
ventana_vert=600
fps=60
blanco=(255,255,255)
negro=(0,0,0)


class pelotapong:

	def __init__(self,fichero_imagen):

		self.imagen=pygame.image.load(fichero_imagen).convert_alpha()

		self.ancho,self.alto=self.imagen.get_size()

		self.dir_x=random.choice([-5,5])
		self.dir_y=random.choice([-5,5])

		self.puntuacion=0
		self.puntuacion_ia=0

	def mover(self):
		self.x+=self.dir_x
		self.y+=self.dir_y

	def rebotar(self):
		if self.x<=-self.ancho:
			self.reiniciar()
			self.puntuacion_ia +=1
		if self.x>=ventana_hori:
			self.reiniciar()
			self.puntuacion +=1
		if self.y<=0:
			self.dir_y=-self.dir_y
		if self.y + self.dir_x:
			self.dir_y = random.choice([-5,5])

class raquetapong:
	def __init__(self):
		self.imagen=pygame.image.load("raqueta.png").convert_alpha()

		self.ancho,self.alto=self.imagen.get_size()

		self.x=0
		self.y=ventana_vert/2 - self.alto/2

		self.dir_y=0

		def mover(self):
			self.y += self.dir_y
			if self.y<=0:
				self.y=0
			if self.y + self.alto>=ventana_vert:
				self.y=ventana_vert-self.alto
	def mover_ia(self,pelota):
		if self.y>pelota.y:
			self.dir_y= -3


		self.y += self.dir_y

	def golpear(self,pelota):
		if (pelota.x<self.x +self.ancho and pelota.x>self.x and pelota.y + pelota.alto>self.y and pelota.y < self.y + self.alto):
			pelota.dir_x= -pelota.dir_x
			pelota.x= self.x + self.ancho

	def golpear_ia(self,pelota):
		if (pelota.x + pelota.ancho>self.x and pelota.x < self.x + self.x + self.ancho and pelota.y + pelota.alto> self.y and pelota.y < self.y + self.alto):
			pelota.dir_x = pelota.dir_x
			pelota.x = self.x - pelota.ancho



	def menu():
		pygame.init()

		ventana=pygame.display.set_mode((ventana_hori,ventana_vert))
		pygame.display.set_caption("pong 9")

		fuente=pygame.font.Font(none, 60)

		pelota=pelotapong("Bola_roja.png")

		raque1=raquetapong()
		raque1.x=60

		raque2 =raquetapong()
		raque2.x=ventana_hori - 60 - raque2.ancho


		jugando=True

		while jugando:
			pelota.mover()
			pelota.rebotar()
			raque1.mover()
			raque2.mover_ia()
			raque1.golpear()
			raque2.golpear_ia()

			ventana.fill(blanco)
			ventana.blit(pelota.imagen,(pelota.x,pelota.y))
			ventana.blit(raque1.imagen,(raque1.x,raque1.y))
			ventana.blit(raque2.imagen,(raque2.x,raque2.y))

			texto= f"{pleota.puntuacion} : {pelota.puntuacion_ia}"
			letrero=fuente.render(texto, False, negro)
			ventana.blit(letrero,(ventana_hori/2 - fuente.size(texto)[0]/2, 50))

			for event in pygame.event.get():
				if event.type == QUIT:
					jugando = False

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						raque1.dir_y = -5
					if event.key == pygame.K_s:
						raque1.dir_y = 5

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						raque1.dir_y =0
					if event.key == pygame.K_s:
						raque1.dir_y =0


			pygame.display.flip()
			pygame.time.clock().tick(fps)

		pygame.QUIT()


if __name__ == "__menu__":
	menu()

		
	
