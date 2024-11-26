import mysql.connector
from getpass import getpass

# Connect to the database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",  # Your MySQL host
        user="root",       # Your MySQL username
        password="password",  # Your MySQL password
        database="atm"    # The ATM database
    )

# Login function
def login(account_number, pin):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE account_number = %s AND pin = %s", (account_number, pin))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Check balance function
def check_balance(account_number):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE account_number = %s", (account_number,))
    balance = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return balance

# Deposit function
def deposit(account_number, amount):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance + %s WHERE account_number = %s", (amount, account_number))
    conn.commit()
    cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s)", 
                   (account_number, "Deposit", amount))
    conn.commit()
    cursor.close()
    conn.close()

# Withdraw function
def withdraw(account_number, amount):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE account_number = %s", (account_number,))
    current_balance = cursor.fetchone()[0]
    
    if current_balance >= amount:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE account_number = %s", (amount, account_number))
        conn.commit()
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, %s, %s)", 
                       (account_number, "Withdraw", amount))
        conn.commit()
        print(f"Withdrawal of {amount} successful.")
    else:
        print("Insufficient balance.")
    
    cursor.close()
    conn.close()

# Transaction history function
def transaction_history(account_number):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT transaction_type, amount, transaction_time FROM transactions WHERE account_number = %s", (account_number,))
    transactions = cursor.fetchall()
    
    print("\nTransaction History:")
    for transaction in transactions:
        print(f"{transaction[0]} of {transaction[1]} at {transaction[2]}")
    
    cursor.close()
    conn.close()

# Main ATM interface
def atm_interface():
    print("Welcome to the Mini ATM!")
    account_number = input("Enter your account number: ")
    pin = getpass("Enter your PIN: ")
    
    user = login(account_number, pin)
    
    if user:
        print("\nLogin successful!")
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                balance = check_balance(account_number)
                print(f"Your current balance is: {balance}")
            
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                deposit(account_number, amount)
                print(f"Deposited {amount} successfully.")
            
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(account_number, amount)
            
            elif choice == '4':
                transaction_history(account_number)
            
            elif choice == '5':
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid account number or PIN.")

# Run the ATM interface
if __name__ == "__main__":
    atm_interface()
