peso = float(input("Peso: "))
unidades = input("(K)g ou (L)bs").lower()
k_t_l=2.205
if unidades == "K":
  print("Peso em libras: " + str(peso * k_t_l))
elif unidades == "l":
  print("Peso em kilos: " + str(peso / k_t_l))
else: 
  print("Unidade inválida")
