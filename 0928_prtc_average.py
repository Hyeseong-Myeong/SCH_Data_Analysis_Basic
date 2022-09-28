a_score=[49, 80, 20, 100, 80]
b_score=[43, 60, 85, 30, 90]
c_score=[49, 82, 48, 50, 100]

print("[")

for i in range(0,4):
    sum = a_score[i] + b_score[i] + c_score[i]
    print(sum / 3 )
    if i!=4:
        print(", ")
    else:
        print("]")

 