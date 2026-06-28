"""
╔══════════════════════════════════════════════════════════╗
║           PYTHON BANK MANAGEMENT SYSTEM                  ║
║         OOP-Based | File Storage | Full CRUD             ║
╚══════════════════════════════════════════════════════════╝
"""

import json
import os
import random
import hashlib
from datetime import datetime


# ─────────────────────────────────────────────
#  UTILITY HELPERS
# ─────────────────────────────────────────────

DATA_FILE = "accounts.json"

def load_data() -> dict:
    """Load all accounts from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data: dict) -> None:
    """Save all accounts to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def hash_pin(pin: str) -> str:
    """Hash a PIN using SHA-256 for secure storage."""
    return hashlib.sha256(pin.encode()).hexdigest()

def generate_account_number() -> str:
    """Generate a unique 10-digit account number."""
    data = load_data()
    while True:
        acc_no = str(random.randint(1_000_000_000, 9_999_999_999))
        if acc_no not in data:
            return acc_no

def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def separator(char="─", width=55):
    print(char * width)

def header(title: str):
    separator("═")
    print(f"  {title}")
    separator("═")


# ─────────────────────────────────────────────
#  ACCOUNT CLASS
# ─────────────────────────────────────────────

class Account:
    def __init__(self, name: str, pin: str, account_type: str,
                 balance: float = 0.0, account_number: str = None,
                 transactions: list = None, created_at: str = None):
        self.account_number = account_number or generate_account_number()
        self.name = name
        self.pin_hash = hash_pin(pin)
        self.account_type = account_type   # "Savings" or "Current"
        self.balance = balance
        self.transactions = transactions or []
        self.created_at = created_at or timestamp()

    # ── Serialization ──────────────────────────

    def to_dict(self) -> dict:
        return {
            "account_number": self.account_number,
            "name": self.name,
            "pin_hash": self.pin_hash,
            "account_type": self.account_type,
            "balance": self.balance,
            "transactions": self.transactions,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        acc = cls.__new__(cls)
        acc.account_number = data["account_number"]
        acc.name = data["name"]
        acc.pin_hash = data["pin_hash"]
        acc.account_type = data["account_type"]
        acc.balance = data["balance"]
        acc.transactions = data["transactions"]
        acc.created_at = data["created_at"]
        return acc

    # ── Core Operations ────────────────────────

    def verify_pin(self, pin: str) -> bool:
        return self.pin_hash == hash_pin(pin)

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("  ✗  Amount must be positive.")
            return False
        self.balance += amount
        self._log("DEPOSIT", amount)
        print(f"  ✓  ₹{amount:,.2f} deposited. New balance: ₹{self.balance:,.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("  ✗  Amount must be positive.")
            return False
        if amount > self.balance:
            print(f"  ✗  Insufficient funds. Available: ₹{self.balance:,.2f}")
            return False
        self.balance -= amount
        self._log("WITHDRAWAL", amount)
        print(f"  ✓  ₹{amount:,.2f} withdrawn. New balance: ₹{self.balance:,.2f}")
        return True

    def transfer(self, recipient: "Account", amount: float) -> bool:
        if amount <= 0:
            print("  ✗  Amount must be positive.")
            return False
        if amount > self.balance:
            print(f"  ✗  Insufficient funds. Available: ₹{self.balance:,.2f}")
            return False
        self.balance -= amount
        recipient.balance += amount
        self._log("TRANSFER OUT", amount, f"To: {recipient.account_number}")
        recipient._log("TRANSFER IN", amount, f"From: {self.account_number}")
        print(f"  ✓  ₹{amount:,.2f} transferred to {recipient.name} ({recipient.account_number})")
        return True

    def _log(self, txn_type: str, amount: float, note: str = ""):
        self.transactions.append({
            "type": txn_type,
            "amount": amount,
            "balance_after": self.balance,
            "note": note,
            "time": timestamp(),
        })

    # ── Display ────────────────────────────────

    def show_details(self):
        separator()
        print(f"  Account Holder : {self.name}")
        print(f"  Account Number : {self.account_number}")
        print(f"  Account Type   : {self.account_type}")
        print(f"  Balance        : ₹{self.balance:,.2f}")
        print(f"  Member Since   : {self.created_at}")
        separator()

    def show_mini_statement(self, n: int = 5):
        separator()
        print(f"  Last {n} Transactions — {self.name}")
        separator()
        if not self.transactions:
            print("  No transactions yet.")
        else:
            recent = self.transactions[-n:]
            for txn in reversed(recent):
                sign = "+" if "IN" in txn["type"] or txn["type"] == "DEPOSIT" else "-"
                print(f"  {txn['time']}  {txn['type']:<14}  {sign}₹{txn['amount']:>10,.2f}  "
                      f"Bal: ₹{txn['balance_after']:,.2f}")
                if txn["note"]:
                    print(f"  {'':>37}  ↳ {txn['note']}")
        separator()


# ─────────────────────────────────────────────
#  BANK CLASS  (controller / façade)
# ─────────────────────────────────────────────

class Bank:
    def __init__(self, bank_name: str = "PyBank"):
        self.bank_name = bank_name

    # ── Internal helpers ───────────────────────

    def _get_account(self, account_number: str):
        data = load_data()
        if account_number in data:
            return Account.from_dict(data[account_number])
        return None

    def _save_account(self, account: Account):
        data = load_data()
        data[account.account_number] = account.to_dict()
        save_data(data)

    def _authenticate(self, account_number: str) -> Account | None:
        acc = self._get_account(account_number)
        if not acc:
            print("  ✗  Account not found.")
            return None
        pin = input("  Enter PIN: ")
        if not acc.verify_pin(pin):
            print("  ✗  Incorrect PIN.")
            return None
        return acc

    # ── Public API ─────────────────────────────

    def create_account(self):
        header("OPEN NEW ACCOUNT")
        name = input("  Full Name       : ").strip()
        if not name:
            print("  ✗  Name cannot be empty.")
            return

        print("  Account Type    : 1) Savings  2) Current")
        choice = input("  Choose [1/2]    : ").strip()
        acc_type = "Savings" if choice == "1" else "Current" if choice == "2" else None
        if not acc_type:
            print("  ✗  Invalid choice.")
            return

        while True:
            pin = input("  Set 4-digit PIN : ").strip()
            if pin.isdigit() and len(pin) == 4:
                break
            print("  ✗  PIN must be exactly 4 digits.")

        confirm = input("  Confirm PIN     : ").strip()
        if pin != confirm:
            print("  ✗  PINs do not match.")
            return

        try:
            initial = float(input("  Initial Deposit (₹): ").strip())
        except ValueError:
            print("  ✗  Invalid amount.")
            return

        if initial < 0:
            print("  ✗  Deposit cannot be negative.")
            return

        acc = Account(name=name, pin=pin, account_type=acc_type, balance=initial)
        if initial > 0:
            acc._log("INITIAL DEPOSIT", initial)
        self._save_account(acc)

        separator()
        print(f"  ✓  Account created successfully!")
        print(f"  ►  Account Number : {acc.account_number}  (save this)")
        separator()

    def deposit(self):
        header("DEPOSIT")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if not acc:
            return
        try:
            amount = float(input("  Deposit Amount (₹): ").strip())
        except ValueError:
            print("  ✗  Invalid amount.")
            return
        if acc.deposit(amount):
            self._save_account(acc)

    def withdraw(self):
        header("WITHDRAW")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if not acc:
            return
        try:
            amount = float(input("  Withdrawal Amount (₹): ").strip())
        except ValueError:
            print("  ✗  Invalid amount.")
            return
        if acc.withdraw(amount):
            self._save_account(acc)

    def transfer(self):
        header("FUND TRANSFER")
        account_number = input("  Your Account Number   : ").strip()
        acc = self._authenticate(account_number)
        if not acc:
            return

        recipient_no = input("  Recipient Account No. : ").strip()
        if recipient_no == account_number:
            print("  ✗  Cannot transfer to your own account.")
            return
        recipient = self._get_account(recipient_no)
        if not recipient:
            print("  ✗  Recipient account not found.")
            return

        print(f"  Recipient Name : {recipient.name}")
        confirm = input("  Proceed? [y/n] : ").strip().lower()
        if confirm != "y":
            print("  Transfer cancelled.")
            return

        try:
            amount = float(input("  Transfer Amount (₹)   : ").strip())
        except ValueError:
            print("  ✗  Invalid amount.")
            return

        if acc.transfer(recipient, amount):
            self._save_account(acc)
            self._save_account(recipient)

    def check_balance(self):
        header("BALANCE ENQUIRY")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if acc:
            print(f"\n  Available Balance: ₹{acc.balance:,.2f}\n")

    def view_details(self):
        header("ACCOUNT DETAILS")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if acc:
            acc.show_details()

    def mini_statement(self):
        header("MINI STATEMENT")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if acc:
            acc.show_mini_statement(n=10)

    def change_pin(self):
        header("CHANGE PIN")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if not acc:
            return

        while True:
            new_pin = input("  New 4-digit PIN : ").strip()
            if new_pin.isdigit() and len(new_pin) == 4:
                break
            print("  ✗  PIN must be exactly 4 digits.")

        confirm = input("  Confirm New PIN  : ").strip()
        if new_pin != confirm:
            print("  ✗  PINs do not match.")
            return

        acc.pin_hash = hash_pin(new_pin)
        self._save_account(acc)
        print("  ✓  PIN changed successfully.")

    def delete_account(self):
        header("CLOSE ACCOUNT")
        account_number = input("  Account Number: ").strip()
        acc = self._authenticate(account_number)
        if not acc:
            return

        if acc.balance > 0:
            print(f"  ⚠  Remaining balance ₹{acc.balance:,.2f} will be forfeited.")

        confirm = input("  Type 'DELETE' to confirm account closure: ").strip()
        if confirm != "DELETE":
            print("  Account closure cancelled.")
            return

        data = load_data()
        del data[account_number]
        save_data(data)
        print(f"  ✓  Account {account_number} closed successfully.")

    def list_all_accounts(self):
        """Admin view — shows all accounts (no PIN required)."""
        header("ALL ACCOUNTS  [ADMIN]")
        data = load_data()
        if not data:
            print("  No accounts found.")
            return
        print(f"  {'Acc. No.':<14}  {'Name':<20}  {'Type':<9}  {'Balance':>12}")
        separator()
        for acc_data in data.values():
            print(f"  {acc_data['account_number']:<14}  "
                  f"{acc_data['name']:<20}  "
                  f"{acc_data['account_type']:<9}  "
                  f"₹{acc_data['balance']:>11,.2f}")
        separator()
        print(f"  Total accounts: {len(data)}")
        separator()


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    bank = Bank("PyBank")

    MENU = """
  ┌─────────────────────────────────────┐
  │         PyBank — Main Menu          │
  ├─────────────────────────────────────┤
  │  1.  Create Account                 │
  │  2.  Deposit Money                  │
  │  3.  Withdraw Money                 │
  │  4.  Fund Transfer                  │
  │  5.  Check Balance                  │
  │  6.  Account Details                │
  │  7.  Mini Statement                 │
  │  8.  Change PIN                     │
  │  9.  Close Account                  │
  │  10. Admin — List All Accounts      │
  │  0.  Exit                           │
  └─────────────────────────────────────┘
"""

    ACTIONS = {
        "1": bank.create_account,
        "2": bank.deposit,
        "3": bank.withdraw,
        "4": bank.transfer,
        "5": bank.check_balance,
        "6": bank.view_details,
        "7": bank.mini_statement,
        "8": bank.change_pin,
        "9": bank.delete_account,
        "10": bank.list_all_accounts,
    }

    print("\n  Welcome to PyBank — Your Trusted Digital Bank")

    while True:
        print(MENU)
        choice = input("  Select option: ").strip()

        if choice == "0":
            print("\n  Thank you for banking with PyBank. Goodbye!\n")
            break
        elif choice in ACTIONS:
            ACTIONS[choice]()
            input("\n  Press Enter to continue...")
        else:
            print("  ✗  Invalid option. Please try again.")


if __name__ == "__main__":
    main()