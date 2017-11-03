BendigoBank API Wrapper
====================

Bendigo Bank API is a wrapper that allows you to access information about your bank account for the Australian Bank, 'Bendigo Bank'.

Installation
==============================================
To install this wrapper clone the respository with
```
git clone git@github.com:Trentr9/Bendigo-Bank-API.git
```

then navigate to the directory in the terminal and run
```
pip install .
```

Basic Usage
==============================================
To use the wrapper to get a list of your account names see the following snippet

```python
import BendigoBankAPI

bendigobank = BendigoBankAPI("ACCESSKEY", "PASSWORD")
accounts = bendigobank.get_accounts()

for account in accounts:
	print(account.get_name())
```

To use the wrapper to get an account by name that is called 'Statement Account' see the following snippet

```python
import BendigoBankAPI

bendigobank = BendigoBankAPI("ACCESSKEY", "PASSWORD")
account = bendigobank.get_account_by_name("Statement Account")

if account is None:
	print("That account wasn't found!")
    return
   
print(account)
```

TODO
==============================================
- Create documentation
- Refactor (maybe?)
- Add more functionality for bank accounts

Feel free to fork and submit pull requests