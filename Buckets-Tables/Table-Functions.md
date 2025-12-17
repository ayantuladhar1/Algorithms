```python
# Name: Ayan Tuladhar

import requests
import lxml.html as lh
import os
# The following function scrap table cells from the url.

url = 'https://covid19.colorado.gov/data'

page = requests.get(url)

doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//table')

[len(T) for T in tr_elements[:12]]

tr_elements = doc.xpath('//table')

col=[]
i=0

# The following function is to parse table header.

for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print ('%d:"%s"'%(i,name))
    col.append((name,[]))

# The following functions were used from Homework 2 part 1(a) to create a table and save it as an output in html format.

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
Metric, Cases, Confirmed cases, Probable cases, Variants of concerns, Variant under investigation, Total Hospitalized, Counties, People tested, Total encounters, Death among cases, Confirmed deaths among cases, Probable death among cases, Deaths due to COVID-19, Total outbreaks
Value, 450630, 423684 (94.02%), 26946 (5.98%), 572, 11, 24490, 64, 2681036, 6742446, 6073, 5343 (87.98%), 730 (12.02%), 6149, 4157

""")[1:-1])

# Function to write html file.

with open("Simple.html", "w", encoding="utf-8") as file_html:
    file_html.write(data)
os.system("Simple.html")
```

    1:""
    2:"Cases
    				450,630
    			Confirmed cases
    				423,684 (94.02%)
    			Probable cases
    				26,946 (5.98%)
    			Variants of concern*
    				572
    			Variants under investigation**
    				11
    			Total hospitalized
    				24,490
    			Counties
    				64
    			People tested
    				2,681,036
    			Test encounters
    				6,742,446
    			Deaths among cases
    				6,073
    			Confirmed deaths among cases
    				5,343 (87.98%)
    			Probable deaths among cases
    				730 (12.02%)
    			Deaths due to COVID-19
    				6,149
    			Total outbreaks
    				4,157
    			"
    




    0




```python

```
