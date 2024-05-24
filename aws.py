# Funcion para verificar si el numero es primo
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generar numero entre 1 a 250
primes = [num for num in range(1, 251) if is_prime(num)]

# Mostrar los resultados del file
with open('results.txt', 'w') as file:
    for prime in primes:
        file.write(str(prime) + '\n')

print("Prime numbers between 1 to 250 have been saved to 'results.txt'.")




def factorial(numero):
    temporal = 1
    for i in range(numero):
        temporal *= i + 1
    return temporal

print(factorial(4))

    

























