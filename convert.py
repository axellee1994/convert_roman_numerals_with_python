numeric = input("What is the roman numeral you want to input in?")

def roman_to_input(numeric):
    count = 0

    if "CM" in numeric:
        count += 900
        numeric = numeric.replace("CM", "")
    elif "CD" in numeric:
        count += 400
        numeric = numeric.replace("CD", "")
    elif "XC" in numeric:
        count += 90
        numeric = numeric.replace("XC", "")
    elif "XL" in numeric:
        count += 40
        numeric = numeric.replace("XL", "")
    elif "IX" in numeric:
        count += 9
        numeric = numeric.replace("IX", "")
    elif "IV" in numeric:
        count += 4
        numeric = numeric.replace("IV", "")

    for i in numeric:
        if i == "I":
            count += 1
        elif i == "V":
            count += 5
        elif i == "X":
            count += 10
        elif i == "L":
            count += 50
        elif i == "C":
            count += 100
        elif i == "D":
            count += 500
        elif i == "M":
            count += 1000
    print(f'The roman numerals you entered translates to: {count}')

roman_to_input(numeric)

