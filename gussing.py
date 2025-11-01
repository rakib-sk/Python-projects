import random
sricred_num = random.randint(1,20)
user_chanc = 1
isWine =  False 
while user_chanc <= 3:
  user_input = int(input("Enter gussing numbar: ")) 
  if user_input == sricred_num:
    print("You are wone!!")
    isWine = True 
    break
  elif user_input > sricred_num:
    print(f"{user_input} is to high")
  else:
    print(f"{user_input} is to low") 
  user_chanc +=1 
if not isWine:
  print(f"You are lose. Computer select {sricred_num}")