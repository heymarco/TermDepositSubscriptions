AGE = "age"
JOB = "job"
MARITAL = "marital"
EDUCATION = "education"
DEFAULT = "default"
BALANCE = "balance"
HOUSING = "housing"
LOAN = "loan"
CONTACT = "contact"
DAY_OF_WEEK = "day_of_week"
MONTH = "month"
CAMPAIGN = "campaign"
PDAYS = "pdays"
PREVIOUS = "previous"
POUTCOME = "poutcome"
PCONTACT = "pcontact"
SUCCESS_RATE = "success_rate"
BALANCE_PER_AGE = "balance_per_age"

categorical_columns = [
    JOB,
    MARITAL,
    EDUCATION,
    DEFAULT,
    HOUSING,
    LOAN,
    CONTACT,
    POUTCOME,
]

date_columns = [
    DAY_OF_WEEK,
    MONTH
]

numeric_date_columns = [
    col + ext for col in date_columns for ext in ["_sin", "_cos"]
]

numerical_columns = [
    AGE,
    BALANCE,
    CAMPAIGN,
    PDAYS,
    PREVIOUS,
    SUCCESS_RATE,
    BALANCE_PER_AGE,
]

TARGET = "y"