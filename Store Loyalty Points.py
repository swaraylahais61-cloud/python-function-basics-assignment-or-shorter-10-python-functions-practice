#Store Loyalty Points System (Multiple Return Conditions)
def calculate_loyalty_points(total_transaction, member_status):
    if not member_status:
        return 0
    points = total_transaction // 20000
    return points


