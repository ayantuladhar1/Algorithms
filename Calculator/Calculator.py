# Name: Ayan Tuladhar

import math
from decimal import *
import os

# The following code was used from the source referenced below to create a table in HTML.
#  https://pythonprogramming.altervista.org/1563-2/.
# Function to create a table in HTML.


def wrap(a, tag):
    tag1 = tag
    if tag == "table":
        tag1 = "table border=5"
    if tag == "td" and a.strip().replace(".", "").isdigit():
        tag1 = "td style=\"text-align:left\""
    return f"<{tag1}>{a}</{tag}>"

# Function to help split the row and column with coma


def split(tab):
    tab = tab.splitlines()
    for q, row in enumerate(tab):
        tab[q] = row.split(",")
    return tab

# Function to wrap the table


def table(tab):
    html = ''
    for r, x in enumerate(tab):
        for a in x:
            html = html + wrap(a, "td")
        html = html + "<tr>"
    html = wrap(html, "table")
    return html

# Function to print the elements to the table in HTML.


data = table(split("""
n, 1 Sec, 1 Min, 1 Hour, 1 Day, 1 Month, 1 Year, 1 Century
log_n, 2 ^ 10 ^ 6, 2 ^ ( 60 * 10 ^ 7 ), 2 ^ ( 3600 * 10 ^ 9 ), 2 ^ ( 86400 * 10 ^ 10 ), 2 ^ ( 2592000 * 10 ^ 12 ), 2 ^ ( 31536000 * 10 ^ 13 ), 2 ^ ( 3153600000 * 10 ^ 15 )
&#8730n, 1.0e+12, 3.6e+15, 1.296e+19, 7.46496e+21, 6.718464e+24, 9.945192960e+26, 9.945192960e+30
n, 1.0e+6, 6.0e+7, 3.6e+9, 8.64e+10, 2.592e+12, 3.1536e+13, 3.1536e+15
nlogn, 62746, 2801417, 133378058, 2755147513, 71870856404, 797633893349, 68610956750570
n&#178, 1000, 7745, 60000, 293938, 1609968, 5615692, 56156922
n&#179, 99, 391, 1532, 4420, 13736, 31593, 146645
2&#8319, 19, 25, 31, 36, 41, 44, 51
n!, 9, 11, 12, 13, 15, 16, 17
    """)[1:-1])

# Function to write html file.

with open("Simple.html", "w", encoding="utf-8") as file_html:
    file_html.write(data)
os.system("Simple.html")


# Calculations to convert sec, minute, hour, day, month, year, and century.

sec = 1000000
minute = 60 * sec
hour = 60 * minute
day = 24 * hour
month = 30 * day
year = 365 * day
century = 100 * year

# Function to calculate n!(n factorial).


def de_fac(b):
    a = 0
    while True:
        if math.factorial(a) >= b:
            return a - 1
        else:
            a = a + 1

# Function to calculate NlogN.


def logic_n_log_n(b):
    bottom = 0.0
    top = 10e13
    while True:
        center = (bottom + top) / 2
        if bottom == center or center == top:
            return center
        if center * math.log(center, 2) > b:
            top = center
        else:
            bottom = center

# Function to calculate logN.


def log_n():
    # log(n)
    html_arr = []
    while True:
        print("LOG_N")
        html_arr.append("2 ^ 10 ^ 6")
        print("2 ^ 10 ^ 6")
        html_arr.append("2 ^ ( %d * 10 ^ 7 )" % (minute / sec))
        print("2 ^ ( %d * 10 ^ 7 )" % (minute / sec))
        html_arr.append("2 ^ ( %d * 10 ^ 9 )" % (hour / sec))
        print("2 ^ ( %d * 10 ^ 9 )" % (hour / sec))
        html_arr.append("2 ^ ( %d * 10 ^ 10 )" % (day / sec))
        print("2 ^ ( %d * 10 ^ 10 )" % (day / sec))
        html_arr.append("2 ^ ( %d * 10 ^ 12 )" % (month / sec))
        print("2 ^ ( %d * 10 ^ 12 )" % (month / sec))
        html_arr.append("2 ^ ( %d * 10 ^ 13 )" % (year / sec))
        print("2 ^ ( %d * 10 ^ 13 )" % (year / sec))
        html_arr.append("2 ^ ( %d * 10 ^ 15 )" % (century / sec))
        print("2 ^ ( %d * 10 ^ 15 )" % (century / sec))
        print(" ")
        break


log_n()

# Function to calculate square root of N.


def square_root_n():
    html_arr = []
    while True:
        print("SQUARE_ROOT_N")
        html_arr.append("{:.1e}".format(Decimal(sec ** 2)))
        print("{:.1e}".format(Decimal(sec ** 2)))
        html_arr.append("{:.1e}".format(Decimal(minute ** 2)))
        print("{:.1e}".format(Decimal(minute ** 2)))
        html_arr.append("{:.3e}".format(Decimal(hour ** 2)))
        print("{:.3e}".format(Decimal(hour ** 2)))
        html_arr.append("{:.5e}".format(Decimal(day ** 2)))
        print("{:.5e}".format(Decimal(day ** 2)))
        html_arr.append("{:.6e}".format(Decimal(month ** 2)))
        print("{:.6e}".format(Decimal(month ** 2)))
        html_arr.append("{:.9e}".format(Decimal(year ** 2)))
        print("{:.9e}".format(Decimal(year ** 2)))
        html_arr.append("{:.9e}".format(Decimal(century ** 2)))
        print("{:.9e}".format(Decimal(century ** 2)))
        print(" ")
        break


