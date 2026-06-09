def calculated_discount(price, discount_percentage):
    return price - (price * discount_percentage/100)

discounted_price = calculated_discount(100,10)
print(discounted_price)