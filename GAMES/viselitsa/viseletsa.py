# -*- coding: utf-8 -*-


import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)

window = pygame.display.set_mode((800,600))
pygame.display.set_caption('Виселелица')



word = 'хуй'
word_silit = list(word)


textsurface0 = myfont.render(' _ '* len(word_silit), False, (0, 0, 0))

l1 = word_silit[0]
l2 = word_silit[1]
l3 = word_silit[2]

letterdict = [l1,l2,l3]
check_letter = ''

t1 = myfont.render(l1, False, (0, 0, 0))
t2 = myfont.render(l2, False, (0, 0, 0))
t3 = myfont.render(l3, False, (0, 0, 0))



'''
for q in range(0, len(word_silit)):
	
	textsurface = myfont.render(word_silit[q], False, (0, 0, 0))
	window.blit(textsurface,(q*60+215,50))
	print(word_silit[q])
	q = q+1
'''


letter0 = pygame.image.load("а.png")
letter1 = pygame.image.load("б.png")
letter2 = pygame.image.load("в.png")
letter3 = pygame.image.load("г.png")
letter4 = pygame.image.load("д.png")
letter5 = pygame.image.load("е.png")
letter6 = pygame.image.load("ж.png")
letter7 = pygame.image.load("з.png")
z1= 0
z2=0
z3= 0
z4=0

letter8 = pygame.image.load("и.png")
letter9 = pygame.image.load("й.png")
letter10 = pygame.image.load("к.png")
letter11 = pygame.image.load("л.png")
letter12 = pygame.image.load("м.png")
letter13 = pygame.image.load("н.png")
letter14 = pygame.image.load("о.png")
letter15 = pygame.image.load("п.png")


letter16 = pygame.image.load("р.png")
letter17 = pygame.image.load("с.png")
letter18 = pygame.image.load("т.png")
letter19 = pygame.image.load("у.png")
letter20 = pygame.image.load("ф.png")
letter21 = pygame.image.load("х.png")
letter22 = pygame.image.load("ц.png")
letter23 = pygame.image.load("ч.png")


letter24 = pygame.image.load("ш.png")
letter25 = pygame.image.load("щ.png")
letter26 = pygame.image.load("ъ.png")
letter27 = pygame.image.load("ы.png")
letter28 = pygame.image.load("ь.png")
letter29 = pygame.image.load("э.png")
letter30 = pygame.image.load("ю.png")
letter31 = pygame.image.load("я.png")


#letters_1st_row = {letter0:'а', letter1:'б', letter2:'в', letter3:'г', letter4:'д', letter5:'е', letter6:'ж', letter7:'з'}
letters_1st_row_keys = [letter0, letter1, letter2, letter3, letter4, letter5, letter6, letter7]
letters_2nd_row_keys = [letter8, letter9, letter10, letter11, letter12, letter13, letter14, letter15]
letters_3th_row_keys = [letter16, letter17, letter18, letter19, letter20, letter21, letter22, letter23]
letters_4th_row_keys = [letter24, letter25, letter26, letter27, letter28, letter29, letter30, letter31]






x = 50
y = 50
width = 40
height = 60
speed = 5
bg = pygame.image.load('bg2.jpg')
white = (255,255,255)
black = (0,0,0)

#screen = pygame.Surface((800,600))
window.blit(bg, (0,0))

#===============рисуем буквы=====================

for i in range(270, 720, 60):
	
	window.blit(letters_1st_row_keys[z1],(i,270))
	
	z1 = z1+1

for i in range(270, 720, 60):
	
	window.blit(letters_2nd_row_keys[z2],(i,340))
	
	z2 = z2+1

for i in range(270, 720, 60):
	
	window.blit(letters_3th_row_keys[z3],(i,410))
	
	z3 = z3+1
	
for i in range(270, 720, 60):
	
	window.blit(letters_4th_row_keys[z4],(i,480))
	
	z4 = z4+1

window.blit(textsurface0,(260,50))
window.blit(t1,(275,50))
window.blit(t2,(340,50))
window.blit(t3,(400,50))






run = True

