"""Peça do usuário um valor em graus para um ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo."""

import math

graus = float(input('Digite um valor em graus: '))

radianos = graus*math.pi/180

print('O seno é {}'.format(math.sin(radianos)))
print('O cosseno é {}'.format(math.cos(radianos)))
print('A tangente é {}'.format(math.tan(radianos)))