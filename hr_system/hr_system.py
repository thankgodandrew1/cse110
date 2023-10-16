                 # WEEK 11 TEAM ACTIVITY, CORE + STRETCH
                        # HUMAN RESOURCE SYSTEM 

with open('hr_system.txt') as hr_system:

    for line in hr_system:
        # print(line)
        line = line.strip()
        parts = line.split()

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        salary = float(salary / 12) / 2

        if job_title == 'Engineer':
            salary += 1000

        print(f'{name} (ID: {id_number}), {job_title} - ${salary:.2f}')