from PIL import Image, ImageFilter

def median_images(images):
    #mettre du code ici
    #les images sont en RGB
    #img = normalize(images)
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


photo1=Image.open("/user/sisavanc/pp/image1.jpg")
photo2=Image.open("/user/sisavanc/pp/image2.jpg")
photo3=Image.open("/user/sisavanc/pp/image3.jpg")

images = [photo1, photo2, photo3]
result = median_images(images)
result.show()
