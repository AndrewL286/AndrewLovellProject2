years = []
averages = []

file = open('Project2.txt', 'r', encoding='utf-8')
file.readline()
for line in file:
        parts = line.split(";")
        year = parts[0].split("-")[0]
        income = float(parts[1])
        house_price = float(parts[2])
        ratio = (house_price / income)
        years.append(year)
        averages.append(ratio)
        print(f"{year}'s house price to income raio was {ratio:.2f}.")