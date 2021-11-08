def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list 

print(biggie_size([-1,1,3,-5]))

def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
            list[-1] = count 
    return list 

print(count_positives([-1,1,1,1]))

def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum 
print(sum_total([1,2,3,4]))

def average (list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)
print(average([1,2,3,4]))

def minimum(list):
    minimum = 0
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i] < minimum:
            minimum = list[i]
    return minimum

print(minimum([37,2,1,-9]))
print(minimum([]))

def maximum(list):
    maximum = 0
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i] > maximum:
            maximum = list[i]
    return maximum

print(maximum([37,2,1,-9]))
print(maximum([]))

def ultimate_analysis(list):
    my_dictionary = {'sumTotal': 0, 'average': 0, 'minimum': list[0], 'maximum': list[0], 'length': len(list)}
    for i in range(len(list)):
        if list[i] < my_dictionary['minimum']:
            my_dictionary['minimum'] = list[i]
        if list[i] > my_dictionary['maximum']: 
            my_dictionary['maximum'] = list [i]
        my_dictionary['sumTotal'] += list[i]
        my_dictionary['average'] = my_dictionary['sumTotal']/len(list)
    return my_dictionary

print(ultimate_analysis([37,2,1,-9]))

def reverse_list(array):
    for i in range(0, (len(array)-1)//2):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array

print(reverse_list([11,12,13]))