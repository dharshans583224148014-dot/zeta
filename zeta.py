def reverse_list(user_input):
    reverse = user_input[len(user_input):0:-1]
    reverse = reverse + user_input[0]
    return reverse
def main():

    while True:
        user_input = input("Enter a word: ")
        reverse = reverse_list(user_input)
        if reverse == user_input:
            print("It's a Palindrome!")
            print(reverse)
        else:
            print("It's not a Palindrome")
            print(reverse)
            break
if __name__ =="__main__":
    main()
