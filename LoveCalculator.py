print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_lower_case = name1.lower()
name2_lower_case = name2.lower()
# name1_lower_case=name1_lower_case.replace(" ", "")
# name2_lower_case=name2_lower_case.replace(" ", "")

both_names = (name1_lower_case + name2_lower_case)
t_counter = both_names.count("t")
r_counter = both_names.count("r")
u_counter = both_names.count("u")
e_counter = both_names.count("e")
true_counter=t_counter+r_counter+u_counter+e_counter

l_counter = both_names.count("l")
o_counter = both_names.count("o")
v_counter = both_names.count("v")
e_counter = both_names.count("e")
love_counter = l_counter+o_counter+v_counter+e_counter
score =int((f"{true_counter}{love_counter}"))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score} .means mehh")
