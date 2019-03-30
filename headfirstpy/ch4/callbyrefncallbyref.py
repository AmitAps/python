
#This function doubles the value passed in.
def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ',  arg)

#This function appends a string to any passed in list.
def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)
