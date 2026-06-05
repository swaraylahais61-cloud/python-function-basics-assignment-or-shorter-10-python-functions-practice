
#Movie Theater Discount Coupon Validation
def check_discount(total_price, ticket_quantity, coupon_code):
    discount = 15000
    if coupon_code == "NONTONSERU" and ticket_quantity >= 2:
        return total_price - discount
    return total_price


