# Dinner split Bill Calculator

def calculate_split_bill(total_bill, number_of_people, tip_percentage):
    """Return final amount each person must pay (including tip)."""
    tip_amount = total_bill * (tip_percentage / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / number_of_people
    return amount_per_person


