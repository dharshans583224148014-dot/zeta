print("WELCOME TO THE EVEN AND ODD NUMBER CHECKER!!")
print("Type 'exit' anytime you want to stop.")

while True:
  #Take an input from the user
  user_input = input("Enter your number:").strip()
  
  #Exit Condition
  if user_input.lower() == "exit":
    print("GoodBye!! Thank you for using the program.")
    break
    
  #Check if the provided number is even 
  if user_input.isdigit():
    num = int(user_input)
    if(num %2 == 0):
      print(num, "is an even number")
    else:
      print(num,"is an odd number")
  else:
    print("Invalid! Please enter a valid number or type exit.")
