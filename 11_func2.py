def date_to_day_month_year(date):
    day, month, year = date.split("-")
    return day, month, year

day, month, year = date_to_day_month_year("26-2-2026")
print("Day:",day)
print("Month:",month)
print("Year:",year)