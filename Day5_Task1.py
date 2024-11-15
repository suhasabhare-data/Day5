class MathFunc:
    def aDDFun(*args):
        total2 = 0
        for i in args:
            total2 += i
        return total2
    def MultiFun(*args):
        total3 = 1
        for i in args:
            total3 = total3 * i
        return total3
    def DiviFunction(*args,n=2):
        n = int(input("Enter Division number"))
        total4 = []
        for i in args:
            i2 = i / n
            total4.append(i2)
        return total4
    def SubFunc(*args,n=0):
        total5 = 0
        n = int(input("Enter number to subtract"))
        print("Number entered is :",n)
        if n != None:
            for i in args:
                total5 = total5-n
        return total5
    def MeanFun(*args):
        MeanArgs = sum(args)/len(args)
        return MeanArgs
    def ModFun(*args):
        global num2
        num2 = {}
        for i in set(args):
            num2[i] = args.count(i)
        max_count = {k for (k,v) in num2.items() if v == max(num2.values())}
        print(max_count)
    def MedianFun(*args):
            n1 = len(args)
            args1 = list(args)
            args1.sort()
            if n1 % 2 == 0:
                median1 = args1[n1//2]
                median2 = args1[n1//2-1]
                median3 = (median1 + median2)/2
            else:
                median3 = args1[n1//2]
            print(median3)
    def PercentileCal(*args):
        percent = input("enter percentile from 75,50,25")
        if percent == '75':
            print(sum(args)*75/100)
        if percent == '50':
            print(sum(args)*50/100)
        if percent == '25':
            print(sum(args)*25/100)

            

        
print(MathFunc.aDDFun(5,4,3,2))
print(MathFunc.MultiFun(5,4,3,2))
print(MathFunc.DiviFunction(5,4,3,2))
print(MathFunc.SubFunc(5,4,3,2))
print(MathFunc.MeanFun(5,4,3,2))
print(MathFunc.ModFun(5,4,3,2,2,2,1))
print(MathFunc.MedianFun(9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25))
print(MathFunc.PercentileCal(9, 10, 12, 13, 13))
