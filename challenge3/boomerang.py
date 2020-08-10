def numBoom(lst):
        boomerLst = []
        counter = 0
        for i in range(len(lst)):
                if len(lst) < 3:
                        return False
                elif (lst[i] == lst[i+2]) and (lst[i+1] != lst[i]): 
                        boomerLst.append([i,i+1,i+2])
                        counter +=1
                        if counter >= len(lst) // 3:
                                break
        print(boomerLst)
        return len(boomerLst)

boom = [9,5,9,5,1,1,1]
print(numBoom(boom))
