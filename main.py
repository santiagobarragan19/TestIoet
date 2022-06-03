def createDictEmployees(file):
    employeesDict = {}

    file = open(file, "r")
    lines = file.readlines()

    for line in lines:
        name, dates = line.split("=")
        dates = dates.replace("\n", "")
        dates = dates.split(",")

        datesDict = {}
        for date in dates:
            day = date[0:2]
            datesDict[day] = date[2:]
        employeesDict[name] = datesDict

    return employeesDict


def count_coincide(day_employeeA, day_employeeB):
    day_employeeA = day_employeeA.replace(":","")
    day_employeeB = day_employeeB.replace(":", "")
    hoursA = day_employeeA.split("-")
    hoursB = day_employeeB.split("-")
    if (hoursA[0] <= hoursB[0] and hoursB[0] <= hoursA[1]) or (hoursA[0] <= hoursB[1] and hoursB[1] <= hoursA[1]):
        return 1
    elif (hoursB[0] <= hoursA[0] and hoursA[0] <= hoursB[1]) or (hoursB[0] <= hoursA[1] and hoursA[1] <= hoursB[1]):
        return 1
    return 0


def getTimes(employees):
    result = []
    for employeeA in list(employees):
        for employeeB in employees:
            if employeeA != employeeB:
                a = employees[employeeA]
                b = employees[employeeB]
                intersections = set(a.keys()) & set(b.keys())
                if intersections.__len__() > 0:
                    count = 0
                    for day in intersections:
                        count += count_coincide(a[day], b[day])
                    relation = [employeeA + "-" + employeeB, count]
                    result.append(relation)
        employees.pop(employeeA)
    return result


employees = createDictEmployees("times2.txt")
times = getTimes(employees)
for time in times:
    print("{}:{}".format(time[0], time[1]))
