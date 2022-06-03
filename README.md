# ioet Posición

## Exercise
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

##  Installation

just uses [Python3.8](https://www.python.org/) to run.

```sh
python3 main.py
```

in order to change the input file change the line 51 of the file

## How the problem was resolved

First is separate the information (split the lines, split the date from each one 
etc..), this was done using a dictionary where each employee was the Key and the data 
was the time in the office 

![alt text](https://i.ibb.co/KLPQN8V/Captura.png)

After that is compare the days in common that each employee have and the function 
getTimes() counts how many times each employee has coincided in the office,
where compares the day of employeeA and employeeB and returns a 1 if they coincided
in the office on that day.

## License

MIT

**Free Software, Hell Yeah!**