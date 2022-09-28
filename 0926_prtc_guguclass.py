num = int(input("구구단 몇 단을 계산할까?"))

print("구구단 ",num,"단을 계산한다.")

assert(1 <= num) & (num < 10), f"입력된 값: {num}. 1~9값만 입력."

for i in range (1, 9, 1):
    print(num,"x ",i," = ", num * i)