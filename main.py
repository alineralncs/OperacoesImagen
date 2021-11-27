from cv2 import imread
from Imagem import *



img1 = lerImagem('imagens/200.png')
img2 = lerImagem('imagens/lena.png')
# deixar as imagens do mesmo tamanho
img2_resized = tamanhoigualImagem(img2, img1)

def mostrar_salvar(name, imagePath, funcao):
    print ("""

    1. Ver Imagem
    2. Salvar Imagem
    """)

    opc =input('Deseja ver ou salvar?')
    if opc=='2':
        save = cv2.imwrite(name, imagePath)
        print('Successfully saved')
        return save
    elif opc=='1':
        cv2.imshow('image',funcao)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


ans=True
while ans:
    print ("""
    Operações Aritméticas

    1. Adição
    2. Subtração
    3. Divisão
    4. Multiplicação
    
    Transformação Geométrica

    5. Translação
    6. Escala
    7. Rotação
    8. Reflexão
    9.Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        print("\n Você escolheu adição") 
        add = adicao(img1, img2_resized)
        mostrar_salvar('adicao.png', add, add)
        # salvarImagem('imagem_adicao.png', add)
    elif ans=="2":
        print("\n Você escolheu subtração")
        sub = subtracao(img1, img2)
        mostrar_salvar('subtracao.png', sub, sub)
    elif ans=="3":
        print("\n Você escolheu divisao")
        div = divisao(img1, img2) 
        mostrar_salvar('divisao.png', div, div)
    elif ans=="4":
        print("\n Você escolheu multiplicacao")
        mult = multiplicacao(img1, img2) 
        mostrar_salvar('divisao.png',  mult,  mult)
        
    elif ans=="5":
        print("\n Você escolheu translação")
        trans = translacao(img1)
        mostrar_salvar('trans.png', trans, trans)
    elif ans=="6":
        print("\n Você escolheu escala")
        esc= escala(img1)
        mostrar_salvar('escala.png', esc, esc)
    elif ans=="7":
        print("\n Você escolheu rotacao")
        rot = rotacao(img1)
        mostrar_salvar('rotacao.png', rot, rot)
    elif ans=="8":
      print("\n Goodbye") 
    elif ans=="9":
      print("\n Goodbye") 
      break
    elif ans !="":
      print("\n Not Valid Choice Try again") 
      