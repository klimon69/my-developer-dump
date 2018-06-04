# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
import PIL.Image

from tkinter import *
#from Tkinter import messagebox
#from Tkinter import filedialog
import tkinter.filedialog
import tkinter.messagebox
import os

if __name__ == '__main__':
	
	root = Tk()
	root.title("Klim[ON]_image_resizer_1.0")
	root.geometry("320x400")
	root.resizable(False, False)
	
links = []
link_replace = ""
final_width = 694
final_heigh = 521

#=============open files===============================================	
	


def open():  
	
	button_2['state'] = 'normal'
	button_3['state'] = 'normal'

	filez =  tkinter.filedialog.askopenfilenames(parent=root, initialdir = "/",title = "Select file",filetypes = (("jpeg, bmp and png files","*.jpg *.bmp *.png"),("all files","*.*")))
	
	global links
	links = list(filez)
	return links


#==============================convert==================================	



def convert():
	
	button_2['state'] = 'disabled'
	
	num_of_files = 0
	a = int(enyry_1.get())
	b = int(enyry_2.get())
	
	save_filez =  tkinter.filedialog.askdirectory() # предлагаю дирректорию куда сохранить
	
 
	for link in links:
		num_of_files = num_of_files+1
		os.path.split(link)
		file_name = os.path.split(link)[1]
		link_replace = link.replace('/',r'\\')
		foo = PIL.Image.open(str(link_replace))
		# I downsize the image with an ANTIALIAS filter (gives the highest quality)
		

		foo = foo.resize((a,b),PIL.Image.ANTIALIAS)

		new_save_filez = save_filez.replace('/',r'\\')
		
		if '.jpg' in link_replace:
			#new_path = link_replace.replace('.jpg','(1).jpg')
			foo.save(str(new_save_filez)+'\\' + '(resized)'+str(file_name),optimize=True,quality=95)  # jpeg into jpeg

		elif '.bmp' in link_replace:
			#new_path = link_replace.replace('.bmp','(1).jpg')
			foo.save(str(new_save_filez)+'\\' + '(resized)'+str(file_name),optimize=True,quality=95)
		elif '.png' in link_replace:
			#new_path = link_replace.replace('.png','(1).jpg')
			foo.save(str(new_save_filez)+'\\' + '(resized)'+str(file_name),optimize=True,quality=95)
	messagebox.showinfo("Succes", str(num_of_files) +  "  files were resized")   # вывожу сообщение что всё гуд




#==============================crop==================================



def crop():
	
	button_2['state'] = 'disabled'
	
	num_of_files = 0
	
	save_filez =  tkinter.filedialog.askdirectory() # предлагаю дирректорию куда сохранить
	 
	for link in links:
		num_of_files = num_of_files+1
		os.path.split(link)
		file_name = os.path.split(link)[1]
		link_replace = link.replace('/',r'\\')
		
		foo = PIL.Image.open(str(link_replace))
				
		width, height = foo.size
		
		area = ((width+20)-width, 0, width-20, height) # x, y лувого верхнего углв, x,y правого нижнего угла
		
		foo = foo.crop(area)
		
		new_save_filez = save_filez.replace('/',r'\\')
		

		if '.jpg' in link_replace:
			#new_path = link_replace.replace('.jpg','(1).jpg')
			foo.save(str(new_save_filez)+'\\' + '(croped)'+str(file_name),optimize=True,quality=95)  # jpeg into jpeg

		elif '.bmp' in link_replace:
			#new_path = link_replace.replace('.bmp','(1).jpg')
			foo.save(str(new_save_filez)+'\\' + '(croped)'+str(file_name),optimize=True,quality=95)
		elif '.png' in link_replace:
			#new_path = link_replace.replace('.png','(1).jpg')
			foo.save(str(new_save_filez)+'\\' + '(croped)'+str(file_name),optimize=True,quality=95)
	messagebox.showinfo("Succes", str(num_of_files) +  "  files were croped")   # вывожу сообщение что всё гуд



#=================расположение=========================================




label_1 = Label(root, text='final_width (px.)') # надпись
label_2 = Label(root, text='final_heigh (px.)') # надпись
enyry_1 = Entry(root)                     #поле ввода ширины
enyry_1.insert(END, final_width)          #значени по умолчанию
enyry_2 = Entry(root)                     #поле ввода высоты
enyry_2.insert(END, final_heigh)          #значени по умолчанию
label_1.grid(row=0, padx=10,pady=30 ,sticky=E)
label_2.grid(row=1,padx=10, sticky=E)
enyry_1.grid(row=0, column=1, padx=10)
enyry_2.grid(row=1, column=1, padx=10)


#=====================================================================


button_1 = Button(root, width=20,height=3, text="Open photo", command = open)
button_1.grid(columnspan=4, rowspan=1, pady=30, padx=85)
button_1.bind()


button_2 = Button(root, width=20,height=3, state=DISABLED, text="RESIZE", command = convert)
button_2.grid( columnspan=6, rowspan=1, pady=5, padx=85)
button_2.bind()


button_3 = Button(root, width=20,height=3, state=DISABLED, text="CROP", command = crop)
button_3.grid( columnspan=6, rowspan=1, pady=35, padx=85)
button_3.bind()

