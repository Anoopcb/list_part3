## looping in list

## for loop
fruits = ["apple", "banana", "orange", "kiwi"]
for fruit in fruits:
    print(fruit)

## list in lists

numbers = [[1, 2, 3, ], [4, 5, 6, ], [4, 8, 9]]

for number in numbers:
    for i in number:
        print(i)

print(numbers[0][2])
print(type(numbers))



numbers = list(range(2, 21, 2))
print(numbers)
print(numbers.pop())
print(numbers)

###index() method

print(numbers.index(16, 5))


## pass list to a function

def negative_list(l):
    negative = []
    for i in l:

        negative.append(-i)
    return  negative


print(negative_list(numbers))


def negative_list1(l):
    negative = []
    for i in l:

        negative.append(i**2)
    return negative
print(negative_list1(numbers))

print(numbers[::-1])



def reverse_list(l):

    l.reverse()
    return l
print(reverse_list(numbers))

def reverse_list1(l):
    return l[::-1]
print(reverse_list1(numbers))


l1 = [1, 5, 8, 9, 6 , 6]
def reverse_list2(l):

    r_list= []
    for i in range(len(l)):

        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

print(reverse_list2(l1))
print(reverse_list2(numbers))


name= ["abc", "def", "acd"]
def reverse_list2(l):

    r_list= []
    for i in range(len(l)):

        popped_item = l.pop()
        r_list.append(popped_item[::-1])
    return r_list
print(reverse_list2(name))



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def filter_odd_even(l):

    odd_num = []
    even_num=[]

    for i in l:
        if i%2==0:
            even_num.append(i)
        else:

            odd_num.append(i)
    output = [odd_num, even_num]
    return  output

print(filter_odd_even(nums))


nums1 = [1, 2, 5, 8, 7]

def common_finder(l1, l2):

    output1 = []
    for i in l1:

        if i in l2:
            output1.append(i)
    return output1

print(common_finder(nums, nums1))



print(min(nums1))
print(max(nums1))

## function for finding how many list in a list are

def sublist_counter(l):

    count = 0

    for i in l:

        if type(i)==list:

            count+=1
    return count
nums2 = [1, 2, 3, [1, 2, 5, 4], [1, 2]]
print(sublist_counter(nums2))










