from PIL import Image, ImageTk
import PIL.Image
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox

root = Tk()
links = []
link_replace = ""
final_width = 694
final_heigh = 521



#def open_image():

	
	
	


def open(event):   # event скорее всегу будет косяк - костыль
	button_2['state'] = 'normal'
	filez =  filedialog.askopenfilenames(parent=root, initialdir = "/",title = "Select file",filetypes = (("jpeg, bmp and png files","*.jpg *.bmp *.png"),("all files","*.*")))
	global links
	links = list(filez)
	return links

	#print (root.tk.splitlist(filez)) #как кортеж
	
	#print (list(filez)) #как список


	



def convert(event):
	#global link_replace
	a = int(enyry_1.get())
	b = int(enyry_2.get())
	for link in links:
		#print(link)
		link_replace = link.replace('/',r'\\')
		#print(link_replace)
		#open image
		foo = PIL.Image.open(str(link_replace))
		#print(link_replace)
		# I downsize the image with an ANTIALIAS filter (gives the highest quality)
		

		foo = foo.resize((a,b),PIL.Image.ANTIALIAS)
		if '.jpg' in link_replace:
			new_path = link_replace.replace('.jpg','(1).jpg')
			foo.save(str(new_path),optimize=True,quality=95)
		elif '.bmp' in link_replace:
			new_path = link_replace.replace('.bmp','(1).jpg')
			foo.save(str(new_path),optimize=True,quality=95)
		elif '.png' in link_replace:
			new_path = link_replace.replace('.png','(1).jpg')
			foo.save(str(new_path),optimize=True,quality=95)
	button_3['state'] = 'normal'

def save(event):
   save_filez =  filedialog.asksaveasfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("jpeg, bmp and png files","*.jpg *.bmp *.png"),("all files","*.*")))
   print(save_filez)




#глобальные переменные ширины и высоты финального изображения




label_1 = Label(root, text='final_width') # надпись
label_2 = Label(root, text='final_heigh') # надпись
enyry_1 = Entry(root)                     #поле ввода ширины
enyry_1.insert(END, final_width)          #значени по умолчанию
enyry_2 = Entry(root)                     #поле ввода высоты
enyry_2.insert(END, final_heigh)          #значени по умолчанию
label_1.grid(row=0, padx=10, sticky=E)
label_2.grid(row=1,padx=10, sticky=E)
enyry_1.grid(row=0, column=1, padx=10)
enyry_2.grid(row=1, column=1, padx=10)


#=====================================================================


button_1 = Button(root, text="Открыть фото")
button_1.grid(columnspan=4, rowspan=2, pady=20)
button_1.bind("<Button-1>", open)


button_2 = Button(root, state=DISABLED, text="CONVERT")
button_2.grid(columnspan=4, rowspan=2, pady=20)
button_2.bind("<Button-1>", convert)


button_3 = Button(root, state=DISABLED, text="SAVE")
button_3.grid(columnspan=4, rowspan=2, pady=20)
button_3.bind("<Button-1>", save)


