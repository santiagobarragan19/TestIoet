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

def getTimes(employees):
    result = []
    employeeKeys = employees.keys()
    for employeeA in employeeKeys:
        for employeeB in employees:
            if employeeA != employeeB:
                a = employees[employeeA]
                b = employees[employeeB]
                intersections = set(a.items()) & set(b.items())
                if intersections.__len__() > 0:
                    relation = [employeeA + "-" + employeeB , intersections.__len__()]
                    result.append(relation)
    return result

employees = createDictEmployees("times1.txt")
times = getTimes(employees)
for time in times:
    print("{}:{}".format(time[0],time[1]))