import random
alunos=["Jõao" , "Felipe", "Pedro" , "Ana" , "Lucas" , "Maria"]
print(f"Lista: {alunos}")
# Embaralhar a lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Ordena a Lista Crescente
alunos.sort()
print(f"Lista cresente: {alunos}")
# Ordena a Lista Decrescente
alunos.sort(reverse=True)
print(f"Lista decrescente: {alunos}")  