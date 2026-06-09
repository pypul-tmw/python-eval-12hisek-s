def cylinder_volume(radius,height,*,units = "cm^3"):
    return f'{3.14 * (radius ** 2) * height} {units}'


print(cylinder_volume(10, 20))                       # 1256.0 cm^3
print(cylinder_volume(10, 20, units='mm^3'))         # 1256000.0 mm^3
print(cylinder_volume(radius=10, height=20))         # 1256.0 cm^3
print(cylinder_volume(10, height=20, units='mm^3'))  # 1256000.0 mm^3
#print(cylinder_volume(10, height=20, 20))   error