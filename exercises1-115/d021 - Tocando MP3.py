import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('d021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

input('Deu certo?')

#Maneira 2: biblioteca playsound

#playsound.playsound('d021.mp3')
