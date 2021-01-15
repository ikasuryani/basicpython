import math

r = input("Jari-jari lingkaran: ")
luas = math.pow(float(r), 2) * math.pi
print("Luas lingkaran dengan jari-jari {0} cm adalah {1:8.2f} cm\u00b2".format(r, luas))