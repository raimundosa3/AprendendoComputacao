from ClasseNo import *
class Lista:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    

    def addInicio(self,valor):
        if isinstance(valor, str):
            valor=valor.upper()
        if self.existe(valor):
            print("Nome ja cadastrado")
            return False
        novo=No(valor)
        novo.prox= self.head
        self.head=novo

    def addFinal(self,valor):
        if isinstance(valor, str):
            valor=valor.upper()
        if self.existe(valor):
            print("Nome ja cadastrado")
            return False
        novo=No(valor)
        if self.head is None:
            novo.prox=self.head
            self.head=novo
        else:
            atual =self.head
            while atual.prox is not None:
                atual=atual.prox
            
            atual.prox=novo
    
    def __str__(self):
        cont=0
        msg=""
        atual=self.head
        while atual is not None:
            msg = msg +str(atual.getValor())+" "
            atual=atual.prox
            cont+=1
        return msg +"qtd: " +str(cont)
    
    def existe(self,valor):
        atual=self.head
        while atual is not None:
            if atual.getValor()==valor:
                return True
                
            atual=atual.prox 
        return False   
    
    def remove(self,valor):
        atual=self.head
        anterior = None
        while atual is not None:
            if atual.getValor()==valor:
                if anterior is None:
                     self.head=atual.prox
                else:
                    anterior.prox=atual.prox
                return True
            anterior=atual
            atual=atual.prox
