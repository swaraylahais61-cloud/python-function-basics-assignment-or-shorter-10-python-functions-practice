# Employee Overtime Salary System

def calculate_overtime_salary(base_salary, total_hours_worked):
    """Return final salary including overtime if hours_worked > 40."""
    if total_hours_worked > 40:
        extra_hours = total_hours_worked - 40
        overtime_pay = extra_hours * 50000
        return base_salary + overtime_pay
    return base_salary


