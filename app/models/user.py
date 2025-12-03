class User:
    def __init__(self, salary, deductions=None):
        self.salary = salary
        self.deductions = deductions or {}
