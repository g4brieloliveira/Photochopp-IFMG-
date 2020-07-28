from PIL import Image, ImageTk
import tkinter as tkinter
from tkinter import Label, Menu, Tk, Frame, Text
from copy import copy
import tkinter.filedialog as janela

def abreImagem(meiotela):
    arquivo = None
    caminho = janela.askopenfilename(filetypes=[('Imagem', ['.jpg', '.png', '.bmp'])])
    if type(caminho) == str:
        arquivo = Image.open(caminho)
        print(arquivo.size)
        resize(arquivo)

def filtroBlackWhite(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (128, 128, 128):
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None

def filtroInverso(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (128, 128, 128):
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None

def filtroBrasil(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (128, 128, 128):
                pixels[i, j] = (0, 0, 255)
            else:
                pixels[i, j] = (255, 255, 0)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None

def filtroCoringa(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (34,139,34):
                pixels[i, j] = (255,105,180)
            elif pixels[i, j] <= (218,165,32):
                pixels [i, j] = (105,89,205)
            elif pixels[i, j] <= (178,34,34):
                pixels [i, j] = (64,224,208)
            elif pixels[i, j] <= (255,140,0):
                pixels [i, j] = (173,255,47)
            else:
                pixels[i, j] = (255, 255, 255)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None

def filtroTropical(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (34,139,34):
                pixels[i, j] = (255,215,0)
            elif pixels[i, j] <= (218,165,32):
                pixels [i, j] = (127,255,212)
            elif pixels[i, j] <= (178,34,34):
                pixels [i, j] = (218,165,32)
            elif pixels[i, j] <= (255,140,0):
                pixels [i, j] = (173,255,47)
            else:
                pixels[i, j] = (255, 255, 255)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None

def filtroAzul(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (34,139,34):
                pixels[i, j] = (65,105,225)
            elif pixels[i, j] <= (218,165,32):
                pixels [i, j] = (32,178,170)
            elif pixels[i, j] <= (178,34,34):
                pixels [i, j] = (173,216,230)
            elif pixels[i, j] <= (255,140,0):
                pixels [i, j] = (135,206,235)
            else:
                pixels[i, j] = (173,216,230)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None

def filtroWaves(meiotela):
    if meiotela.image is None:
        meiotela.file = abreImagem(meiotela)
        meiotela.image = ImageTk.PhotoImage(meiotela.file)
    pixels = meiotela.file.load()
    for i in range(1, meiotela.file.size[0] - 1):
        for j in range(1, meiotela.file.size[1] - 1):
            if pixels[i, j] <= (34,139,34):
                pixels[i, j] = (148,0,211)
            elif pixels[i, j] <= (218,165,32):
                pixels [i, j] = (0,191,255)
            elif pixels[i, j] <= (178,34,34):
                pixels [i, j] = (124,252,0)
            elif pixels[i, j] <= (255,140,0):
                pixels [i, j] = (255,165,0)
            else:
                pixels[i, j] = (255,215,0)
    imagem = ImageTk.PhotoImage(meiotela.file)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.text = None


def resize(arquivo):
    if arquivo.size[0] >= arquivo.size[1]:
                if arquivo.size[0] > 600:
                    proporcao = arquivo.size[0]/600
                    arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                    print(arquivo.size)
                    meiotela.file = arquivo

                    if arquivo.size[1] > 500:
                        proporcao = 500/arquivo.size[1]
                        arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                        print(arquivo.size)
                        meiotela.file = arquivo
                    
                else:
                    proporcao = 600/arquivo.size[0]
                    arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                    print(arquivo.size)
                    meiotela.file = arquivo

                    if arquivo.size[1] > 500:
                        proporcao = 500/arquivo.size[1]
                        arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                        print(arquivo.size)
                        meiotela.file = arquivo
                
    else:
                if arquivo.size[1] > 500:
                    proporcao = arquivo.size[1]/500
                    arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                    print(arquivo.size)
                    meiotela.file = arquivo

                    if arquivo.size[0] > 600:
                        proporcao = 500/arquivo.size[1]
                        arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                        print(arquivo.size)
                        meiotela.file = arquivo
                    
                else:
                    proporcao = 500/arquivo.size[1]
                    arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                    print(arquivo.size)
                    meiotela.file = arquivo

                    if arquivo.size[0] > 600:
                        proporcao = 500/arquivo.size[1]
                        arquivo = arquivo.resize((int(arquivo.size[0] * proporcao), int(arquivo.size[1] * proporcao)), Image.ANTIALIAS)
                        print(arquivo.size)
                        meiotela.file = arquivo
    imagem = ImageTk.PhotoImage(arquivo)
    meiotela.config(image=imagem)
    meiotela.image = imagem
    meiotela.config(text=None)
    meiotela.text = None

    return(arquivo)
       

def sobreAutor(meiotela):
    meiotela.configure(background='grey')
    texto = 'Gabriel Augusto - IFMG \nPedro H. Tavares - IFMG\nLuiz Felipe - IFMG\nPedro H. José - IFMG'
    meiotela.config(text=texto)
    meiotela.image = None
    meiotela.file = None
    meiotela.text = texto
    meiotela.configure(bg="grey",font=("Helvetica", 15, "italic"))

def telaInicial(conteudo):
    meiotela.configure(background='grey')
    texto = 'Bem-vindo ao PhotoChopp'
    meiotela.config(text=texto)
    meiotela.image = None
    meiotela.file = None
    meiotela.text = texto
    meiotela.configure(bg="grey",font=("Helvetica", 15, "italic bold"))

telaraiz = Tk()
conteudo = Frame(telaraiz)
conteudo.pack()
meiotela = Label(conteudo, file=None, image=None, text=None)
meiotela.image = None
meiotela.file = None
meiotela.text = None
meiotela.pack()
telaInicial(conteudo)

barraMenu = Menu(conteudo)
telaraiz.config(menu=barraMenu)
telaraiz.title('Photochopp')
telaraiz.resizable(width=False, height=False)
telaraiz.configure(background='grey')
telaraiz.geometry('600x500')

opcao1 = Menu(barraMenu, tearoff=False)
opcao2 = Menu(barraMenu, tearoff=False)
opcao3 = Menu(barraMenu, tearoff=False)
barraMenu.add_cascade(label='Comandos', menu=opcao1)
barraMenu.add_cascade(label='Filtros', menu=opcao3)
barraMenu.add_cascade(label='Sobre', menu=opcao2)
opcao1.add_command(label='Abrir imagem...', command=lambda: abreImagem(meiotela))
opcao3.add_command(label='Aplicar filtro Black & White', command=lambda: filtroBlackWhite(meiotela))
opcao3.add_separator()
opcao3.add_command(label='Aplicar filtro Inverso', command=lambda: filtroInverso(meiotela))
opcao3.add_separator()
opcao3.add_command(label='Aplicar filtro Brasil', command=lambda: filtroBrasil(meiotela))
opcao3.add_separator()
opcao3.add_command(label='Aplicar filtro Azul', command=lambda: filtroAzul(meiotela))
opcao3.add_separator()
opcao3.add_command(label='Aplicar filtro Coringa', command=lambda: filtroCoringa(meiotela))
opcao3.add_separator()
opcao3.add_command(label='Aplicar filtro Tropical', command=lambda: filtroTropical(meiotela))
opcao3.add_separator()
opcao3.add_command(label='Aplicar filtro Waves', command=lambda: filtroWaves(meiotela))
opcao2.add_command(label='Autores', command=lambda: sobreAutor(meiotela))

telaraiz.mainloop()
