profile = {'f_name':'Catherine', 'l_name':'Ivelia', 'age':60}
for key in profile.items():
    print(key[0], ":", key[1])

profile.setdefault('city','NRB')
print(profile)
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
odd_indices = list1[1::2]
even_indices = list2[0::2]
print(odd_indices)
print(even_indices)
new_list = odd_indices + even_indices
print(new_list)
print(odd_indices.append(even_indices))