
def countdown (num):
    my_list = []
    for i in range (num,-1,-1):
        my_list.append(i)
    return my_list

print(countdown(5))

def print_and_return(x,y):
    print (x)
    return y

print(print_and_return(1,2))

def first_plus_length(my_list):
    return (my_list[0]) + len(my_list)

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    new_list =[]
    for i in list:
        if i > list[1]:
            new_list.append(i)
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))


def length_and_value(size, value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list

print(length_and_value(4,7))