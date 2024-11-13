class Employee:
    def __init__(self, employee_id, name, position, salary, contact_info):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.contact_info = contact_info

    def view_customer_account(self, customer):
        # Assume the customer has a list of accounts and we display the details
        print(f"Viewing account information for Customer: {customer.name}")
        for account in customer.accounts:
            print(f"Account Number: {account.account_number}, Balance: ${account.balance}")

    def manage_account(self, account, action):
        # Example action could be "open" or "close" account
        if action == "open":
            print(f"Opening account {account.account_number} for customer {account.customer.name}.")
        elif action == "close":
            print(f"Closing account {account.account_number} for customer {account.customer.name}.")
        else:
            print("Unknown action.")
    
    def handle_transaction(self, transaction):
        # Handle a transaction, like deposit or withdrawal
        transaction.execute()
        print(f"Transaction {transaction.transaction_id} executed by {self.name}.")

