'''
Here are the parts of an outing:

	Event Type:
		Golf, Bowling, Amusement Park, Concert
	Number of people that attended,
	Date,
	Total cost per person for the event,
	Total cost for the event
'''


class Outing:

    def __init__(self, event_type, people_attending, date, cost_per_person):
        self.event_type = event_type
        self.people_attending = people_attending
        self.date = date
        self.cost_per_person = cost_per_person 
        self.total_cost = int(people_attending) * int(cost_per_person)  
            
    # TODO: add f string to repr to include date, type, people attending, total cost
    def __repr__(self):
        return f"(Event Type: {self.event_type}, {self.date}, People: {self.people_attending}, Total Cost: {self.total_cost})"