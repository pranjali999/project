from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import Config
app = Flask(__name__)

app.config.from_object(Config)
mysql = MySQL(app)
class Customer:
    def __init__(self, customer_id, name, address, phone_number, email):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.accounts = []  # A list to store multiple accounts the customer has

    def add_account(self, account):
        self.accounts.append(account)

    def view_balance(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: ${account.balance}")
    
    def deposit(self, account, amount):
        account.deposit(amount)
    
    def withdraw(self, account, amount):
        account.withdraw(amount)

