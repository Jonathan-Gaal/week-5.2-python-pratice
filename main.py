import pandas as pd
import datetime
import matplotlib.pyplot as plt
# import seaborn as sns

def load_data():
    df = pd.read_csv("data/october-2024.csv")
    df.columns = df.columns.str.lower()
    return df

def calculate_budget_summary(df, monthly_budget=5000):
    #compare total monthly expenses to total monthly budget
    total_monthly_expenses = df["amount"].sum().round(2)
    difference_between_monthly_expenses_and_monthly_budget = round(total_monthly_expenses + monthly_budget, 2)
    # Group and sum spending by category
    monthly_expenses_grouped_and_summed_by_category = df.groupby("category")["amount"].sum()
    # identify top 5 individual monthly expenses
    top5_monthly_expenses = df.sort_values(by="amount").head(5)
    # Output a dictionary consisting of the monthly budget summary
    monthly_budget_summary = {"total_monthly_expenses": total_monthly_expenses, "difference_between_monthly_expenses_and_monthly_budget": difference_between_monthly_expenses_and_monthly_budget, "monthly_expenses_grouped_and_summed_by_category": monthly_expenses_grouped_and_summed_by_category, "top5_monthly_expenses":top5_monthly_expenses }
    #return the monthly budget summary
    return monthly_budget_summary 



def create_pie_chart(monthly_budget, df, budget_summary):
    # Get the monthly expenses grouped by category
    monthly_expenses = abs(budget_summary["monthly_expenses_grouped_and_summed_by_category"])
    
    # Calculate the percentage of each expense relative to the total budget
    expense_category_percentages = round((monthly_expenses / monthly_budget) * 100)

    # Update the pie chart to show percentages as values and category names as labels
    plt.pie(expense_category_percentages, labels=monthly_expenses.index, autopct='%1.1f%%')  # Use index for labels
    plt.savefig('pie_chart.png')
    plt.show()




# create_text_report()
# send_email()

def calculate_budget_expenses():
    monthly_budget = 5000
    df = load_data()

    monthly_budget_summary = calculate_budget_summary(df, monthly_budget)

    print(create_pie_chart(monthly_budget, df, monthly_budget_summary ))









print(calculate_budget_expenses())