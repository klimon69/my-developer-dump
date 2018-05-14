from PIL import Image
 # My image is a 200x374 jpeg that is 102kb large
foo = Image.open("C:\\Users\\Klimon\\PycharmProjects\\PHOTO_REDUCER\\images\\" + '222.bmp')
#foo.size(200,374)
 # I downsize the image with an ANTIALIAS filter (gives the highest quality)
foo = foo.resize((700,520),Image.ANTIALIAS)
#foo.save("C:\\Users\\Klimon\\PycharmProjects\\PHOTO_REDUCER\\images\\image_scaled.jpg",quality=95)
 # The saved downsized image size is 24.8kb
foo.save("C:\\Users\\Klimon\\PycharmProjects\\PHOTO_REDUCER\\images\\image_scaled_opt.jpg",optimize=True,quality=95)
 # The saved downsized image size is 22.9kb