import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


def income_allocation_pie(income, expenses, savings):

    labels = ["Expenses", "Savings"]
    values = [expenses, savings]

    fig, ax = plt.subplots(figsize=(4,4))

    # HANDLE ZERO CASE
    if sum(values) == 0:
        ax.text(0.5, 0.5, "No financial data", 
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=12)
        ax.axis("off")
        return fig

    ax.pie(values, labels=labels, autopct="%1.1f%%")

    ax.set_title("Income Allocation")

    return fig


def savings_bar_chart(savings):

    fig, ax = plt.subplots(figsize=(5,3))

    if savings == 0:
        ax.text(0.5,0.5,"No savings data",
        horizontalalignment='center',
        verticalalignment='center')
        ax.axis("off")
        return fig

    ax.bar(["Monthly Savings"], [savings])

    ax.set_title("Savings Performance")

    return fig

def debt_ratio_chart(debt_ratio):

    fig, ax = plt.subplots(figsize=(4,2))

    if debt_ratio == 0:
        ax.text(0.5,0.5,"No debt data",
        horizontalalignment='center',
        verticalalignment='center')
        ax.axis("off")
        return fig

    ax.barh(["Debt Ratio"], [debt_ratio], color="#ff6b6b")

    ax.set_xlim(0,100)

    ax.set_title("Debt-to-Income Ratio")

    return fig

def financial_health_score(savings_ratio, debt_ratio):

    if savings_ratio == 0 and debt_ratio == 0:
        return 0

    score = 100

    if savings_ratio < 20:
        score -= 20

    if debt_ratio > 40:
        score -= 30

    return max(score,0)
import plotly.graph_objects as go


def financial_health_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Financial Health Score"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "green"},
            'steps': [
                {'range':[0,40],'color':'#ff4d4d'},
                {'range':[40,70],'color':'#ffa500'},
                {'range':[70,100],'color':'#4CAF50'}
            ]
        }
    ))

    fig.update_layout(height=300)

    return fig