altura=1.80
peso=80.135
print("Tu altura es ",altura,"y tu peso es ",peso)
print(f'Tu altura es {altura} y tu peso es {peso}')
print("tu altura es {0} y tu pes es de {1} kologramos".format(altura,peso))
print("tu altura es {a} metros y tu peso es de {p} kilogramos".format(a=altura,p=peso))


n=(input("Introduce un número "))
print(str(n).zfill(6))
m=float(input("Introduce otro número: "))
print(str(m).zfill(7),"{:3f}".format(m))
