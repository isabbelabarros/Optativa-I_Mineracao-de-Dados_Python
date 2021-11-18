"""Repita o processo da questão anterior, porém utilizando a função deg2rad da biblioteca numpy para converter o ângulo de graus para radianos."""

import math
import numpy

graus = float(input('Digite um valor em graus: '))

radianos = numpy.deg2rad(graus)

print('O seno é {}'.format(math.sin(radianos)))
print('O cosseno é {}'.format(math.cos(radianos)))
print('A tangente é {}'.format(math.tan(radianos)))
