
products = ["молоко", "кефир", "масло", "мясо", "сыр", "хлеб", "помидоры","йогурт" ]

count = len(products)

for i in products:
    if len(i)%2==0:
        print(i)


print(f"У тебя {count} продуктов, где {count} - значение переменной count.")