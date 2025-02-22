# criar conta de usuario
# mostrar conta do usuario
# calcular imc do usuario
# dica do dia 
# registrar treinos
# saida



def verMenu():
        
    print("+{}+".format("-"*50))
    print("|{:^50}|".format("Menu Principal"))
    print("+{}+".format("-"*50))
    print("|1-criar conta de usuario{}|".format(" "*26))
    print("|2-mostrar conta do usuario{}|".format(" "*24))
    print("|3-calcular macronutrientes do usuario{}|".format(" "*25))
    print("|4-calcular IMC do usuario{}|".format(" "*37))
    print("|5-registrar treinos{}|".format(" "*31))
    print("|6-saida{} |".format("  "*21))
    print("+{}+".format("-"*50))
 
def calcularIMC(peso,altura):


    return peso/(altura**2)
    



print("{:^550}".format("SEJA BEM-VINDO"))
infoUser = {}

while True:
    verMenu()
    print("\n")
    opcao = (input(f"{' ':^35}Digite a opção desejada: "))
    if opcao =="1":
        print("\n")
        print("{}".format("="*50))
        print("{:^50}".format("Cadastro Usuario"))
        print("{}".format("="*50))

        nome = input("Nome: ")
        sexo = input("h = Homem / m = Mulher :  ")   
        idade = input("Digite sua idade:  ")
        peso = float(input("Peso (kg):  "))
        altura = float(input("Altura (m):  "))
        infoUser = {'nome':nome,"sexo":sexo,"idade":idade,'peso':peso,'altura':altura}        
    elif opcao == "2":
        print("{}".format("="*50))
        print("{:^50}".format("informacoes do Usurario"))
        print("{}".format("="*50))


        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Peso (kg): {peso:.2f}")
        print(f"Altura (m): {altura:.2f}")

    elif opcao == "3":

        print("")

        print("|=================================================================================|")
        print("|   Nivel       |   classificação   |     Tempo de exercicio (Semanais)           |")
        print("|_________________________________________________________________________________|")
        print("|  -> Nivel 1   |   Sedentario      |        <150 minutos semanais                |")
        print("|_________________________________________________________________________________|")
        print("|  -> Nivel 2   |   Pouco Ativo     |        Entre 150 e 300 minutos semanais     |")
        print("|_________________________________________________________________________________|")
        print("|  -> Nivel 3   |   Muito ativo     |        >300 minutos semanais                |")
        print("|=================================================================================|")

        print("")

        print("Digite o numero 1, 2 ou 3")
        nivel_Sedentarismo = input("Diga Qual seu nivel de sedentarismo  ->     ")

        print("")

        print("1 => Manter")
        print("2 => Perder Peso")
        print("3 => Ganhar Peso")

        print("Digite o numero 1, 2 ou 3")
        objetivo = float(input("Qual seu objetivo   ->    "))
    #Calculo para transformar altura de metros em centimetros.
        altura_cm = int(altura *100)

    # Calculo de metabolismo basal
        #calculo para homem 
        if sexo == "h":
            bmr = (10 * (peso) + 6.25 * (altura_cm) - 5 * (idade) + 5)
        #Calculo para mulher
        elif sexo == "m":
            bmr = (10 * (peso) + 6.25 * (altura_cm) - 5 * idade - 161)

    # Calculo do gasto calorico total diario (TDEE)
        if nivel_Sedentarismo == "1":
            tdee = (bmr * 1.2)
        elif nivel_Sedentarismo == "2":
            tdee = (bmr * 1.375)
        elif nivel_Sedentarismo == "3":
            tdee = (bmr * 1.55)


    #Calculo para distribuiçao de macronutrientes de acordo com o objetivo

        percentual_proteina = 0
        percentual_carboidrato = 0
        percentual_gordura = 0

        if objetivo ==1:
            percentual_proteina = 0.25
            percentual_carboidrato = 0.50
            percentual_gordura = 0.25
        elif objetivo ==2:
            percentual_proteina = 0.30
            percentual_carboidrato = 0.40
            percentual_gordura = 0.30
        elif objetivo ==3:
            percentual_proteina =0.30
            percentual_carboidrato =0.50
            percentual_gordura = 0.20
        else:
            print("Objetivo invalido  ERROr:     Digite apenas 1, 2 ou 3.")
        
    #Calculadora de de calorias para cada macronutrientes
        calorias_proteinas = ( tdee * percentual_proteina )
        calorias_carboidratos = ( tdee * percentual_carboidrato)
        calorias_gorduras = ( tdee * percentual_gordura)

    #Converter calorias para gramas.

        gramas_proteina = (calorias_proteinas /4)
        gramas_carboidratos = (calorias_carboidratos /4)
        gramas_gordura = (calorias_gorduras /9)

        if objetivo ==1:
            print("A distribuição de macronutrientes diario para o seu objetivo de manter o peso é:")
            print("")
            print("Proteinas:    gramas {:.2f}, calorias {:.0f}".format(gramas_proteina,calorias_proteinas))
            print("Carboidratos: gramas {:.2f}, calorias {:.0f}".format(gramas_carboidratos,calorias_carboidratos))
            print("Gordura:      gramas {:.2f}, calorias {:.0f}".format(gramas_gordura,calorias_gorduras))
            print("")
        elif objetivo ==2:
            print("A distribuição de macronutrientes diario para o seu objetivo de perder peso é:")
            print("")
            print("Proteinas:    gramas {:.2f}, calorias {:.0f}".format(gramas_proteina,calorias_proteinas))
            print("Carboidratos: gramas {:.2f}, calorias {:.0f}".format(gramas_carboidratos,calorias_carboidratos))
            print("Gordura:      gramas {:.2f}, calorias {:.0f}".format(gramas_gordura,calorias_gorduras))
            print("")
        elif objetivo ==3:
            print("A distribuição de macronutrientes diario para o seu objetivo de ganhar peso é:")
            print("")
            print("Proteinas:    gramas {:.2f}, calorias {:.0f}".format(gramas_proteina,calorias_proteinas))
            print("Carboidratos: gramas {:.2f}, calorias {:.0f}".format(gramas_carboidratos,calorias_carboidratos))
            print("Gordura:      gramas {:.2f}, calorias {:.0f}".format(gramas_gordura,calorias_gorduras))
            print("")
    elif opcao == "4":
        imc = calcularIMC(peso,(altura))

        print(" ")

        print("    ->  {}, Seu Indice de Massa Corporal é   | {:.2f} |" .format(nome, imc))

        print("")

        if imc <16:
            print("    -> Atenção {}! Você está com magreza grave".format(nome))
        elif  16<= imc < 17:
            print("    -> {} Você está com magreza moderada".format(nome))
        elif  17<= imc <18.5:
            print("    ->  {} Você está com magreza leve".format(nome))
        elif 18.5<= imc <25:
            print("    -> {} Que bom! Você está saudável".format(nome))
        elif 25<= imc <30:
            print("    -> {} Você está com sobrepeso".format(nome))
        elif 30<= imc <35:
            print("    -> ATENÇÃO {}! Você está com obesidade grau 1" .format(nome))
        elif 35<= imc <40:
            print("    -> ATENÇÃO {}! Você está com obesidade grau 2".format(nome))
        elif imc >40:
            print("    -> ATENÇÃO {}! Você está com obesidade grau 3".format(nome))
         

    elif opcao == "5":
        ...
    elif opcao == "6":
        ...

   