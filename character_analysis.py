#
# Character Analysis
# Reads and counts each character in the file
# Input(s)
#  text.txt
#
# Output
#  uppercase_count, lowercase_count, digit_count, whitespace_count


def main():
    # User knows what the program does
    print("This program reads the file and counts the characters in the file.")
    print()

    # The file
    user_file = 'text.txt'

    # Each type of character count
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    whitespace_count = 0
    
    try:
        # Open the file and read it
        with open(user_file, 'r') as file:
            content = file.read()
            
            # Checks through each character in the file
            for character in content:
                if character.isupper():
                    uppercase_count += 1
                elif character.islower():
                    lowercase_count += 1
                elif character.isdigit():
                    digit_count += 1
                elif character.isspace():
                    whitespace_count += 1
        
        # Display the results
        print('=' * 30)
        print('Characters\t\t Count')
        print('-' * 30)
        print(f'Uppercase letters:\t {uppercase_count}')
        print(f'Lowercase letters:\t {lowercase_count}')
        print(f'Digits:\t\t\t {digit_count}')
        print(f'Whitespace:\t\t {whitespace_count}')
        print('=' * 30)
    
    except FileNotFoundError:
        print(f"<<< ERROR: The file '{user_file}' does not exist. ")
    except IOError:
        print(f"<<< ERROR: An error occurred while reading the file '{user_file}'. ")
    except Exception as e:
        print(f"<<< Something went wrong: {e} >>>")
    
    # Display end, let user know
    print()
    print("Program ends.")

# Call main function
main()
