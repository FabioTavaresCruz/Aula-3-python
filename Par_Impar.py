quantidade = int(input("Digite quantos números você quer: "))
numero = input("o(s) números deve(m) ser impar ou par? ")

par = 0
impar = -1
loop = 1

if numero.lower() == "par":
    while loop <= quantidade:
        print(par + 2)
        par += 2
        loop += 1
elif numero.lower() == "impar":
     while loop <= quantidade:
         print(impar + 2)
         impar += 2
         loop += 1