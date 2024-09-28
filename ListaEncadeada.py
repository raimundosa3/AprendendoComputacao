from ClasseNo import *
class Lista:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addInicio(self,valor):
        novo=No(valor)
        novo.prox= self.head
        self.head=novo

    def addFinal(self,valor):
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
        return msg + str(cont)
    
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

teste=Lista()
teste.addInicio(20)
teste.addInicio(10)
teste.addInicio(0)
teste.addFinal(30)
print(teste)
print(teste.existe(30))
print(teste.existe(50))
teste.remove(30)
print(teste)