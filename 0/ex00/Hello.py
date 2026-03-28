ft_list = ["Hello", "tata!"]        # -> World
ft_tuple = ("Hello", "toto!")       # -> France
ft_set = {"Hello", "tutu!"}         # -> Paris
ft_dict = {"Hello" : "titi!"}       # -> 42Paris

## update data struct

#your list

ft_list[1] = 'World'

# tuples are immutable
ft_tuple = ("Hello", "France")

# set
ft_set.remove("tutu!")
ft_set.add("Paris")

# dict
ft_dict = ft_dict | {
            "Hello": "42Paris"
        }

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
