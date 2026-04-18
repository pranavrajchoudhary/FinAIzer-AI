def validate_inputs(income, expenses, savings, debt):

    if income <= 0:
        return "Income must be greater than 0"

    if expenses < 0 or savings < 0 or debt < 0:
        return "Values cannot be negative"

    if expenses > income:
        return "Expenses exceed income"

    return None