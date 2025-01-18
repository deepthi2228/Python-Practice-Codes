li1 = [1,2,3,4,5]
print(li1) #[1,2,3,4,5]
sq_list = []
for i in li1:
    sq_list.append(i**2)
print(sq_list) #[1,4,9,16,25]

li = [1,2,3,4,5]
duplicate_li = [i for i in li]
#When we have only if part then write it after for loop.
even = [i for i in li if i%2 == 0]
sq_list = [i ** 2 for i in li]
new_li = [ele + 2 for ele in li]

# When we have if-else both write it before for loop.
even_odd = ['Even' if i%2 == 0 else 'Odd' for i in li]

#Multiple Nested for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]

