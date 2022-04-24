# class Student():

#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first +  last + '.' + '2017@vitstudetn.ac.in'

# Student1 = Student('nvsp','anurudh',159)
# Student2 = Student('sai','ganesh',800)

# print(Student1.email)
# print(Student2.pay)





class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry","Ron" ,"Hermione","Ginny"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
         print(f"No seats available for {person}")
