name1 = input("enter your name: ").lower()
name2 = input("enter the name of yout love: ").lower()
cname = name1 + name2
true = str(cname.count("t") + cname.count("r") + cname.count("u") + cname.count("e"))
love = str(cname.count("l") + cname.count("o") + cname.count("v") + cname.count("e"))

score = true + love
if score <= '10' or score >= '90':
 print(f"your score is {score}. you go like coke and mentos.")
elif score >= '40' and score <= '50':
 print(f"your score is {score}. you are alright together.")
else:
 print(f"your score is {score}")


