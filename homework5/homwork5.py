def get_number():
    numlist=list()
    for i in range(30):
        if i%2!=0:
            numlist.insert(i,i)
    return(numlist)
num_list=list(get_number())
if len(num_list)>=5:
    print("Первое:",num_list[0],"\nПятое:",num_list[4],"\nПоследнее:",num_list[-1])
else:
    print("Недостаточно цифр")