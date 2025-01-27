name1_lower = input("Enter First person name. ").lower()
name2_lower = input("Enter Second person name. ").lower()

t_count = name1_lower.count("t")
r_count = name1_lower.count("r")
u_count = name1_lower.count("u")
e_count = name1_lower.count("e")
true_count = t_count + r_count + u_count + e_count

l_count = name2_lower.count("l")
o_count = name2_lower.count("o")
v_count = name2_lower.count("v")
e2_count = name2_lower.count("e")
love_count = l_count + o_count + v_count + e2_count

total_count = int(str(true_count) + str(love_count))

#I learned to convert the above to string, and then back to integer 
# from Dr. Yu, didn't have this initially
# perhaps I need to do the same above to true_count and love_count?

if total_count <= 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count >= 40 and total_count <= 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
