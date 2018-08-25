
napis = input("Podaj jakis napis z wyrazem w nawias <>: ")

l_ind = napis.find('<')
r_ind = napis.find('>')

# print(l_ind, r_ind)
ile = r_ind - l_ind - 1
print(ile)
