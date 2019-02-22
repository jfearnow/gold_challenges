 from outing import Outing


'''
This module will handle the UI
and CRUD Functionality of the Menus object
'''
#CRUD: Create, Read, Update, Delete
outings = []

def create_outing(event_type, people_attending, date, cost_per_person):
    new_outing = Outing(event_type, people_attending, date, cost_per_person)
    outings.append(new_outing)

def get_outings():
    return outings


def total_cost():
    total = 0
    for event in outings:
        total += event.total_cost
    return total 


def total_by_type(event):
    total = 0
    for event_outing in outings:
        if event_outing.event_type == event:
            total += event_outing.total_cost
    return total

    










    
