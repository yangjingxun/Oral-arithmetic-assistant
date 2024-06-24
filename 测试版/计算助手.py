import random
while 1:
    passage = eval(input("请输入要生成几篇口算:"))
    number = eval(input("请输入口算大小（0~？）:"))
    for x in range(passage):
        for y in range(25):
            first = random.randint(0, number)
            second = random.randint(0, number)           
            print(first,"+", second,"     ",first,"-", second,"     ",first,"*", second,"     ",first,"/", second)
        print("完成一篇")
    print("全部完成")
    print("\
    ")

                 
