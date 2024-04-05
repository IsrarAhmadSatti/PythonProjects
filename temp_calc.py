kalvin = float(input('enter value in kalvin: '))
faren = float(input('enter value in faren: '))
degree = float(input('enter value in degrees: '))

kalvin_to_degree = kalvin - 273
faren_to_degree = ((faren - 32) /1.8)
degree_to_faren=((degree * 1.8) +32)

print(kalvin, "kalvin is equal to", round(kalvin_to_degree, 3), " egrees")
print(faren, "faren is equal to", round(faren_to_degree,3), "degrees")
print(degree, "degree is equal to", round(degree_to_faren,3), "farenhite")
