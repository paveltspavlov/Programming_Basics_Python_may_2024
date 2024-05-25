yearly_fee = int(input())

sneakers = float(yearly_fee * 0.6)
clothes = float(sneakers * 0.8)
ball = float(clothes * 0.25)
accessories = float(ball * 0.2)

total_ammount = float(yearly_fee + sneakers + clothes + ball + accessories)
print(total_ammount)
