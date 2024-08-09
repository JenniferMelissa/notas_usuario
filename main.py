print('======SOMAR NOTAS======\n')
print('1 - Adicionar notas.')
print('2 - Sair do programa.')

opcao = int(input('Informe a opção desejada: '))

match opcao:
    case 1:
        # quantidade de notas digitadas pelo usuario
        quantidade_notas = int(input("Digite a quantidade de notas: "))
        # lista vazia para armazenar as notas
        notas = []
        # notas do usuario
        for i in range(quantidade_notas):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)

        # media das notas do usuario
        media = sum(notas) / quantidade_notas

        # exibe o resultado
        print(f"A média das notas é: {media:.2f}")
    case 2:
        #encerrar programa
        print('Programa encerrado. Obrigada!')
    case _:
        #quando o usuario digitar outro numero que nao esta na lista
        print('Opcao não encontrada!')

