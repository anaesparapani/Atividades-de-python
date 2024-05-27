import time 

beatles = [] # lista vazia

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)


for i in range(2):
    if i == 1:
        print()
        membro_adicionado = str(input('Escreva "Pete Best" para adicionar: ')) #adicionando pete na lista
        beatles.append(membro_adicionado)
    else:
        membro_adicionado = str(input('Escreva "Stu Sutcliffe" para adicionar:')) #adicionando stu na lista
        beatles.append(membro_adicionado)

print(beatles)
print()

del(beatles[-1]) #tirando pete da lista
del(beatles[-1]) #tirando stu da lista

print(beatles)

beatles.insert(0, "Ringo Starr")

print(beatles)


time.sleep(5)
