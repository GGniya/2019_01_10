import re

salary = "4.55-6千/月"
salary = "6.5千元以下/月"
salary = "10-20万/年"
# {0, 1} 等价于  ?
pattern = re.compile(r"\d+\.?\d*")
result = pattern.findall(salary)
# if len(result) == 2:
# if '-' in salary:
if len(result) == 2:
    min_salary = result[0]
    max_salary = result[1]
else:
    min_salary = max_salary = result[0]

min_salary = float(min_salary)
max_salary = float(max_salary)

if '千' in salary:
    min_salary = min_salary * 1000
    max_salary = max_salary * 1000
elif '万' in salary:
    min_salary = min_salary * 10000
    max_salary = max_salary * 10000

if '年' in salary:
    min_salary = int(min_salary / 12)
    max_salary = max_salary // 12             # // 表示整除
print(min_salary, max_salary)











