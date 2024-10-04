def square(boolean,size):
    if boolean == True:
        for i in range(size):
            print('* '*size)
    else:
        for i in range(size):
            if i == 0 or i == size-1:
                print('* '*size)
            else:
                print('* '+'  '*(size-2)+'*')


square(True,5)
