# Module 1 Lesson 2: After-Class Project
# Project Name: Automated Corporate Payroll and Tax Deduction System

class CorporatePayrollProcessor:
    def __init__(self, tax_rate=0.18, provident_fund_rate=0.12):
        self.tax_rate = tax_rate
        self.pf_rate = provident_fund_rate

    def compute_net_salary(self, emp_id, employee_name, base_salary, overtime_hours, hourly_rate):
        if base_salary < 0 or overtime_hours < 0:
            return "Error: Negative fiscal parameters detected."
            
        gross_overtime = overtime_hours * hourly_rate
        gross_salary = base_salary + gross_overtime
        
        tax_deduction = gross_salary * self.tax_rate
        pf_deduction = gross_salary * self.pf_rate
        total_deductions = tax_deduction + pf_deduction
        
        net_payout = gross_salary - total_deductions
        
        return {
            "ID": emp_id, "Name": employee_name, "Gross": gross_salary,
            "Tax": tax_deduction, "PF": pf_deduction, "Net": net_payout
        }

if __name__ == "__main__":
    processor = CorporatePayrollProcessor()
    ledger = processor.compute_net_salary("EMP-2026", "Alex Mercer", 75000, 12, 450)
    print("--- Financial Payroll Ledger Generated ---")
    for key, val in ledger.items():
        print(f" * {key}: {val}")