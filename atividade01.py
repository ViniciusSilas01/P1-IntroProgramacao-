with open ('mobydick.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()
    print(conteudo) 

print(f'O tipo de linhas é : {type(conteudo)}')
print(f'A quantidade de linhas é: {len(conteudo)}')  