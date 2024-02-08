########## Part A ##########
# def main():
#     annual_salary = float(input('enter your annual salary: '))
#     portion_saved = float(input('portion of salary to be saved: '))
#     total_cost = float(input('cost of your dream house: '))
#
#     portion_down_payment = 0.25 * total_cost
#     current_savings = 0
#     r = 0.04
#     monthly_salary = annual_salary / 12
#     months = 0
#
#     while current_savings < portion_down_payment:
#         current_savings += (portion_saved * monthly_salary) + (current_savings*r/12)
#         months+=1
#
#     print('months needed: ' , months)

####### Part B ###################
# def main():
#     annual_salary = float(input('enter your annual salary: '))
#     portion_saved = float(input('portion of salary to be saved: '))
#     total_cost = float(input('cost of your dream house: '))
#     semi_annual_raise = float(input('semi-annual salary raise: '))
#
#     portion_down_payment = 0.25 * total_cost
#     current_savings = 0
#     r = 0.04
#     months = 0
#
#     while current_savings < portion_down_payment:
#         if months % 6 == 0 and months != 0:
#             annual_salary += (semi_annual_raise * annual_salary)
#         current_savings += (portion_saved * annual_salary / 12) + (current_savings*r/12)
#         months+=1
#
#     print('months needed: ' , months)

################# Part C #############################

def main():
    semi_annual_raise = 0.07
    r = 0.04
    total_cost = 1000000
    portion_down_payment = 0.25 * total_cost
    annual_salary = float(input('enter the starting salary: '))
    initial_salary = annual_salary
    current_savings = 0

    if 3 * annual_salary < portion_down_payment:
        print("It is not possible to pay the down payment in three years")

    low = 0
    high = 1
    bisection_count = 0
    months = 0
    portion_saved = (low + high) / 2
    while True:
        while months < 36:
            current_savings += (current_savings*r/12) + (portion_saved*annual_salary/12)
            months += 1
            if months % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
        if current_savings >= portion_down_payment + 100:
            high = portion_saved
            portion_saved = (high + low) / 2
            bisection_count += 1
            months = 0
            current_savings = 0
            annual_salary = initial_salary
        elif portion_down_payment - 100 <= current_savings <= portion_down_payment + 100:
            break
        else:
            low = portion_saved
            portion_saved = (high + low) / 2
            bisection_count += 1
            months = 0
            current_savings = 0
            annual_salary = initial_salary
    print("best savings rate: ", portion_saved)
    print("steps in bisection search: ", bisection_count)


if __name__ == "__main__":
    main()
