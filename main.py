from locale import windows_locale

import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('Setup End')

print('loop Start')
while True:
   # Check todos os eventos
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        print("quitting...")
        pygame.quit() #fechar a janela
        quit() 