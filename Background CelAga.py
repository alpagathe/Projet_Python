from PIL import Image, ImageFilter
import sys

if len(sys.argv) <2 :
	print("utilisation : python3", sys.argv[0], "<image>")
	exit()

img=Image.open(sys.argv[1]) 
img1=Image.open(sys.argv[1]) 
img2=Image.open(sys.argv[1]) 
img3=Image.open(sys.argv[1]) 
img4=Image.open(sys.argv[1]) 
img5=Image.open(sys.argv[1]) 

#img.show()

images = [img,img1,img2,img3,img4,img5]
img.show()


def crop(im, top, left, bottom, right):
    cop = im.copy()
    pix=cop.load() 
    a=right-left
    b=bottom-top
    im=Image.new("RGB", (a,b))
    pixim=im.load()
    for y in range (b):
        for x in range (a):
        
            
            xl=x+left
            yr=y+top
            pixim[x,y]=pix[xl,yr]
        
    return im
    #im est une image RGB
    pass#pass sert juste a ce que ca compile

def normalize(images):
    #mettre du code ici 
    minW=1000000
    minH=1000000
    maxW=0
    maxH=0
    
    for im in images:
        
        w,h=im.size
        
        if (minW>w):
            minW=w
        if (maxW<w):
            maxW=w
            
        if (minH>h):
            minH=h
        if (maxH<h):
            maxH=h
        
           
    if (minW==maxW and minH==maxH):
        return images
        
    else :
        l=[]
        for im in images:
            l.append(crop(im,0,0,minH,minW))
        
        
    return l

def median (images) :

    im=normalize(images)
    
    R=Image.new("RGB",im[0].size)
    RR=R.load()
  
    
    for y in range (im[0].size[1]):
        for x in range (im[0].size[0]):
            mr=[]
            mg=[]
            mb=[]
        
            for img in images:
                ima=img.load()      
                r,g,b=ima[x,y]
		mr.append(r)
                mg.append(g)
                mb.append(b)
            
            mr.sort()
            mg.sort()
            mb.sort()
            medianr=mr[len(mr)//2]
            mediang=mg[len(mg)//2]            
            medianb=mb[len(mb)//2]
            
            RR[x,y]=medianr,mediang,medianb
    return R    
