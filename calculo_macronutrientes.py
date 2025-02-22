if opcao =="3":

    idade = int(input("Digite sua idade  ->    "))
    sexo = input("Digite o seu sexo('h'= Homem/'m'= Mulher)  ->     ")
    peso = float(input("Digite seu peso   ->     "))

    print("Ao digitar idade ela precisa que não contenha o ponto ou virgula. Ex: 145, 171")

    altura = float(input("Digite sua altura   ->     "))

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

# Calculo de metabolismo basal
    #calculo para homem 
    if sexo == "h":
        bmr = (10 * (peso) + 6.25 * (altura) - 5 * (idade) + 5)
    #Calculo para mulher
    elif sexo == "m":
        bmr = (10 * (peso) + 6.25 * (altura) - 5 * idade - 161)

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
        print("Objetivo invalido ERROr:")
    
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