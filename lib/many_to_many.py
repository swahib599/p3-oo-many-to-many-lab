class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []  # Store contracts in a list

    def contracts(self):
        # Return the list of contracts associated with this author
        return self.contracts_list

    def books(self):
        # Return a list of books associated with this author based on their contracts
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        # Create a new contract for this author and the given book
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        # Return the sum of royalties from all contracts associated with this author
        return sum(contract.royalties for contract in self.contracts_list)

class Book:
    def __init__(self, title):
        self.title = title
        self.contracts_list = []  # Store contracts in a list

    def contracts(self):
        # Return the list of contracts associated with this book
        return self.contracts_list

    def authors(self):
        # Return a list of authors associated with this book based on contracts
        return [contract.author for contract in self.contracts_list]

class Contract:
    all_contracts = []  # A class attribute to store all contracts

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book

        # Validate that the date is a string
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        
        self.date = date

        # Validate that royalties is an integer
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        
        self.royalties = royalties

        # Add the contract to the author and book
        author.contracts_list.append(self)
        book.contracts_list.append(self)

        # Add this contract to the list of all contracts
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, target_date):
        # Filter contracts by the given date and sort by date
        return sorted([contract for contract in cls.all_contracts if contract.date == target_date], key=lambda x: x.date)
