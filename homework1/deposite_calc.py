deposite = float(input())
period = int(input())
yearly_intrest = float(input())

acummulated_interest = float(deposite * (yearly_intrest / 100))
monthly_interest = acummulated_interest / 12
total_sum = float(deposite + (period * monthly_interest))
print(total_sum)