# IOI Algorithms Course Training
# Module 6 Lesson 1: After-Class Project
# Project Name: Decentralized Campus E-Library Catalog Ledger Engine

class BookAsset:
    def __init__(self, isbn, title, author, copies_available):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = copies_available

    def transition_inventory(self, quantity_delta):
        if self.copies + quantity_delta < 0:
            return False
        self.copies += quantity_delta
        return True

class CampusLibraryRegistry:
    def __init__(self):
        self.catalog = {}

    def register_new_asset(self, book_instance):
        self.catalog[book_instance.isbn] = book_instance

    def process_checkout(self, isbn):
        if isbn in self.catalog and self.catalog[isbn].transition_inventory(-1):
            return f"Checkout Success: '{self.catalog[isbn].title}' dispatched safely."
        return "Checkout Exception: Asset missing or zero copies inventory threshold reached."

if __name__ == "__main__":
    registry = CampusLibraryRegistry()
    registry.register_new_asset(BookAsset("978-3-16", "Introduction to Algorithms", "CLRS", 3))
    print(registry.process_checkout("978-3-16"))