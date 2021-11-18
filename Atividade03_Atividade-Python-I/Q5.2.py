"""Faça um Python Script que receba um valor t referente a uma quantidade total em segundos. Calcule a quantas horas:minutos:segundos a quantidade total de segudos corresponde."""

t = int(input('Digite o tempo em segundos: '))

minutos = t//60
segundos = t%60

horas = minutos//60
minutos = minutos%60

print('{:02d}:{:02d}:{:02d}'.format(horas, minutos, segundos))