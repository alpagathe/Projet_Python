from PIL import Image, ImageFilter

photo1=Image.open("/user/denouaia/homedir/E2/python/image1.jpg")
photo2=Image.open("/user/denouaia/homedir/E2/python/image2.jpg")
photo3=Image.open("/user/denouaia/homedir/E2/python/image3.jpg")
photo4=Image.open("/user/denouaia/homedir/E2/python/image4.jpg")
photo5=Image.open("/user/denouaia/homedir/E2/python/image5.jpg")
photo6=Image.open("/user/denouaia/homedir/E2/python/image6.jpg")

images = [photo1, photo2, photo3, photo4, photo5]

def median_images(images):
    #mettre du code ici
    #les images sont en RGB
    img = normalize(images)
    img_dest = Image.new("RGB", images[0].size)
    dest = img_dest.load()
    N = len(images)
    
    for y in range (images[0].size[1]):
        for x in range (images[0].size[0]):
            rp = []                     #listes pour les valeurs des pixels
            gp = []
            bp = []
            for i in range(N):          #pour travailler sur chaque pixel de chaque img
                pix = images[i].load()
                r1,g1,b1 = pix[x,y]
                rp.append(r1)           #valeurs rouge de chaque img
                gp.append(g1)           #valeurs verte de chaque img
                bp.append(b1)           #valeurs bleu de chaque img
            
            rp.sort()                   #trie des listes
            gp.sort()
            bp.sort()
            dest[x,y] = rp[N//2],gp[N//2],bp[N//2]     #la valeur med de chaque couleur
            
    return img_dest	


def normalize(images):
    minW = images[0].size[0]
    minH = images[0].size[1]
    maxW = images[0].size[0]
    maxH = images[0].size[1] #on initialise les variables min et max aux dimensions 
    #de la premiere image pour la comparer avec les suivantes

        
    for i in images:
        nvimages = []
        hauteur = []
        largeur = []
        hauteur.append(i.size[1])
        largeur.append(i.size[0]) #pas obligatoire de faire un tableau pour hauteur et largeur (inutile?!)


        if(hauteur[0] <= minH ):
            minH = hauteur[0]
        elif (hauteur[0] >= maxH):
            maxH = hauteur[0]
                
        if (largeur[0] <= minW):
            minW = largeur[0]
        elif (largeur[0] >= maxW) :
            maxW = largeur[0]
            
    if (minW == maxW and minH == maxH):
        return images
    
    for i in images:
        nvimages.append(crop(i, 0, 0, minH, minW))
    return nvimages



result = median_images(images)
result.show()