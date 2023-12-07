# 1



#(ii)
def sum_of_natural_numbers(n):
    if n == 0:
        print(0) 
    else:
        print (n + sum_of_natural_numbers(n - 1))

#test
n = 4
print (sum_of_natural_numbers(n))
print(f"The sum of natural numbers up to {n} is: {result}")



#(iii)
numbers = [1, 3, 5, 7, 9]

# Removing
numbers.remove[2]

# adding 10
numbers[2]= 10

print(numbers)



#iv using a list comprehension, create  a new list that contains only the even numbers from the original list
even_numbers =[2,4,6,8,10]
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in original_list if num % 2 == 0]

print(even_numbers)

#given a dictionary  below , update the value of 'age' to 25 and add a new key-value pair('city','new york') student_info= {'name':'Alice':'age':'A'} 
student_info = {'name': 'Alice', 'age': 'A'}

# Update age to 25
student_info['age'] = 25

# Add a new key-value pair ('city', 'new york')
student_info['city'] = 'new york'


print(student_info)

{'name': 'Alice', 'age': 25, 'city': 'new york'}


#using dictionary conprehension, create a new dictionary with only key-value pairs where the value is greater than 5   original_dict={'a':3,'b':8, 'c':2, 'd':7}


original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}

new_dict = {key: value for key, value in original_dict.items() if value > 5}

print(new_dict)




















