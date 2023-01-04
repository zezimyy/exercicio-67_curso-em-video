n_digitado = 1
n_tabuada = 1
resultdo = 1
loop = True
loop2 = True

while loop == True:
  n_digitado = int(input("Digite um numero para ver a sua tabuada: "))
  loop2 = True
  loop = True
  n_tabuada = 1
  
  if n_digitado < 0:
    break
  
  while loop2 == True:
    resultdo = n_digitado * n_tabuada
    print("{} x {} = {}".format(n_digitado, n_tabuada, resultdo))
    n_tabuada +=1
    if n_tabuada == 11:
      loop2 = False