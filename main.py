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
    # plt.show()


#HELPERS

# HELPER function to convert dates to human readable format
def convert_pd_series_dates_to_human_readable_format (pd_date_to_format):
    pd_date_datetime = pd.to_datetime(pd_date_to_format)
    formatted_pd_date_string = pd_date_datetime.dt.strftime('%B %d, %Y')
    return formatted_pd_date_string

# HELPER function to convert dates to a range in human readable format
def convert_pd_series_date_range_to_human_readable_format(formatted_pd_start_date="N/A", formatted_pd_end_date="N/A"):
    month = formatted_pd_start_date.str.slice(0,7)
    start_day = formatted_pd_start_date.str.slice(8,10)
    end_day = formatted_pd_end_date.str.slice(8,10)
    year = formatted_pd_start_date.str.slice(-4)

    formatted_pd_date_range = f"{month} {start_day} - {end_day} {year}" 
    return formatted_pd_date_range


# create_text_report()
def create_text_report(df, monthly_budget_summary, monthly_budget=5000 ):
    # get the start and end dates from df
    reporting_period_start_date_string = df['date'].head(1)
    reporting_period_end_date_string = df['date'].tail(1)
    # convert the dates to datetimes to human readable format using helper formatting function
    reporting_period_start_formatted_date_string = convert_pd_series_dates_to_human_readable_format(reporting_period_start_date_string)
    reporting_period_end_formatted_date_string = convert_pd_series_dates_to_human_readable_format(reporting_period_end_date_string)
    # create a final string to express the range of the reporting period in human readable format
    # formatted_reporting_period = convert_pd_series_date_range_to_human_readable_format(reporting_period_start_formatted_date_string,reporting_period_end_formatted_date_string)
    total_monthly_expenses = monthly_budget_summary["total_monthly_expenses"]
    remaining_budget = monthly_budget_summary["difference_between_monthly_expenses_and_monthly_budget"]
    percent_of_budget_spent = round((total_monthly_expenses / monthly_budget *100) ,2)
    spending_by_category = monthly_budget_summary["monthly_expenses_grouped_and_summed_by_category"]
    top_5_expenses = monthly_budget_summary["top5_monthly_expenses"]
    budget_status = "Under budget" if remaining_budget > 0 else "Over budget"
    

    




    #Monthly Expenses Text Report
    final_monthly_expenses_report_string =f"""
    Monthly Budget Analysis Report 

    Reporting Period:{reporting_period_start_formatted_date_string} to {reporting_period_end_formatted_date_string}

    Budget Summary: 
    Total Budget: {monthly_budget}
    Total Expenses: {total_monthly_expenses}
    Budget Remaining: {remaining_budget}
    % of Budget Spent: {percent_of_budget_spent}

    Spending by category:
    {spending_by_category}

    Top 5 expenses:
    {top_5_expenses}

    Budget Status: {budget_status}

    Please review the attached pie chart for a visual breakdown of spending by category.

    This report was generated automatically. If you have any questions or notice any discrepancies,
    please contact the finance department.

    """


    with open("final_monthly_expenses_report.txt", "w") as file:
        file.write(final_monthly_expenses_report_string)

    return(final_monthly_expenses_report_string)



# send_email()
def send_email():
    print("test")


def calculate_budget_expenses():
    monthly_budget = 5000
    df = load_data()

    monthly_budget_summary = calculate_budget_summary(df, monthly_budget)

    monthly_expenses_pie_chart = create_pie_chart(monthly_budget, df, monthly_budget_summary )


    
    print(create_text_report(df, monthly_budget_summary, monthly_budget,))









print(calculate_budget_expenses())