from src.sorting import sort_by

jobs_mock = [
    {"min_salary": 1, "max_salary": 10, "date_posted": "2010-10-10"},
    {"min_salary": 2, "max_salary": 20, "date_posted": "2010-11-20"},
    {"min_salary": 3, "max_salary": 30, "date_posted": "2010-10-30"},
]

criteria_mock = [
    {"min_salary": "min_salary"},
    {"max_salary": "max_salary"},
    {"date_posted": "date_posted"},
]

jobs_mock_by_min_salary = [
    {"min_salary": 1, "max_salary": 10, "date_posted": "2010-10-10"},
    {"min_salary": 2, "max_salary": 20, "date_posted": "2010-11-20"},
    {"min_salary": 3, "max_salary": 30, "date_posted": "2010-10-30"},
]

jobs_mock_by_max_salary = [
    {"min_salary": 3, "max_salary": 30, "date_posted": "2010-10-30"},
    {"min_salary": 2, "max_salary": 20, "date_posted": "2010-11-20"},
    {"min_salary": 1, "max_salary": 10, "date_posted": "2010-10-10"},
]

jobs_mock_by_date = [
    {"min_salary": 2, "max_salary": 20, "date_posted": "2010-11-20"},
    {"min_salary": 3, "max_salary": 30, "date_posted": "2010-10-30"},
    {"min_salary": 1, "max_salary": 10, "date_posted": "2010-10-10"},
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == jobs_mock_by_min_salary

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == jobs_mock_by_max_salary

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == jobs_mock_by_date
