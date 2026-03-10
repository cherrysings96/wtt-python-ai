from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmpoloyee(Employee):
    def calculate_salary(self, days_in_month, time_per_day):
        salary = days_in_month*time_per_day
        return salary


class PartTimeEmployee(Employee):
    def calculate_salary(self, days_in_month, time_per_day):
        salary = days_in_month*time_per_day*0.5
        return salary


full = FullTimeEmpoloyee()
part = PartTimeEmployee()
print(f"Full time salary is: Rs.{full.calculate_salary(22, 8)}")
print(f"Part time salary is: Rs.{part.calculate_salary(22, 4)}")
