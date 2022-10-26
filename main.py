import json
import math

with open("input/text.json", "r") as file:
    data = json.load(file)


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

lotSize = decaps("lotSize")
marketInsuranceValue = decaps("marketInsuranceValue")

fundsAvailable = decapsMargin("fundsAvailable")
discountShort = decapsMargin("discountShort")
discountLong = decapsMargin("discountLong")
plannedPosition = decapsMargin("plannedPosition")

minValue = decapsCommissionInfo("minValue")
valueInPercent = decapsCommissionInfo("valueInPercent")

price = float(input("Цена заявки"))
discountCheck = input("Short = (S) Long = (L)")
if (discountCheck = "S"):
    discount = discountShort
elif (discountCheck = "L"):
    discount = discountLong


 def answer(formula):
     match formula:
         case 0:
             return math.floor(decapsMargin("fundsAvailable")) / (price * (1 + marketInsuranceValue) * lotSize * discount * (1 + valueInPercent))


formula = ( decapsMargin("fundsAvailable") / (1 + decapsCommissionInfo("valueInPercent"))) - (decapsCommissionInfo("minValue") / decapsCommissionInfo("valueInPercent") * (1 + decapsCommissionInfo("valueInPercent")))