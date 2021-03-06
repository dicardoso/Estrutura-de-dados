import tkinter as tk
from tkinter import *
from tkinter import ttk
from No import No
from Fila import Fila
from Filme import Filme
import json

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(master)
        self.oitavoContainer["pady"] = 20
        self.oitavoContainer.pack()


  
        self.guifilme = Label(self.primeiroContainer, text="Adicionar Filmes")
        self.guifilme["font"] = ("Arial", "10", "bold")
        self.guifilme.pack()
  

        self.tituloLabel = Label(self.segundoContainer,text="Titulo", font=self.fontePadrao)
        self.tituloLabel.pack(side=TOP)
  
        self.titulo = Entry(self.segundoContainer)
        self.titulo["width"] = 30
        self.titulo["font"] = self.fontePadrao
        self.titulo.focus_force()
        self.titulo.pack(side=TOP)
  
        self.generoLabel = Label(self.terceiroContainer, text="Genero", font=self.fontePadrao)
        self.generoLabel.pack(side=TOP)
  
        self.genero = Entry(self.terceiroContainer)
        self.genero["width"] = 30
        self.genero["font"] = self.fontePadrao
        self.genero.pack(side=TOP)

        self.tempoLabel = Label(self.quartoContainer, text="Duração", font=self.fontePadrao)
        self.tempoLabel.pack(side=TOP)
  
        self.tempo = Entry(self.quartoContainer)
        self.tempo["width"] = 30
        self.tempo["font"] = self.fontePadrao
        self.tempo.pack(side=TOP)
  
        self.atoresLabel = Label(self.quintoContainer, text="Atores", font=self.fontePadrao)
        self.atoresLabel.pack(side=TOP)

        self.atores2Label = Label(self.quintoContainer, text="Escreva os nomes\n separados por ';'", font=('Helvetica', 10, 'bold'))
        self.atores2Label.pack(side=TOP)
  
        self.atores = Entry(self.quintoContainer)
        self.atores["width"] = 30
        self.atores["font"] = self.fontePadrao
        self.atores.pack(side=TOP)

        self.anoLabel = Label(self.sextoContainer, text="Ano", font=self.fontePadrao)
        self.anoLabel.pack(side=TOP)
  
        self.ano = Entry(self.sextoContainer)
        self.ano["width"] = 30
        self.ano["font"] = self.fontePadrao
        self.ano.pack(side=TOP)


        #self.nomeListaLabel = Label(self.setimoContainer, text="Nome da Lista", font=self.fontePadrao)
        #self.nomeListaLabel.pack(side=TOP)
  
        #self.nomeLista = Entry(self.setimoContainer)
        #self.nomeLista["width"] = 30
        #self.nomeLista["font"] = self.fontePadrao

        self.adicionarLa = Button(self.oitavoContainer)
        self.adicionarLa["text"] = "Adicionar"
        self.adicionarLa["font"] = ("Calibri", "8")
        self.adicionarLa["width"] = 12
        self.adicionarLa["command"] = self.adicionar
        self.adicionarLa.pack()

        self.deletar = Button(self.oitavoContainer)
        self.deletar["text"] = 'Deletar'
        self.deletar["font"] = ("Calibri", "8")
        self.deletar["width"] = 12
        self.deletar["command"] = self.remove
        self.deletar.pack()

        self.listar = Button(self.oitavoContainer)
        self.listar["text"] = 'Listar tamanho\nno terminal'
        self.listar["font"] = ("Calibri", "8")
        self.listar["width"] = 12
        self.listar["command"] = self.liste
        self.listar.pack()

        self.mensagem = Label(self.oitavoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Métodos
    def adicionar(self):
        titulo = self.titulo.get()
        genero = self.genero.get()
        tempo = self.tempo.get()
        atores = str(self.atores.get()).split(';')
        ano = self.ano.get()
        a.add(Filme(titulo,genero,tempo,atores,ano))
        
    
    def liste(self):
        print(a.size())

    def remove(self):
    	print(a.remove())


a = Fila()
root = Tk()
Application(root)
root.mainloop()