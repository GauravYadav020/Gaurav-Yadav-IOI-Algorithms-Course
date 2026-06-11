# Module 2 Lesson 3: After-Class Project
# Project Name: E-Commerce Store Checkout Cart Discount Engine

class CartTransactionProcessor:
    def __init__(self):
        self.coupon_codes = {"WELCOME10": 0.10, "IOIALGOS": 0.25}

    def process_checkout(self, items_prices_list, applied_coupon):
        subtotal = sum(items_prices_list)
        discount_reduction = 0.0
        
        if applied_coupon in self.coupon_codes:
            discount_reduction = subtotal * self.coupon_codes[applied_coupon]
            
        tax_accrual = (subtotal - discount_reduction) * 0.08
        final_invoice_payout = (subtotal - discount_reduction) + tax_accrual
        return round(final_invoice_payout, 2)

if __name__ == "__main__":
    processor = CartTransactionProcessor()
    print(f"Final Cart Checkpoint Invoice Total: ${processor.process_checkout([120, 45, 300], 'IOIALGOS')}")