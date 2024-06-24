import random
import time
while 1:
    try:
        passage = eval(input("请输入要生成几篇口算:"))
        tittel_Rep = str(input("请输入输出文件标题:"))
        try:
            number = eval(input("请输入口算大小（0~？）:"))
            tittel = str(tittel_Rep + ".txt")
            try:
                open(tittel,"x")
                t = open(tittel, 'w', encoding='utf-8')   
                for x in range(passage):
                    for y in range(25):
                        first = str(random.randint(0, number))
                        second = str(random.randint(0, number))
                        out1 = str(first + "+" + second)
                        out2 = str(first + "-" + second)
                        out3 = str(first + "*" + second)
                        out4 = str(first + "/" + second)
                        t.write(out1 + "=     ")
                        t.write(out2 + "=     ")
                        t.write(out3 + "=     ")
                        t.write(out4 + "=     \n")
                    t.write("完成一篇\n")
                t.write("全部完成\n   ")
                t.close()
                finish = eval(input("是否结束（输入“1”结束）:"))
                if finish == 1:
                    break
            except FileExistsError as e:# python 3 以后用 as 链接
                print("文件重复，请换一个标题")
        except NameError as e1:# python 3 以后用 as 链接
            print("请勿输入字符串")
    except NameError as e1:# python 3 以后用 as 链接
        print("请勿输入字符串")
