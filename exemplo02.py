with open('carro.txt', 'w', encoding='utf-8') as file:
    file.write('Corsa\n') 
    file.write('Kombi\n')
    file.write('chevette\n')
    file.write('Santana\n')
    file.write('Passat\n')
    file.write('Uno Mile\n')
    file.write('Opala\n')

with open('carro.txt', 'a', encoding='utf-8') as arquivo:

    for i in range(3):
        meu_carro = input('Digite um novo carro: ')
        arquivo.write(meu_carro + '\n')
        