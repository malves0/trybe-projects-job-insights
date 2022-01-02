from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    return {job["job_type"] for job in jobs}


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs = read(path)
    list_industries = {
        job["industry"] for job in jobs if job["industry"] not in ""
    }
    return list_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs = read(path)
    list_salaries = {
        job["max_salary"] for job in jobs if job["max_salary"].isdigit()
    }
    list_salaries = [int(value) for value in list_salaries]
    return max(list_salaries)


def get_min_salary(path):
    jobs = read(path)
    list_salaries = {
        job["min_salary"] for job in jobs if job["min_salary"].isdigit()
    }
    list_salaries = [int(value) for value in list_salaries]
    return min(list_salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min salary or max salary doesn't exists")
    if (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("min salary or max salary aren't valid integers")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min salary is greather than max salary")
    if type(salary) is not int:
        raise ValueError("salary isn't a valid integer")

    matched = job["min_salary"] <= salary <= job["max_salary"]
    return matched


def filter_by_salary_range(jobs, salary):
    job_filtered = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_filtered.append(job)
        except ValueError:
            pass
    return job_filtered
