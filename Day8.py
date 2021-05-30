
#python does not have buit-in array. we should import an array from a library like NumPy or array.
#Arrays are used as container. array is meant to be for type elements but we could add different types to an array.
#Arrays are specially optimized for arithmetic computations.
#Array is mutable

# from array import array
# intarray = array('i')
# print(type(intarray))
#
# x = array ('f',[3,6,9,12])
# print(x)

#we use List instead of array in python
#the main difference between Array and List  is the operation we can perform on them
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# numbers = even + odd
# print("before sorting " + str(numbers) )
# #sort() function modifies list and has NO RETURN VALUE
# numbers.sort()
# print("after sorting " + str(numbers) )
# #the sorted() function will create a new list containing a sorted version of my list given to it
# numbers_in_order = sorted(numbers )
# print(numbers_in_order)




#lets check deeper if the 2 lists are equal
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# numbers = even + odd
# numbers_in_order = sorted(numbers)
# print(numbers )
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("the lists are equal")
# else:
#     print("the lists are NOT equal")



# print("-----Student1 after sorting")
# Student1 = ["Singh","Kaur","Balba"]
# Student1.sort()
# print(Student1)
# print("-----Student2 after sorting")
# Student2 = ["Peykan","Aria","Hilman","John"]
# Student2.sort()
# print(Student2)
#
# for x in Student2:
#     print(x)
#
# print("----Students before sorting--------")
# Students = Student1 + Student2
# print(Students)
# print("----Students after sorting------")
# Students.sort()
# print(Students)
# print("-----Students after appending dara------")
# Students.append('dara')  #it works by ascii code ....
# Students.sort()
# print(Students)



# list_1 = []
# list_2 = list()
# print(type (list_1))
# print(type (list_2))
#
# print("List 1 : {}".format(list_1))
# print("List 2 : {}".format(list_2))
#
# if list_1 == list_2:
#     print("the lists are equal")
#
# print(list("the lists are equal"))



# even = [2,4,6,8]
# another_even = even
# even_copy = even.copy()
# another_even.sort(reverse=True)
# print(even)
# print(even_copy)
# print(another_even is even)
# print(even is even_copy)


# even = [2,4,6,8]
# another_even = even
# sorted_another_even = sorted(another_even,reverse=True)
# print("even: {}".format(even))
# print("sorted_another_even: {}".format(sorted_another_even))
# print("another_even is sorted_another_even", another_even is sorted_another_even)

# even = [2,4,6,8]
# another_even = list(even)
# print(even)
# print(another_even is even)
# print(another_even)
# another_even.sort(reverse=True)
# print(another_even)
# print(even)




# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# numbers = even + odd
# print(numbers )
# numbers = [even,odd]
# print(numbers)
#
# print("--first dimension---" )
# for number_set in numbers:
#     print(number_set)
#
# print("--second dimension---")
# for number in numbers:
#     for value in number:
#         print(value, end=" ")
#     print()



# menu = []
# menu.append(["egg","spam","bacon"])
# menu.append(["egg","sausage","bacon"])
# menu.append(["egg","spam"])
# menu.append(["egg","bacon","spam"])
# menu.append(["egg","bacon","sausage","spam"])
# menu.append(["spam","bacon","sausage","spam"])
# menu.append(["spam","egg","spam","spam", "bacon","spam"])
# menu.append(["spam","egg","sausage","spam"])
# print(menu)


#finding a meal without spam
# new_menu =[]
# myFlag = 1
# for meal in menu:
#     myFlag = 1
#     for ingredient in meal:
#         if ingredient == "spam":
#             myFlag=0;
#     if myFlag == 1:
#         new_menu.append(meal)
#
# for meal in new_menu:
#     print(meal)
#
# for ingredient in meal:
#     print(ingredient)

#finding a meal without spam: trying second solution
# print("----second solution------")
# for meal in menu:
#     if not "spam" in meal:
#         print(meal)
# #give me all ingredients for each menu
# for ingredient in menu:
#     for x in ingredient:
#         print(x,end=" ")
#     print()



