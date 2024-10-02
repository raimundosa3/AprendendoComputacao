from ListaDupla import *
from ListaEncadeada import *
from ClasseNo import*
from DuploNo import *

if __name__ == '__main__':
    teste=Lista()
    #adicionando no inicio
    teste.addInicio("Raimundo")
    teste.addInicio("Rommel")
    teste.addInicio(20)
    teste.addInicio("Raimundo")
    teste.addInicio(10)
    teste.addInicio(10)
    teste.addInicio(0)
    teste.addInicio("raimundo")
    print(teste)
    #adicionando no final
    teste.addFinal(30)
    teste.addFinal(30)
    teste.addFinal("Inacio")
    teste.addFinal("Inacio")
    print(teste)
    #executando o existe
    try:
        a=int(input("digite numero: "))
        print(teste.existe(a))
    except:
        a=input("digite nome: ")
        
        print(teste.existe(a.upper()))

    #removendo os elementos
    teste.remove(30)
    print(teste)
    print("finalizando questao 1!!!\n\n" )

    teste2=Lista2()
    teste2.add(20)
    teste2.add(10)
    teste2.add(0)
    teste2.add(30)
    teste2.add(30)
    print(teste2)

    a=int(input("digite numero: "))
    print(teste2.existe(a))


    teste2.remove(30)
    print(teste2)
    print("finalizando questao 2!!!\n\n\n" )