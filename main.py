import json
import math

# Реализация с загрузкой ответа по методу parameters/operation
with open("input/text.json", "r") as file:
    data = json.load(file)

# Создание словаря для заполнения параметрами калькулятора
check = dict()


# Функция для работы со значениями вне блоков из файла
def decaps(x):
    func = data[x]
    return func


# Функция для работы со значениями в блоке margin из файла
def decapsMargin(y):
    func = float(data["margin"][y])

    return func


# Функция для работы со значениями в блоке commissionInfo из файла
def decapsCommissionInfo(z):
    func = float(data["commissionInfo"][z])
    return func


# Обращения по функции decaps
lotSize = decaps("lotSize")
marketInsuranceValue = decaps("marketInsuranceValue")

# Обращения по функции decapsMargin
fundsAvailable = decapsMargin("fundsAvailable")
discountShort = decapsMargin("discountShort")
discountLong = decapsMargin("discountLong")
plannedPosition = decapsMargin("plannedPosition")

# Обращения по функции decapsCommissionInfo
minValue = decapsCommissionInfo("minValue")
valueInPercent = decapsCommissionInfo("valueInPercent")

# Получение даты вне parameters/operation
price = float(input("Цена заявки"))
Crossrate = float(input("Crossrate"))

# Заворачиваем значения в параметры словаря check
check['discount'] = input(" Используем discountShort = (S) или discountLong = (L)")
check['direction'] = input("По направлению (1) или против направления (2)")

# Заводим значение комиссии в словарь check
if (fundsAvailable / (1 + valueInPercent)) - (minValue / valueInPercent * (1 + valueInPercent)) >= 0:
    check['commission'] = 'percentage'
else:
    check['commission'] = 'natural'


def main(check):
    print(check)
    print(type(check))
    match check:
        case {'discount': 'L', 'direction': '1', 'commission': 'percentage'}:
            func = (math.floor(fundsAvailable) / (
                    price * (1 + marketInsuranceValue) * lotSize * discountLong * (1 + valueInPercent)))
        case {'discount': 'L', 'direction': '1', 'commission': 'natural'}:
            func = (math.floor(fundsAvailable) - minValue) / (
                    price * (1 + marketInsuranceValue) * lotSize * discountLong)
        case {'discount': 'S', 'direction': '1', 'commission': 'percentage'}:
            func = (math.floor(fundsAvailable) / (
                    price * (1 + marketInsuranceValue) * lotSize * discountShort * (1 + valueInPercent)))
        case {'discount': 'S', 'direction': '1', 'commission': 'natural'}:
            func = (math.floor(fundsAvailable) - minValue) / (
                    price * (1 + marketInsuranceValue) * lotSize * discountShort)
        case {'discount': 'L', 'direction': '2', 'commission': 'percentage'}:
            func = -- дописать
        case {'discount': 'L', 'direction': '2', 'commission': 'natural'}:
            func = -- дописать
        case {'discount': 'S', 'direction': '2', 'commission': 'percentage'}:
            func = -- дописать
        case {'discount': 'S', 'direction': '2', 'commission': 'natural'}:
            func = -- дописать
    return print(func)


main(check)
