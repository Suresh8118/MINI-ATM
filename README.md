# MINI-ATM
# Mini ATM System

## Overview
The **Mini ATM System** is a simple simulated banking system that allows users to perform basic banking transactions such as checking balances, making deposits, withdrawing money, and viewing transaction history. This project uses **Python** for the application logic and **MySQL** as the database to store user information and transaction records.

## Features
- **User Login**: Secure login using account number and PIN.
- **Check Balance**: View the current balance in the user's account.
- **Deposit**: Deposit money into the user's account.
- **Withdraw**: Withdraw money from the user's account (with balance validation).
- **Transaction History**: View the transaction history (list of all deposits and withdrawals).
- **ATM System Simulation**: Command-line interface (CLI) to interact with the system.

## Technologies Used
- **Python**: Main programming language for the system logic.
- **MySQL**: Database management system for storing user and transaction data.
- **MySQL Connector**: Python library to connect and interact with the MySQL database.
- **CLI (Command-Line Interface)**: Simple text-based user interface.

## Requirements
- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)

## Setup and Installation

###1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/Suresh8118/MINI-ATM/edit/main/README.md#mini-atm
cd mini-atm-project
2. Install Python and MySQL Dependencies
You need to install the required Python packages. Use the following steps:

Install Python Dependencies:
Create a virtual environment (optional, but recommended for project isolation):

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required Python libraries:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file, you can manually install the MySQL Connector by running:

bash
Copy code
pip install mysql-connector-python
Install MySQL Server
Make sure you have MySQL installed on your machine. You can download MySQL from the official website: MySQL Downloads.
3. Set Up MySQL Database
Create Database: Open MySQL and create the atm database:

sql
Copy code
CREATE DATABASE atm;
USE atm;
Create Tables: Run the following SQL commands to create the users and transactions tables:

sql
Copy code
-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    pin VARCHAR(20) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0
);

-- Create transactions table
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20),
    transaction_type VARCHAR(50),
    amount DECIMAL(10, 2),
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255) DEFAULT 'No description',
    status VARCHAR(50) DEFAULT 'Successful'
);
Insert Sample Data (optional): You can insert some sample users and transactions into the tables for testing:

sql
Copy code
-- Insert sample users
INSERT INTO users (account_number, pin, balance)
VALUES 
('1234567890', '1234', 5000.00),
('9876543210', '5678', 1500.50),
('1112223333', '4321', 2500.75);

-- Insert sample transactions
INSERT INTO transactions (account_number, transaction_type, amount, description, status)
VALUES 
('1234567890', 'Deposit', 1000.00, 'ATM Deposit', 'Successful'),
('9876543210', 'Withdraw', 500.00, 'ATM Withdrawal', 'Successful'),
('1112223333', 'Deposit', 1500.00, 'Bank Transfer', 'Successful'),
('1234567890', 'Withdraw', 200.00, 'ATM Withdrawal', 'Successful');
4. Update Database Connection Settings
Make sure to update the MySQL connection settings in the Python code, such as the host, user, password, and database name. You can do this in the connect_to_db() function of the main Python script.

python
Copy code
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",      # Your MySQL host (usually localhost)
        user="root",           # Your MySQL username
        password="password",   # Your MySQL password
        database="atm"         # The name of the database
    )
5. Running the Application
Run the Python script to start the ATM simulation:

bash
Copy code
python atm_system.py
6. Using the ATM System
Once the application is running, you will be prompted to log in with an account number and PIN. After logging in successfully, you will be presented with options to check your balance, deposit money, withdraw money, or view your transaction history.

Example Interaction
markdown
Copy code
Welcome to the Mini ATM!
Enter your account number: 1234567890
Enter your PIN: ********

Login successful!

1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Choose an option: 1
Your current balance is: 5000.00

1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Choose an option: 4

Transaction History:
Type            Amount     Date & Time            Description                  Status
----------------------------------------------------------------------------------------------------
Deposit         1000.00    2024-11-27 10:05:32    ATM Deposit                 Successful
Withdraw        200.00     2024-11-27 09:20:15    ATM Withdrawal              Successful
Withdraw        500.00     2024-11-26 18:15:00    ATM Withdrawal              Successful
Deposit         1500.00    2024-11-26 08:00:00    Bank Transfer               Successful
Contributing
Feel free to fork this repository and submit pull requests. If you find any bugs or issues, please report them via the Issues section.

License
This project is licensed under the MIT License - see the LICENSE file for details.
