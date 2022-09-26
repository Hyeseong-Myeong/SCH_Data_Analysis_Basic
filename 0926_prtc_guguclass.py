num = int(input("구구단 몇 단을 계산할까?"))

print("구구단 ",num,"단을 계산한다.")

for i in range (1, 9, 1):
    print("num x ",i," = ", num * i)