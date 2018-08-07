from PIL import Image

im = Image.open('D:\\1.jpg')
print(im.format,im.size,im.mode)
t = im.size
im.thumbnail((t[0]/2,t[1]/2))
im.save('D:\\2.jpg','JPEG')

