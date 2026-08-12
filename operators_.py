name = str(input("Customer Name:"))
age = int(input("Age:"))
salary = float(input("Monthly Salary:"))
emi = float(input("Monthly EMI:"))
credit_score = float(input("Credit Score:"))
balance = float(input("Loan Amount:"))
Annual_Salary = float(input("Annual Salary:"))
remaining_salary = (salary - emi)
emi_percentage = ((emi / salary) * 100)
loan_per_credit_score = (balance / credit_score)
is_adult = age >= 18
good_salary = salary >= 50000
good_credit = credit_score >= 750
low_emi = emi_percentage <= 40

eligible = is_adult and good_salary and good_credit and low_emi

premium_customer = good_salary and good_credit

needs_review = good_credit or good_salary

reject = not eligible

print("======================================\n\tLOAN ANALYSIS REPORT\n======================================")

print("Customer :", name)
print("Age :", age)
print("Salary :", salary)
print("EMI :", emi)
print("Credit Score :", credit_score)

print("\nAnnual Salary :", Annual_Salary)
print("Remaining Salary :", remaining_salary)
print("EMI Percentage :", emi_percentage)

print("\nAdult :", is_adult)
print("Good Salary :", good_salary)
print("Good Credit :", good_credit)
print("Low EMI :", low_emi)

print("\nEligible :", eligible)
print("Premium Customer :", premium_customer)
print("Needs Review :", needs_review) 
print("Reject :", reject)

# Reward Points :

print("\n======================================")





