# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. 
# Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def average(self, salary: list[int]) -> float:
        maxSal = minSal = salary[0]
        total = 0
        for sal in salary:
            total += sal
            if sal > maxSal:
                maxSal = sal
            if sal < minSal:
                minSal = sal
        total = total - maxSal - minSal
        return total / (len(salary) - 2)