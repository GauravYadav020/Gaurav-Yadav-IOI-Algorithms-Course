# IOI Algorithms Course Training
# Module 1 Lesson 1: After-Class Project
# Project Name: Enterprise Multi-Paradigm Command-Line Calculator Enclave

import math
import sys

class EnterpriseCalculator:
    def __init__(self):
        self.history = []
        self.bit_depth = 32

    def log_transaction(self, operation, inputs, result):
        self.history.append({"op": operation, "in": inputs, "out": result})

    def execute_basic(self, op, a, b):
        if op == '+': res = a + b
        elif op == '-': res = a - b
        elif op == '*': res = a * b
        elif op == '/':
            if b == 0: raise ZeroDivisionError("System Error: Critical Division by Zero Target.")
            res = a / b
        else: raise ValueError("Invalid Operator Flag.")
        self.log_transaction(op, (a, b), res)
        return res

    def execute_scientific(self, op, val):
        if op == 'sin': res = math.sin(math.radians(val))
        elif op == 'cos': res = math.cos(math.radians(val))
        elif op == 'log':
            if val <= 0: raise ValueError("Domain Error: Logarithm non-positive bounds.")
            res = math.log10(val)
        else: raise ValueError("Invalid Scientific Flag.")
        self.log_transaction(op, (val,), res)
        return res

    def print_audit_trail(self):
        print("\n=== CALCULATOR ENCLAVE AUDIT TRAIL ===")
        for idx, entry in enumerate(self.history):
            print(f"Transaction [{idx}]: Op={entry['op']} | Inputs={entry['in']} | Output={entry['out']}")

# Production Sandbox Execution
if __name__ == "__main__":
    calc = EnterpriseCalculator()
    print("Executing Sample Scenarios for Students...")
    try:
        print(f"Addition: {calc.execute_basic('+', 150.75, 45.25)}")
        print(f"Logarithm: {calc.execute_scientific('log', 100)}")
        calc.print_audit_trail()
    except Exception as e:
        print(f"Fault Handled: {e}")