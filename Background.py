from PIL import Image, ImageFilter
import sys

if len(sys.argv) <2 :
	print("utilisation : python3", sys.argv[0], "<image>")
	exit()

img=Image.open(sys.argv[1]) 
img.show()
