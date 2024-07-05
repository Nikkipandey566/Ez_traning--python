weight=int(input())
height=float(input())
BMI=weight/(height*height)
if BMI<18:
    print(0)
elif BMI>=18 and BMI<25:
    print(1)
elif BMI>=25 and BMI<30:
    print(2)
elif BMI>=30 and BMI<40:
    print(3)
elif BMI>=40:
    print(4)
