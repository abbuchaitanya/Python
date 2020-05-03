car_brands  =   ["Ford", "Merc", "Audi", "Citroen", "Maruti", "Suzuki", "Vauxhall", "Tata"]
car_years   =   ["1890", "1945", "1963", "1995", "1970", "1965", "1987", "1983", "1996"]

print(car_brands)
print(car_years)

car_brands.extend(car_years)
print(car_brands)

car_brands.append("Hyundai")
print(car_brands)

car_brands.insert(3, "Honda")
print(car_brands)

car_brands.remove("Hyundai")
print(car_brands)

car_brands.pop()
print(car_brands)

car_years.clear()
print(car_years)

print(car_brands.index("Merc"))

car_years   =   [1890, 1945, 1963, 1995, 1983, 1970, 1965, 1987, 1983, 1996]

print(car_years.count("1983"))

car_years.sort()
print(car_years)

car_years.reverse()
print(car_years)

car_years2  =   car_years
print(car_years2)

car_brands2  =   car_brands.copy()
print(car_brands2)