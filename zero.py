list = []

while True:

    num = int(input('Digite um valor:'))

    if num != 0:
        list.append(num)
        print(list)
        print('Soma dos itens da lista:', sum(list))

    if num == 0:
        list.pop()
        print(list)
        print('Soma dos itens da lista:', sum(list))

    if sum(list) == 0:
        print('Error/Encerrado')
        break
        