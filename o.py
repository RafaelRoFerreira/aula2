#Interação usuário
while True:
    try:
        n1= int(input("Digite um numero:"))
        n2= int(input("Digite um segundo numero:"))
       
    except ValueError:
            print("digite apenas numeros")
            continue
    break
opr= input("Qual operação? (+,-,*,/):")


#Calculadora
elif opr == "*":
     print("seu resultado é:", str(n1 * n2))
elif opr == "/":
    print("seu resultado é:", str(n1 / n2))

     










