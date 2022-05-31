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



employees = createDictEmployees("times1.txt")
