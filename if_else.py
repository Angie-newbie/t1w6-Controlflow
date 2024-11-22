is_raining = False

# if is_raining == True:
#     print("I need a umbrella")
# else:
#     print("Don't need a umbrella")

# print("The End")
# Ternary
print("I need an Umberella" if is_raining else "No need Umbrella")

# >=80 = HD
# 70-79 = D
# 
marks = 53

if marks >= 80:
    print("HD")
elif marks >= 70:
    print("D")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("P")
else:
    print("F")
    
# Nested if 

# 2 stated -> State1 and State2
# State1: >= 18 can vote
# State2: >= 21 can vote

state = "State1"
age = 17

# Display whether they can vote or not
# if (state == "State1" and age >= 18) or (state == "State2" and age >= 21)
if state == "State1":
    if age >= 18:
        print("You can vote in State1")
    else:
        print("Cannot vote in State1")
else:
    if age>= 21:
        print("Can vote in State 2")
    else:
        print("Cannot vote in State2")

day_of_week = 4

# if day_of_week == 1:
#     print("Monday")
# elif day_of_week == 2:
#     print("Tuesday")

match day_of_week:
    # case 1:
    #     print("Monday")
    # case 2: 
    #     print("Tuesday")
    # case 3:
    #     print("Wednesday")
    # case 4:
    #     print("Thursday")
    # case 5:
    #     print(Friday)
    # case _:
    #     print("That is not a weekday")
    case 1|2|3|4|5:
        print("It is a weekday")