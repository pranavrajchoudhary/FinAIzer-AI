def savings_ratio(income, savings):

    if income == 0:
        return 0

    return (savings / income) * 100


def expense_ratio(income, expenses):

    if income == 0:
        return 0

    return (expenses / income) * 100


def debt_ratio(income, debt):

    if income == 0:
        return 0

    return (debt / income) * 100


def monthly_savings_potential(income, expenses):

    return income - expenses


def emergency_fund_required(expenses):

    return expenses * 6


def investment_potential(income, expenses):

    remaining = income - expenses

    return max(remaining * 0.6, 0)


def financial_health_score(savings_ratio, debt_ratio):

    score = 100

    if savings_ratio < 20:
        score -= 20

    if debt_ratio > 40:
        score -= 30

    return max(score, 0)

def net_worth(savings, debt):

    return savings - debt


def future_value(monthly_investment, rate, years):

    months = years * 12

    monthly_rate = rate / 12 / 100

    value = 0

    for _ in range(months):

        value = (value + monthly_investment) * (1 + monthly_rate)

    return value