while run:

	
	pygame.time.delay(100)  # цикл выполняется каждую 0,1 сек
	
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			run = False

		if e.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			#print(pos)
			x1,y1 = e.pos
			#print(x1,y1)
			
			x_first_row = 295

			if letter0.get_rect(center=(x_first_row,300)).collidepoint(x1, y1):
				check_letter = 'а'
			if letter1.get_rect(center=(x_first_row+60,300)).collidepoint(x1, y1):
				check_letter = 'б'
			if letter1.get_rect(center=(x_first_row+120,300)).collidepoint(x1, y1):
				check_letter = 'в'
			if letter1.get_rect(center=(x_first_row+180,300)).collidepoint(x1, y1):
				check_letter = 'г'
			if letter1.get_rect(center=(x_first_row+240,300)).collidepoint(x1, y1):
				check_letter = 'д'
			if letter1.get_rect(center=(x_first_row+300,300)).collidepoint(x1, y1):
				check_letter = 'е'
			if letter1.get_rect(center=(x_first_row+360,300)).collidepoint(x1, y1):
				check_letter = 'ж'
			if letter1.get_rect(center=(x_first_row+420,300)).collidepoint(x1, y1):
				check_letter = 'з'


	#====================2 row==================


			if letter0.get_rect(center=(x_first_row,370)).collidepoint(x1, y1):
				check_letter = 'и'
			if letter1.get_rect(center=(x_first_row+60,370)).collidepoint(x1, y1):
				check_letter = 'й'
			if letter1.get_rect(center=(x_first_row+120,370)).collidepoint(x1, y1):
				check_letter = 'к'
			if letter1.get_rect(center=(x_first_row+180,370)).collidepoint(x1, y1):
				check_letter = 'л'
			if letter1.get_rect(center=(x_first_row+240,370)).collidepoint(x1, y1):
				check_letter = 'м'
			if letter1.get_rect(center=(x_first_row+300,370)).collidepoint(x1, y1):
				check_letter = 'н'
			if letter1.get_rect(center=(x_first_row+360,370)).collidepoint(x1, y1):
				check_letter = 'о'
			if letter1.get_rect(center=(x_first_row+420,370)).collidepoint(x1, y1):
				check_letter = 'п'
				
				
#====================3 row==================


			if letter0.get_rect(center=(x_first_row,440)).collidepoint(x1, y1):
				check_letter = 'р'
			if letter1.get_rect(center=(x_first_row+60,440)).collidepoint(x1, y1):
				check_letter = 'с'
			if letter1.get_rect(center=(x_first_row+120,440)).collidepoint(x1, y1):
				check_letter = 'т'
			if letter1.get_rect(center=(x_first_row+180,440)).collidepoint(x1, y1):
				check_letter = 'у'
			if letter1.get_rect(center=(x_first_row+240,440)).collidepoint(x1, y1):
				check_letter = 'ф'
			if letter1.get_rect(center=(x_first_row+300,440)).collidepoint(x1, y1):
				check_letter = 'х'
			if letter1.get_rect(center=(x_first_row+360,440)).collidepoint(x1, y1):
				check_letter = 'ц'
			if letter1.get_rect(center=(x_first_row+420,440)).collidepoint(x1, y1):
				check_letter = 'ч'
				

#====================3 row==================


			if letter0.get_rect(center=(x_first_row,510)).collidepoint(x1, y1):
				check_letter = 'ш'
			if letter1.get_rect(center=(x_first_row+60,510)).collidepoint(x1, y1):
				check_letter = 'щ'
			if letter1.get_rect(center=(x_first_row+120,510)).collidepoint(x1, y1):
				check_letter = 'ъ'
			if letter1.get_rect(center=(x_first_row+180,510)).collidepoint(x1, y1):
				check_letter = 'ы'
			if letter1.get_rect(center=(x_first_row+240,510)).collidepoint(x1, y1):
				check_letter = 'ь'
			if letter1.get_rect(center=(x_first_row+300,510)).collidepoint(x1, y1):
				check_letter = 'э'
			if letter1.get_rect(center=(x_first_row+360,510)).collidepoint(x1, y1):
				check_letter = 'ю'
			if letter1.get_rect(center=(x_first_row+420,510)).collidepoint(x1, y1):
				check_letter = 'я'












	
	#========hero=======================

	
	


	#pygame.draw.rect(window,(0,0,255), (x, y, width, height))
	pygame.draw.line(window, black, (37,545), (220,545), 3)
	pygame.draw.line(window, black, (90,545), (90,260), 3)
	pygame.draw.line(window, black, (65,260), (220,260), 3)
	pygame.draw.line(window, black, (168,260), (168,310), 3)
	face = pygame.draw.circle(window, black, (168,330), 20, 3)
	pygame.draw.line(window, black, (168,350), (168,415), 3)
	pygame.draw.line(window, black, (168,415), (150,490), 3)
	pygame.draw.line(window, black, (168,415), (186,490), 3)
	pygame.draw.line(window, black, (168,350), (150,415), 3)
	pygame.draw.line(window, black, (168,350), (186,415), 3)

	pygame.draw.line(window, black, (63,545), (90,463), 3)
	pygame.draw.line(window, black, (115,545), (90,463), 3)

	pygame.draw.line(window, black, (90,285), (115,260), 3)



	#screen.fill((133,45,44))

	
	

	pygame.display.update()

pygame.quit()