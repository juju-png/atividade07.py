# Digite um valor e veja quantos dolares voce poderá comprar: R$
real= float(input("digite um valor em real"))
dolar = float(input("digite a cotação do dolar hoje"))

conv= dolar / real

print (f"""
         seu valor em R$ {real}
         cotação atual $ {dolar}
         
         valor da conversão $ {conv}
         
         """)