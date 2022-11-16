#Corrida dos tracajás
n = int(input("Quantos tracajás tem no grupo: "))
max = 0
vel = []
i = 0
while (i != n):
  vel.append(int(input("Qual a velocidade do tracajá {}: ".format(i+1))))
  i += 1

for i in range(0, n):
  if vel[i] > max:
    max = vel[i]

print(" ")
if max < 10:
  print("Nível 1")
elif max >= 10 and max < 15:
  print("Nível 2")
elif max <= 15:
  print("Nível 3")