square_root_n()

# Function to calculate N.


def n():
    html_arr = []
    while True:
        print("N")
        html_arr.append("{:.1e}".format(Decimal(sec)))
        print("{:.1e}".format(Decimal(sec)))
        html_arr.append("{:.1e}".format(Decimal(minute)))
        print("{:.1e}".format(Decimal(minute)))
        html_arr.append("{:.1e}".format(Decimal(hour)))
        print("{:.1e}".format(Decimal(hour)))
        html_arr.append("{:.2e}".format(Decimal(day)))
        print("{:.2e}".format(Decimal(day)))
        html_arr.append("{:.3e}".format(Decimal(month)))
        print("{:.3e}".format(Decimal(month)))
        html_arr.append("{:.4e}".format(Decimal(year)))
        print("{:.4e}".format(Decimal(year)))
        html_arr.append("{:.4e}".format(Decimal(century)))
        print("{:.4e}".format(Decimal(century)))
        print("")
        break


n()

# Function to calculate NlogN.


def n_log_n():
    html_arr = []
    while True:
        print("N_LOG_N")
        html_arr.append(logic_n_log_n(sec))
        print(math.floor(logic_n_log_n(sec)))
        html_arr.append(logic_n_log_n(minute))
        print(math.floor(logic_n_log_n(minute)))
        html_arr.append(logic_n_log_n(hour))
        print(math.floor(logic_n_log_n(hour)))
        html_arr.append(logic_n_log_n(day))
        print(math.floor(logic_n_log_n(day)))
        html_arr.append(logic_n_log_n(month))
        print(math.floor(logic_n_log_n(month)))
        html_arr.append(logic_n_log_n(year))
        print(math.floor(logic_n_log_n(year)))
        html_arr.append(logic_n_log_n(century))
        print(math.floor(logic_n_log_n(century)))
        print("")
        break


n_log_n()

# Function to calculate N Square.


def n_square():
    html_arr = []
    while True:
        print("N_SQUARE")
        html_arr.append(math.sqrt(sec))
        print(math.floor(math.sqrt(sec)))
        html_arr.append(math.sqrt(minute))
        print(math.floor(math.sqrt(minute)))
        html_arr.append(math.sqrt(hour))
        print(math.floor(math.sqrt(hour)))
        html_arr.append(math.sqrt(day))
        print(math.floor(math.sqrt(day)))
        html_arr.append(math.sqrt(month))
        print(math.floor(math.sqrt(month)))
        html_arr.append(math.sqrt(year))
        print(math.floor(math.sqrt(year)))
        html_arr.append(math.sqrt(century))
        print(math.floor(math.sqrt(century)))
        print("")
        break


n_square()

# Function to calculate N Cube.


def n_cube():
    html_arr = []
    while True:
        print("N_CUBE")
        html_arr.append(sec ** (1 / 3.0))
        print(math.floor(sec ** (1 / 3.0)))
        html_arr.append(minute ** (1 / 3.0))
        print(math.floor(minute ** (1 / 3.0)))
        html_arr.append(hour ** (1 / 3.0))
        print(math.floor(hour ** (1 / 3.0)))
        html_arr.append(day ** (1 / 3.0))
        print(math.floor(day ** (1 / 3.0)))
        html_arr.append(month ** (1 / 3.0))
        print(math.floor(month ** (1 / 3.0)))
        html_arr.append(year ** (1 / 3.0))
        print(math.floor(year ** (1 / 3.0)))
        html_arr.append(century ** (1 / 3.0))
        print(math.floor(century ** (1 / 3.0)))
        print("")
        break


n_cube()

# Function to calculate 2 Pow N.


def two_power_n():
    html_arr = []
    while True:
        print("2_POWER_N")
        html_arr.append(math.log(sec, 2))
        print(math.floor(math.log(sec, 2)))
        html_arr.append(math.log(minute, 2))
        print(math.floor(math.log(minute, 2)))
        html_arr.append(math.log(hour, 2))
        print(math.floor(math.log(hour, 2)))
        html_arr.append(math.log(day, 2))
        print(math.floor(math.log(day, 2)))
        html_arr.append(math.log(month, 2))
        print(math.floor(math.log(month, 2)))
        html_arr.append(math.log(year, 2))
        print(math.floor(math.log(year, 2)))
        html_arr.append(math.log(century, 2))
        print(math.floor(math.log(century, 2)))
        print("")
        break


two_power_n()

# Function to calculate N Factorial.


def n_factorial():
    html_arr = []
    while True:
        print("N_FACTORIAL")
        html_arr.append(de_fac(sec))
        print(de_fac(sec))
        html_arr.append(de_fac(minute))
        print(de_fac(minute))
        html_arr.append(de_fac(hour))
        print(de_fac(hour))
        html_arr.append(de_fac(day))
        print(de_fac(day))
        html_arr.append(de_fac(month))
        print(de_fac(month))
        html_arr.append(de_fac(year))
        print(de_fac(year))
        html_arr.append(de_fac(century))
        print(de_fac(century))
        break


n_factorial()