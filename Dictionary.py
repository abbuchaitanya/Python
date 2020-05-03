month_conversion    =   {"Jan":"January",
                         "Feb":"February",
                         "Mar":"March",
                         "jan":"January",
                         "JAN":"January"}

print(month_conversion["Jan"])
print(month_conversion["jan"])
print(month_conversion["Feb"])
print(month_conversion["JAN"])
print(month_conversion.get("Mar"))
print(month_conversion.get("Jul", "Invalid"))