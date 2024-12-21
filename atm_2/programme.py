import uuid

# Global dictionary to store user data
user_data = {}  # Stores user ID, password, and bank balance


def main():
    while True:
        print("\nWelcome to Razal's ATM")
        print("-----------------------")
        print("1. Insert ATM Card (Create Account)")
        print("2. Login to Your Account")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using Razal's ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def create_account():
    """Function to create a new user account."""
    print("\nCreating a New Account")
    bank_name = input("Enter the name of your bank: ")
    user_id = generate_user_id()
    password = input("Set your ATM password: ")
    initial_balance = float(input("Enter your initial deposit: "))

    # Store user data
    user_data[user_id] = {
        "bank": bank_name,
        "password": password,
        "balance": initial_balance
    }
    print(f"Account created successfully! Your user ID is {user_id}. Keep it safe.")


def generate_user_id():
    """Generate a unique user ID."""
    u = uuid.uuid4()
    return str(u.int)[:6]  # Use the first 6 digits of the UUID


def login():
    """Function to log in to an existing account."""
    print("\nLogin to Your Account")
    user_id = input("Enter your user ID: ")

    if user_id in user_data:
        password = input("Enter your ATM password: ")
        if user_data[user_id]["password"] == password:
            print(f"Welcome back! You are logged into {user_data[user_id]['bank']} account.")
            atm_menu(user_id)
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User ID not found. Please check and try again.")


def atm_menu(user_id):
    """Display ATM menu for logged-in users."""
    while True:
        print("\nATM Menu")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            check_balance(user_id)
        elif choice == "2":
            withdraw_money(user_id)
        elif choice == "3":
            print("Logging out. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


def check_balance(user_id):
    """Display the user's bank balance."""
    balance = user_data[user_id]["balance"]
    print(f"Your current balance is: ₹{balance:.2f}")


def withdraw_money(user_id):
    """Allow the user to withdraw money."""
    amount = float(input("Enter the amount to withdraw: ₹"))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    elif amount > user_data[user_id]["balance"]:
        print("Insufficient funds. Please try a smaller amount.")
    else:
        user_data[user_id]["balance"] -= amount
        print(f"₹{amount:.2f} withdrawn successfully. Your new balance is ₹{user_data[user_id]['balance']:.2f}")


# Run the program
if __name__ == "__main__":
    main()
