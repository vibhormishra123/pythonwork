


length = float(input('Please Enter the Length of a Cuboid: '))
width = float(input('Please Enter the Width of a Cuboid: '))
height = float(input('Please Enter the Height of a Cuboid: '))


SA = 2 * (length * width + length * height + width * height)

Volume = length * width * height


LSA = 2 * height * (length + width)

print("\n The Surface Area of a Cuboid = %.2f " %SA)
print(" The Volume of a Cuboid = %.2f" %Volume);
print(" The Lateral Surface Area of a Cuboid = %.2f " %LSA)