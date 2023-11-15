 import time
time.sleep(0.5)
print('Tu signo del zodiaco')
time.sleep(0.5)
print('...')
time.sleep(1)
num1 = int(input('Día de nacimiento: '))
time.sleep(0.5)
num2 = int(input('Mes de nacimiento: '))
time.sleep(0.5)
print('...')
time.sleep(1)
if num1 > 31 or  num2 > 12 or num1 < 1 or num2 < 1:
    print('mes o día no válido')
else:
    if num1 >=23 and num2 ==12:
        print('Eres Capricornio')
    if num1 <= 19 and num2 ==1:
        print('Eres Capricornio')

    if num1 >=20 and num2 ==1:
        print('Eres Acuario')
    if num1 <= 19 and num2 ==2:
        print('Eres Acuario')

    if num1 >=20 and num2 ==2:
        print('Eres Piscis')
    if num1 <= 20 and num2 ==3:
        print('Eres Piscis')

    if num1 >=21 and num2 ==3:
        print('Eres Aries')
    if num1 <= 19 and num2 ==4:
        print('Eres Aries')

    if num1 >=20 and num2 ==4:
        print('Eres Tauro')
    if num1 <= 20 and num2 ==5:
        print('Eres Tauro')

    if num1 >=21 and num2 ==5:
        print('Eres Géminis')
    if num1 <=20 and num2 ==6:
        print('Eres Géminis')

    if num1 >=21 and num2 ==6:
        print('Eres Cáncer')
    if num1 <=21 and num2 ==7:
        print('Eres Cáncer')

    if num1 >=22 and num2 ==7:
        print('Eres Leo')
    if num1 <= 22 and num2 ==8:
        print('Eres Leo')

    if num1 >=23 and num2 ==8:
        print('Eres Virgo')
    if num1 <= 22 and num2 ==9:
        print('Eres Virgo')

    if num1 >=23 and num2 ==9:
        print('Eres Libra')
    if num1 <= 22 and num2 ==10:
        print('Eres Libra')

    if num1 >=23 and num2 ==10:
        print('Eres Escorpio')
    if num1 <= 21 and num2 ==11:
        print('Eres Escorpio')

    if num1 >=22 and num2 ==11:
        print('Eres Sagitario')
    if num1 <= 22 and num2 ==12:
        print('Eres Sagitario')
