def parse_salary(salary: int):
    salary = list(str(salary))
    s_length = len(salary)
    start = s_length%3
    if start == 0:
        start = 3
    for i in range(start, s_length, 4):
        salary.append([]) # Since a new character is added to the string.
        s_length = s_length + 1
        for j in range(1, s_length-i):
            salary[s_length-j] = salary[s_length-j-1]
        salary[i] = ','
        print(salary)
    return "".join(salary)
