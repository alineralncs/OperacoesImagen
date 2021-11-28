import cv2
from Imagem import *



img1 = lerImagem('imagens/200.png')
img2 = lerImagem('imagens/pisa-red-flag.jpg')
# deixar as imagens do mesmo tamanho
img2_resized = tamanhoigualImagem(img2, img1)

img3 = lerImagem('imagens/city.jpg')
img4 = lerImagem('imagens/cat.jpg')
img4_resized = tamanhoigualImagem(img4, img3)

img5 = lerImagem('imagens/guy.jpg')
img6 = lerImagem('imagens/person.jpg')
img6_resized = tamanhoigualImagem(img6, img5)

img7 = lerImagem('imagens/lena.png')
img8 = lerImagem('imagens/fingerprint.bmp')
img8_resized = tamanhoigualImagem(img8, img7)

img9 = lerImagem('imagens/water.jpg')
img10 = lerImagem('imagens/bee.jpg')
img10_resized = tamanhoigualImagem(img10, img9)

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
    9. Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        print("\n Você escolheu adição") 
        print('\n Imagens 1 e 2')
        add = adicao(img1, img2_resized)
        mostrar_salvar('adicao1.png', add, add)
        print('\n Imagens 3 e 4')
        add = adicao(img3, img4_resized)
        mostrar_salvar('adicao2.png', add, add)
        print('\n Imagens 5 e 6')
        add= adicao(img5, img6_resized)
        mostrar_salvar('adicao3.png', add, add)
        print('\n Imagens 7 e 8')
        add = adicao(img7, img8_resized)
        mostrar_salvar('adicao4.png', add, add)
        print('\n Imagens 9 e 10')
        add = adicao(img9, img10_resized)
        mostrar_salvar('adicao5.png', add, add)
    elif ans=="2":
        print("\n Você escolheu subtração")
        print('\n Imagens 1 e 2')
        sub = subtracao(img1, img2_resized)
        mostrar_salvar('subtracao1.png', sub, sub)
        print('\n Imagens 3 e 4')
        sub = subtracao(img3, img4_resized)
        mostrar_salvar('subtracao2.png', sub, sub)
        print('\n Imagens 5 e 6')
        sub = subtracao(img5, img6_resized)
        mostrar_salvar('subtracao3.png', sub, sub)
        print('\n Imagens 7 e 8')
        sub = subtracao(img7, img8_resized)
        mostrar_salvar('subtracao4.png', sub, sub)
        print('\n Imagens 9 e 10')
        sub = subtracao(img9, img10_resized)
        mostrar_salvar('subtracao5.png', sub, sub)
    elif ans=="3":
        
        print("\n Você escolheu divisao")
        print('\n Imagens 1 e 2')
        div = divisao(img1, img2_resized) 
        mostrar_salvar('divisao1.png', div, div)
        print('\n Imagens 3 e 4')
        div = divisao(img3, img4_resized) 
        mostrar_salvar('divisao2.png', div, div)
        print('\n Imagens 5 e 6')
        div = divisao(img5, img6_resized) 
        mostrar_salvar('divisao3.png', div, div)
        print('\n Imagens 7 e 8')
        div = divisao(img7, img8_resized) 
        mostrar_salvar('divisao4.png', div, div)
        print('\n Imagens 9 e 10')
        div = divisao(img9, img10_resized) 
        mostrar_salvar('divisao5.png', div, div)
    elif ans=="4":
        print("\n Você escolheu multiplicacao")
        print('\n Imagens 1 e 2')
        mult = multiplicacao(img1, img2_resized) 
        mostrar_salvar('mult1.png',  mult,  mult)
        print('\n Imagens 3 e 4')
        mult = multiplicacao(img3, img4_resized) 
        mostrar_salvar('mult2.png',  mult,  mult)
        print('\n Imagens 5 e 6')
        mult = multiplicacao(img5, img6_resized) 
        mostrar_salvar('mult3.png',  mult,  mult)
        print('\n Imagens 7 e 8')
        mult = multiplicacao(img7, img8_resized) 
        mostrar_salvar('mult4.png',  mult,  mult)
        print('\n Imagens 9 e 10')
        mult = multiplicacao(img9, img10_resized) 
        mostrar_salvar('mult5.png',  mult,  mult)
        
    elif ans=="5":
        print("\n Você escolheu translação")
        print('\n Imagem 1')
        trans = translacao(img1)
        mostrar_salvar('trans1.png', trans, trans)
        print('\n Imagem 2')
        trans = translacao(img6)
        mostrar_salvar('trans2.png', trans, trans)
        print('\n Imagem 3')
        trans = translacao(img5)
        mostrar_salvar('trans3.png', trans, trans)
        print('\n Imagem 4')
        trans = translacao(img7)
        mostrar_salvar('trans4.png', trans, trans)
        trans = translacao(img10)
        mostrar_salvar('trans5.png', trans, trans)
    elif ans=="6":
        print("\n Você escolheu escala")
        print('\n Imagem 1')
        esc= escala_cubic(img1)
        mostrar_salvar('escala1.png', esc, esc)
        print('\n Imagem 2')
        esc= escala_cubic(img6)
        mostrar_salvar('escala2.png', esc, esc)
        print('\n Imagem 3')
        esc= escala_cubic(img5)
        mostrar_salvar('escala3.png', esc, esc)
        print('\n Imagem 4')
        esc= escala_cubic(img7)
        mostrar_salvar('escala4.png', esc, esc)
        esc= escala_cubic(img10)
        mostrar_salvar('escala5.png', esc, esc)
    elif ans=="7":
        print("\n Você escolheu rotacao")
        print('\n Imagem 1')
        rot = rotacao(img1)
        mostrar_salvar('rotacao1.png', rot, rot)
        print('\n Imagem 2')
        rot = rotacao(img6)
        mostrar_salvar('rotacao2.png', rot, rot)
        print('\n Imagem 3')
        rot = rotacao(img5)
        mostrar_salvar('rotacao3.png', rot, rot)
        print('\n Imagem 4')
        rot = rotacao(img7)
        mostrar_salvar('rotacao4.png', rot, rot)
        rot = rotacao(img10)
        mostrar_salvar('rotacao5.png', rot, rot)
    elif ans=="8":
        print('\n Você escolheu reflexão')
        op = input("""
        1. Vertical
        2. Horizontal
        3. Vertical e Horizontal
        """)
        if op=='1':
            print('\n Imagem 1')
            vert = reflexao_vertical(img1)
            mostrar_salvar('reflexao1.png', vert, vert)
            print('\n Imagem 2')
            vert = reflexao_vertical(img6)
            mostrar_salvar('reflexao2.png', vert, vert)
            print('\n Imagem 3')
            vert = reflexao_vertical(img5)
            mostrar_salvar('reflexao3.png', vert, vert)
            print('\n Imagem 4')
            vert = reflexao_vertical(img7)
            mostrar_salvar('reflexao4.png', vert, vert)
            vert = reflexao_vertical(img10)
            mostrar_salvar('reflexao5.png', vert, vert)
        elif op=='2':
            print('\n Imagem 1')
            hor = reflexao_horizontal(img1)
            mostrar_salvar('horizontal1.png', hor, hor)
            print('\n Imagem 2')
            hor = reflexao_horizontal(img6)
            mostrar_salvar('horizontal2.png', hor, hor)
            print('\n Imagem 3')
            hor = reflexao_horizontal(img5)
            mostrar_salvar('horizontal3.png', hor, hor)
            print('\n Imagem 4')
            hor = reflexao_horizontal(img7)
            mostrar_salvar('horizontal4.png', hor, hor)
            hor = reflexao_horizontal(img10)
            mostrar_salvar('horizontal5.png', hor, hor)
        elif op=='3':
            print('\n Imagem 1')
            both = reflexao_vert_hori(img1)
            mostrar_salvar('both1.png', both, both)
            print('\n Imagem 2')
            both = reflexao_vert_hori(img6)
            mostrar_salvar('both2.png', both, both)
            print('\n Imagem 3')
            both = reflexao_vert_hori(img5)
            mostrar_salvar('both3.png', both, both)
            print('\n Imagem 4')
            both = reflexao_vert_hori(img7)
            mostrar_salvar('both4.png', both, both)
            both = reflexao_vert_hori(img10)
            mostrar_salvar('both5.png', both, both)
   
    elif ans=="9":
      print("\n Goodbye") 
      break
    elif ans !="":
      print("\n Not Valid Choice Try again") 



       # elif ans=='9':
    #     print('\n Imagem 1')
    #     mostrar_antes(img1)
    #     print('\n Imagem 2')
    #     mostrar_antes(img2)
    #     print('\n Imagem 3')
    #     mostrar_antes(img3)
    #     print('\n Imagem 4')
    #     mostrar_antes(img4)
    #     print('\n Imagem 5')
    #     mostrar_antes(img5)
    #     print('\n Imagem 6')
    #     mostrar_antes(img6)
    #     print('\n Imagem 7')
    #     mostrar_antes(img7)
    #     print('\n Imagem 8')
    #     mostrar_antes(img8)
    #     print('\n Imagem 9')
    #     mostrar_antes(img9)
    #     print('\n Imagem 10')
    #     mostrar_antes(img10)