import cv2
import numpy as np
#____________________________________________________________
# ler, salvar e redmensionar imagem
def lerImagem(imagePath):
    return cv2.imread(imagePath)

def salvarImagem(name, imagePath):
    save = cv2.imwrite(name, imagePath)
    print('Successfully saved')
    return save

def tamanhoigualImagem(img2, img1):
    return cv2.resize(img2, (img1.shape[1], img1.shape[0]))


#____________________________________________________________
# Operações Aritméticas
def adicao(img1, img2):
    return cv2.add(img1,img2)

def subtracao(img1, img2):
    return cv2.subtract(img1, img2)

def divisao(img1, img2):
    return cv2.divide(img1, img2)

def multiplicacao(img1, img2):
    return cv2.multiply(img1, img2)
#____________________________________________________________
# Transformações Geométricas
# Translação, Rotação, Escala, Reflexão.
def escala(img):
    return cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

def translacao(img):
    rows = img.shape[0]
    cols = img.shape[1]
    M = np.float32([[1,0,100], [0, 1, 50]])
    transl = cv2.warpAffine(img, M, (cols, rows))
    return transl

def rotacao(img):
    rows = img.shape[0]
    cols = img.shape[1]
    MN = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
    #AARUMAER LINHA 48
    translacao(img, MN, (cols, rows))




# import cv2
# import os
# class Imagens:
#     def __init__(self, img) :
#         self.img = img
#     def __str__(self):
#         return self.img
#     def lerImagem(self):
#         return cv2.imread(self.img)
#     def salvarImagem(imagePath, name):
#        return cv2.imwrite(name, imagePath)


# path_img1 = Imagens('imagens/vi.jpg')
# path_img2 = Imagens('imagens/jiinx.jpg')
# # img1 = 'imagens/200.png'
# # img2 = 'imagens/lena.png'

# img1 = Imagens.lerImagem(path_img1)
# img2 = Imagens.lerImagem(path_img2)


# img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# dst = cv2.add(img1,img2_resized)
# Imagens.salvarImagem('save.png', dst)
# print("After saving image:")  
# print(os.listdir('imagens'))
  
# print('Successfully saved')