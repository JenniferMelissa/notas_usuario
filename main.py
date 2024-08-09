#incluir biblioteca
import os

#lista
notas = []

#limpar console
os.system('cls')

#loop
while True:
    print('======SOMAR NOTAS======\n')
    print('1 - Inserir notas.')
    print('2 - Calcular média das notas.')
    print('3 - Sair do programa.')

    #usuario indica a opcao desejada
    opcao = input('Opcao desejada: ')

    #limpar console
    os.system('cls')

    #verifica opcao desejada
    match opcao:
        case '1':
            #usuario informa a nova nota
            nova_nota = str(input('Informe nova nota de 0 a 10: ')).replace(',','.')

            #insere a nova nota ou retorna erro
            try:
                nova_nota = float(nova_nota)

                #verifica se a nota é maior que 0 ou menor que 10
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print(f'Nota {nova_nota} inserida com sucesso.')
                else:
                    print('Nota inválida!')
            except:
                print('Não foi possível inserir a nova nota.')
            finally:
                continue
        case '2':
            #calcula a media ou retorna erro
            try:
                media = sum(notas) / len(notas)
                print(f'A  média do aluno é {media:.2f}.')
            except:
                print('Não foi possível calcular a média.')
            finally:
                continue
        case '3':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida!')
            continue