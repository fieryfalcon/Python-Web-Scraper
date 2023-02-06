from scrape import *
from database import *

break_loop = int(input("type in the range : "))

for id in range(break_loop):
    if scrape(id):
        a = scrape(id)[0]["name"]
        b = scrape(id)[0]["cas_number"]
        print(a)
        obj_name = 'sample_object{}'.format(id)
        obj_name = chemical(a, b)
        obj_name.save()
    else:
        print(str(id) + " page not found")


search(1051)
