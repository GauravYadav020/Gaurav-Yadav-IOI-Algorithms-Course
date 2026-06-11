# Module 6 Lesson 6: After-Class Project
# Project Name: Retail E-Commerce Invoice Generation and Cart Object Aggregator

class ProductItem:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

class OrderInvoice:
    def __init__(self, order_id, user_profile_object):
        self.order_id = order_id
        self.user = user_profile_object
        self.line_items = []

    def inject_product_row(self, product_instance, ordered_qty):
        self.line_items.append((product_instance, ordered_qty))

    def compute_grand_total_invoice(self, promotional_rebate=0.0):
        subtotal = sum(prod.price * qty for prod, qty in self.line_items)
        return round(subtotal - promotional_rebate, 2)

if __name__ == "__main__":
    item1 = ProductItem("P-101", "Developer Mechanical Keyboard", 125.50)
    invoice = OrderInvoice("INV-8832", "Alice_Root")
    invoice.inject_product_row(item1, 2)
    print(f"Grand Total Invoice Execution Payout: ${invoice.compute_grand_total_invoice(15.0)}")