# Exercise# 3.1 [Friend's Names];
print("Exercise# 3.1......")
names = ['Abdullah', 'Bilal', 'Taha', 'Ahmad']
print(names[0], "is my friend.")
print(names[1], "is my friend.")
print(names[2], "is my friend.")
print(names[3], "is my friend.")
print(" ")

# Exercise# 3.2 [Greetings];
print("Exercise# 3.2......")
print(f"Hello! {names[0]} I'm very happy to see you here.")
print(f"Hello! {names[1]} I'm very happy to see you here.")
print(f"Hello! {names[2]} I'm very happy to see you here.")
print(f"Hello! {names[3]} I'm very happy to see you here.")
print(" ")

# Exercise# 3.3 [Your Own List];
print("Exercise# 3.3......")
fav_transportation = ['Honda', 'Yamaha', 'RollsRoyce', 'Ferrari']
print(f"I would like to own a {fav_transportation[0]} car.")
print(f"I would like to own a {fav_transportation[1]} bike.")
print(f"I want to bring my procession in {fav_transportation[2]}.")
print(f"I want to buy {fav_transportation[3]} for my mother.")
print(" ")

# Exercise# 3.4 [Guest List];
print("Exercise# 3.4......")
guest_list = ['Ahmad', 'Bilal', 'Taha', 'Abdullah']
print(f"Dear! {guest_list[0]}, You are cordially invited to dinner at my place tonight.")
print(f"Dear! {guest_list[1]}, You are cordially invited to dinner at my place tonight.")
print(f"Dear! {guest_list[2]}, You are cordially invited to dinner at my place tonight.")
print(f"Dear! {guest_list[3]}, You are cordially invited to dinner at my place tonight.")
print(" ")

# Exercise# 3.5 [Changing Guest List];
print("Exercise# 3.5......")
print(f"Unfortunately, {guest_list[1]} can't make it to dinner tonight. So, Furqan take it his place.")
guest_list[1] = "Furqan"
print(f"Dear! {guest_list[0]}, I would be honored if you joined me for dinner.")
print(f"Dear! {guest_list[1]}, I would be honored if you joined me for dinner.")
print(f"Dear! {guest_list[2]}, I would be honored if you joined me for dinner.")
print(f"Dear! {guest_list[3]}, I would be honored if you joined me for dinner.")
print(" ")

# Exercise# 3.6 [More Guests];
print("Exercise# 3.6......")
print("Dear friends good news! We've found a bigger table for more people at dinner. So, that's why i want to call more friends!")
guest_list.insert(0, "Nabeel")
guest_list.insert(3, "Fahad")
guest_list.append("Qasim")
print(f"Dear {guest_list[0]}, you are invited to dinner at our bigger table!")
print(f"Dear {guest_list[1]}, you are invited to dinner at our bigger table!")
print(f"Dear {guest_list[2]}, you are invited to dinner at our bigger table!")
print(f"Dear {guest_list[3]}, you are invited to dinner at our bigger table!")
print(f"Dear {guest_list[4]}, you are invited to dinner at our bigger table!")
print(f"Dear {guest_list[5]}, you are invited to dinner at our bigger table!")
print(f"Dear {guest_list[6]}, you are invited to dinner at our bigger table!")
print(" ")

# Exercise# 3.7 [Shrinking Guest List];
print("Exercise# 3.7......")
print("Dear friends, Due to a delay with my new table, I can only host two guests for dinner. So, i can only invite my brothers.")
print(f"Dear {guest_list.pop()}, I'm really sorry. I can't invite you to at dinner due to a delay with my new table and I can only host two guests for dinner. So, i can invite my brothers only. So, I'll plan another gathering soon and hope you can join then!")
print(f"Dear {guest_list.pop()}, I'm really sorry. I can't invite you to at dinner due to a delay with my new table and I can only host two guests for dinner. So, i can invite my brothers only. So, I'll plan another gathering soon and hope you can join then!")
print(f"Dear {guest_list.pop()}, I'm really sorry. I can't invite you to at dinner due to a delay with my new table and I can only host two guests for dinner. So, i can invite my brothers only. So, I'll plan another gathering soon and hope you can join then!")
print(f"Dear {guest_list.pop()}, I'm really sorry. I can't invite you to at dinner due to a delay with my new table and I can only host two guests for dinner. So, i can invite my brothers only. So, I'll plan another gathering soon and hope you can join then!")
print(f"Dear {guest_list.pop()}, I'm really sorry. I can't invite you to at dinner due to a delay with my new table and I can only host two guests for dinner. So, i can invite my brothers only. So, I'll plan another gathering soon and hope you can join then!")
print(guest_list)
guest_list.__delitem__(0)
guest_list.__delitem__(0)
print("At the end guest list is:", guest_list)
print(" ")

# Exercise# 3.8 [Seeing the World]'
print("Exercise# 3.8......")
country_list = ['Turkey', 'France', 'Germany', 'Dubai', 'Japan']
print("Original list;", country_list)
print("Original list after sorted;", sorted(country_list))
print("Original list after sorted again;", sorted(country_list, reverse=True))
country_list.reverse()
print("Original list after reverse;", country_list)
country_list.reverse()
print("Original list after reverse again;", country_list)
country_list.sort()
print("Original list after sort;", country_list)
country_list.sort(reverse=True)
print("Original list after sort again;", country_list)
print(" ")

# Exercise# 3.9 [Dinner Guests length];
print("Exercise# 3.9......")
print("Length of the guest list is;", len(guest_list))
print(" ")

# Exercise# 3.10 [Every Function];
print("Exercise# 3.10......")
cities = ['Lahore', 'Gujranwala', 'Karachi', ]
print(f"Original list", cities)
cities.append('Multan')
print(f"Original list after append", cities)
cities.insert(2, 'Sialkot')
print(f"Original list after insert", cities)
cities.reverse()
print(f"Original list after reverse", cities)
cities.sort()
print(f"Original list after sort", cities)
print(f"Length of Original list", len(cities))
print(f"Result with index",cities[2])
print(f"Result with positive indexing", cities[0:])
print(f"Result with slicing", cities[0:3])
print(f"Result with positive slicing",cities[0:5:2])
print(f"Result with negative indexing",cities[-6 : -1])
print(f"Result with negative slicing",cities[-6 : -1 : 2])
cities.pop()
print(f"Original list after pop", cities)
cities.remove('Gujranwala')
print(f"Original list after remove", cities)