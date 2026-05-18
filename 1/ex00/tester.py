from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# my tests

print("My tests:")
bmi_list = [18.5, 22.0, 27.3, 31.0]
result = apply_limit(bmi_list, 25)
print(result)
