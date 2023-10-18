import requests
def get_str(promt:str):
    while 1:
        x = str(input(promt))
        if (x != "EUR" and  x != "USD" and x != "PLN" and x != "exit"):
            print ("Wrong")
        else:
            return x
def get_int(promt:str):
    while 1:
        try:
            return int(input(promt))
        except ValueError:
            print ("Wrong")
def rate(a):
    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    for elem in response.json():
        if elem['cc'] == a:
            return elem['rate']
def result(a, b):
    return a*b
while 1:
    val = get_str("Choise EUR, USD or PLN (exit to leave): ")
    if val == "exit":
        break
    amount = get_int("Amount: ")
    print ("Result ", amount, " ", val, " to UAH = ", result(rate(val), amount))