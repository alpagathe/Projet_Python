
from PIL import Image, ImageFilter

background = Image.open("/user/denouaia/homedir/E2/python/background.jpg")
photo1=Image.open("/user/denouaia/homedir/E2/python/image1.jpg")
photo2=Image.open("/user/denouaia/homedir/E2/python/image2.jpg")
photo3=Image.open("/user/denouaia/homedir/E2/python/image3.jpg")
photo4=Image.open("/user/denouaia/homedir/E2/python/image4.jpg")
photo5=Image.open("/user/denouaia/homedir/E2/python/image5.jpg")
photo6=Image.open("/user/denouaia/homedir/E2/python/image6.jpg")

images = [background, photo1, photo2, photo3, photo4, photo5]

def mask(images):
    #img = normalize(images)
    img_dest = Image.new("RGB", images[0].size)
    dest = img_dest.load()
    masks = []
    N = len(images)
    

    for y in range (images[0].size[1]):
        for x in range (images[0].size[0]):
            rp = []                     #listes pour les valeurs des pixels
            gp = []
            bp = []
            for i in range(N):          #pour travailler sur chaque pixel de chaque img
                pix = images[i].load()
                pixb = images[0].load()
                r1,g1,b1 = pix[x,y]
                r2,g2,b2 = pixb[x,y]
                rp.append(r2-r1)
                gp.append(g2-g1)
                bp.append(b2-b1)
                
                # rp.append(r1)           #valeurs rouge de chaque img
                # gp.append(g1)           #valeurs verte de chaque img
                # bp.append(b1)           #valeurs bleu de chaque img
                

            # rp.sort()                   #trie des listes
            # gp.sort()
            # bp.sort()
            dest[x,y] = rp[N//2],gp[N//2],bp[N//2]     #la valeur med de chaque couleur
            masks.append(img_dest)
    return masks	

result = mask(images)
result[2].show()    