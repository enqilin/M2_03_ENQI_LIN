n=int(input("Introduce un número: "))
print(str(n).zfill(5))
m=float(input("Introduce otro número: "))
print(str(m).zfill(7),"{:3f}".format(m))