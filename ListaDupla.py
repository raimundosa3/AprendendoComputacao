from DuploNo import *

class Lista:
    def __init__(self):
        self.head=None
        self.cont=0
    
    def add(self,valor):
        self.cont+=1
        atual=self.head
        anterior=None
        novo=DuploNo(valor)

        if self.head is None:
            self.head=novo
            return True
        
        else:
            while atual is not None:
                if atual.getValor()>novo.getValor():

                    if anterior is None:
                        novo.prox=self.head
                        self.head.ant=novo
                        self.head=novo
                        return True
                    
                    else:

                        anterior.prox=novo
                        novo.ant=anterior
                        novo.prox=atual
                        atual.ant=novo
                        return True
                    
                anterior=atual
                atual=atual.prox

            anterior.prox=novo
            novo.ant=anterior
            novo.prox=None


    def existe(self,valor):
        a=False
        atual=self.head
        while atual is not None:
            if atual.getValor()==valor:
                a=True
                return True
            atual=atual.prox
        return a
    
    def remove(self,valor):
        if self.head is None:
            return False
        else:

            if self.head.getValor()==valor:
                if self.head.prox is None:
                    self.head=None
                else:
                    self.head=self.head.prox
                    self.head.ant=None
                return True
            
            atual=self.head.prox
            anterior=self.head
            while atual is not None:
                if atual.getValor()==valor:
                    anterior.prox=atual.prox
                    if atual.prox is not None:
                        atual.prox.ant=anterior
                    return True
                anterior=atual
                atual=atual.prox
        return False

    def __str__(self):
        msg=""
        atual=self.head
        while atual is not None:
            msg = msg + str(atual.getValor())+" "
            atual=atual.prox
        return msg + str(teste.cont)
    
teste=Lista()
teste.add(20)
teste.add(10)
teste.add(0)
teste.add(30)
print(teste)
print(teste.existe(30))
print(teste.existe(50))
teste.remove(30)
print(teste)

                        


        


