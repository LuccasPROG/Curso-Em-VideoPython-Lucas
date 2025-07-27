# Faça um programa em Python que abra e reproduza um arquivo mp3


import time
import pygame #um biblioteca para musicas etc . . . 
pygame.init() #init para iniciar o pygame
pygame.mixer.music.load('ex023a.mp3') # achar a musica pasta / carregar a musica
pygame.mixer.music.play() #dar play na musica
pygame.event.wait()
time.sleep(60) #a musica vai acabar quando chegar no 60 segundos !