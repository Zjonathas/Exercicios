def teste(valor):
    teste1 = valor % 3
    teste2 = valor % 5
    if teste1 == 0 and teste2 == 0:
        return 'FizzBuzz'
    if teste1 == 0:
        return 'Fizz'
    if teste2 == 0:
        return 'Buzz'

    return valor


num = int(input('Digite um número: '))
print(f'{teste(num)}')
