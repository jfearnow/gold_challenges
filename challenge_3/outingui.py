import outing_repo

"""
   Komodo Outing Manager:
   1- List outings
   2- Add outing to list
      1. Golf
      2. Bowling
      3. Amusement Park
      4. Concert
   -another prompt for all types of event
   3- Get event calculations 
      -individual 
      -all together
   4- exit
"""


while True:
   print('Komodo Outings')
   choice = input("Enter your choice: \n" +
                  '1. List Outing: \n' +
                  '2. Add Outing to List: \n' +
                  '3. Get Event Costs: \n' +
                  '4. Exit\n')
            

   if choice == '1':
      list_copy = outing_repo.get_outings()
      print(list_copy)
   

   elif choice == '2':
      event_type = input('Enter your Event Choice: ')
      people_attending = input('Number of People Attending: ')
      date = input('Enter the Date of Event: ')
      cost_per_person = input('Cost per Person: ')
      outing_repo.create_outing(event_type, people_attending, date, cost_per_person)
   else:
      print('Outing is not an option')


   if choice == '3':
      cost = input("Enter your choice: \n" +
                  '1. Total Cost of All Outings: \n' +
                  '2. Individual Cost of Outings by Type: \n' )
      if cost == '1':
         total = outing_repo.total_cost()
         print(total)
      elif cost == '2':
         event = input("Enter the Event to total: \n")
         total = outing_repo.total_by_type(event)
         print(total) 
         

   if choice == '4':
      exit()

# TODO: get values from user for outing_repo.outing_builder() #2
# tmp_event_type = input("What is the event type (options here):")
# outing_repo.outing_builder(tmp_event_type)2