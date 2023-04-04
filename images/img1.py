import imghdr
from PIL import Image
imghdr.what('/root/Pictures/business1.png')
img = Image.open('/root/Pictures/business1.png')
print(img.format)
print(img.size)
print(img.mode)
img.show()

crop = (55,70,85,100)
img2 = img.crop(crop)
img2.show()