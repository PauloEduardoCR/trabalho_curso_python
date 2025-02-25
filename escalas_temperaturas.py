
print("        Transformador de Temperatura | °C  | °F  | K  |")
print("")

#Escalas de temperatura, celsius, fahrenheit, kelvin.
escala_Temperatura = ["    c => °Celsius",
                      "    f => °Fahrenheit",
                      "    k => °Kelvin",
                      ]

for lista_temperatura in escala_Temperatura:
    print(lista_temperatura)
print("")

temperatura = float(input("Diga a temperatura ->   "))
opcao_1 = input("Digite qual a escala de temperatura c/f/k->    ").strip().lower()
opcao_2 = input("Para qual escala de temperatura transformar a opção anterior ? ->    ").strip().lower()

#Calculo de Celsius para Fahrenheit.
if opcao_1 =="c" and opcao_2 =="f":
    fahrenheit = (temperatura * 1.8) + 32
    print("  {}° graus celsius é  {:.2f}° fahrenheit".format(temperatura,fahrenheit))

#Calculo de Celsius para Kelvin.
elif opcao_1 =="c" and opcao_2 =="k":
    kelvin = (temperatura + 273.15)
    print("  {}°  celsius é  {:.2f}° Kelvin".format(temperatura,kelvin))

#Calculo de Fahrenheit para Celsius.
elif opcao_1 =="f" and opcao_2 =="c":
    celsius = (temperatura - 32)/1.8
    print("  {}°  fahrenheit é  {:.2f}° Celsius" .format(temperatura,celsius))

#Calculo de Fahrenheit para Kelvin.
elif opcao_1 =="f" and opcao_2 =="k":
    fahrenheit_kelvin = (temperatura - 32) * 5/9 + 273.15
    print("  {}°  fahrenheit é  {:.2f}° Kelvin".format(temperatura,fahrenheit_kelvin))

#Calculo de Kelvin para Fahrenheit.
elif opcao_1 =="k" and opcao_2 =="f":
    kelvin_fahrenheit = (temperatura - 273.15) * 1.8 + 32
    print("  {}°  Kelvin é  {:.2f}° Fahrenheit".format(temperatura,kelvin_fahrenheit))
    
#Calculo de Kelvin para Celsius
elif opcao_1 =="k" and opcao_2 =="c":
    kelvin_celsius = (temperatura - 273.15)
    print("  {}°  Kelvin é  {:.2f}° Celsius".format(temperatura,kelvin_celsius))
else:
  print("      !   Transformação Invalida, tente novamente e lembre-se de usar apenas c/f/k")
