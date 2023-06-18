# #how to add an item in a list
# bookshelf =[]
# bookshelf.append("Today seems interesting")
# bookshelf.append("Practice Practice")
# print(bookshelf[0])





# class BaobabTree:
#     def __init__(self):
#         self.current_fruit = ""
#         self.current_power = ""
#         self.fruit_powers_map = {
#             "Apple": "Healing",
#             "Orange": "Energy Boost",
#             "Banana": "Strength",
#             "Mango": "Teleportation"
#         }

#     def get_current_fruit(self):
#         return self.current_fruit

#     def get_current_power(self):
#         return self.current_power

#     def plant_fruit(self, fruit):
#         self.current_fruit = fruit
#         self.current_power = self.fruit_powers_map.get(fruit, "Unknown")

#     def consume_fruit(self):
#         consumed_fruit = self.current_fruit
#         consumed_power = self.current_power

#         self.current_fruit = ""
#         self.current_power = ""

#         print(f"You consumed a {consumed_fruit}. It had the power of {consumed_power}.")


# # Example usage
# baobab_tree = BaobabTree()

# # Plant an apple
# baobab_tree.plant_fruit("Apple")
# print("Current fruit:", baobab_tree.get_current_fruit())
# print("Current power:", baobab_tree.get_current_power())

# # Consume the apple
# baobab_tree.consume_fruit()

# # Plant a mango
# baobab_tree.plant_fruit("Mango")
# print("Current fruit:", baobab_tree.get_current_fruit())
# print("Current power:", baobab_tree.get_current_power())

# # Consume the mango
# baobab_tree.consume_fruit()


#QUESTION 4

#The Magical Baobab: In a small village there is a Baobab tree believed
#  to have magical properties.Every season it bear different types of fruits,
# each with its own unique power. You have decided to create a software system 
# that tracks the changes in the tree and predicts what type of fruit it will bear
# next season and what powers it will possess. 
# The system should also record the effect o each each fruit hen consumed


empty_list =[]

class Possible_Fruit:
    def __init__(self,powers,effect,season,name):
        self.powers=powers
        self.effect=effect
        self.season=season
        self.name=name



    def __repr__(self):
         return f"{self.name} {self.effect} {self.powers} {self.season}"
fruits = Possible_Fruit(powers="changecolor",effect="gives energy",season="wet",name="big baobab")
empty_list.append(fruits)
print(fruits)

print(empty_list)

class Seasons:
    def __init__(self,seasons):
        self.seasons = seasons

    def __str__(self):
            return f"{self.seasons}"
    def predict_fruit(self):
        for item in empty_list:
            if self.seasons == item.season:
                print( f"{item.name} was produced in this {self.seasons} season")  


             
s = Seasons(seasons="wet")
s.predict_fruit()





#QUESTION 5
#You’re part of a community that hosts one of the largest drum circles in Africa.
#  There are different types of traditional drums used in the circle,
#  each with its unique sound and rhythm. The Djembe, Talking Drum, and
#  Bougarabou are among the popular ones. 
# These drums have common properties such as the material they’re made
#  from and their sizes, but they also have distinct characteristics.
#  For instance, the Talking Drum can mimic the lines of human speech, the Djembe is known for its wide range of tones, and the Bougarabou is noted for its deep, rich bass tones.
# You want to create a software model of the drum circle that encapsulates
# these different types of drums. You wish to include methods for each drum
# that represent the sound it makes, and also group similar drums together.
# Think about creating a base Drum class that contains properties and methods
#  common to all drums, and then create subclasses for each specific type of
#  drum (like Djembe, TalkingDrum, and Bougarabou).
# The subclasses should inherit from the base Drum class and also implement
#  their unique characteristics. This software model would help newcomers understand
#  the characteristics. This software model would help newcomers understand the characteristics
#  of each drum and how they contribute to the overall rhythm of the drum circle.
class Drum:
    def __init__(self, material, size):
        self.material = material
        self.size = size

    def make_sound(self, tone):
        print(f"{self.__class__.__name__}:{self.tone} {self.material} {self.size}")
        print(f" the drum of {self.material} and {self.size} makes {tone} tones ")
        


class Djembe(Drum):
    def make_sound(self, tone):
        super().__init__(self.material,self.size)
        print(f"The  djembe  makes {tone} sound")


class TalkingDrum(Drum):
    def make_sound(self, tone):
        print(f"makes {tone} sounds")

    def mimic_speech(self, tone):
        print("mimic human speech")

    def wide_range_tones(self, tone):
        print(f"wide range of {tone} tones")


class Bougarabou(Drum):
    def deep_rich_base(self, tone):
        print(f"contains deep rich {tone} sounds")


class MovieProject:
    def __init__(self, title, cast_members, shooting_schedule, budget):
        self.title = title
        self.cast_members = cast_members
        self.shooting_schedule = shooting_schedule
        self.budget = budget

    def add_cast_member(self, cast_member):
        self.cast_members.append(cast_member)

    def remove_cast_member(self, cast_member):
        if cast_member in self.cast_members:
            self.cast_members.remove(cast_member)
        else:
            print(f"{cast_member} is not a cast member of this project.")

    def update_shooting_schedule(self, schedule):
        self.shooting_schedule = schedule

    def adjust_budget(self, amount):
        if self.budget + amount >= 0:
            self.budget += amount
        else:
            print("Error: Budget cannot be negative.")

#Nolly Wood Movie Planner:AS a producer in the booming Nollywood movie industry , you are in 
# charge of multiple film projects at once.Each movie has different cast members , shooting
#  schedules , and budgets . You want to write a program to help manage your film projects
#  efficiently . The software should be able to handle he complexities of scheduling ,budgeting
#  and coordinating between different movie projects.

class MoviePlanner:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)
        else:
            print(f"{project.title} is not a project in the planner.")

    def update_project_details(self, project, cast_members, schedule, budget):
        project.cast_members = cast_members
        project.shooting_schedule = schedule
        project.budget = budget

    def generate_report(self):
        for project in self.projects:
            print(f"Title: {project.title}")
            print(f"Cast Members: {project.cast_members}")
            print(f"Shooting Schedule: {project.shooting_schedule}")
            print(f"Budget: {project.budget}")
            print()

# Great migration Forecast. Every year, millions of wildebeest, zebras, and other animals participate 
# in great migration across the Serengeti -Mara ecosystem. As a conservationist, you want
#  to develop a software system that models this migration, predicting the movement of
#  the herds based on the weather patterns, rivers levels, predator locations, and the 
# various factors that influence the migration

class GreatMigration:
    def __init__(self, weather_patterns, river_levels):
        self.weather_patterns = weather_patterns
        self.river_levels = river_levels

    def migrating_animals(self):
        if self.weather_patterns == "dry" or self.river_levels == "low":
            print("The migration will occur")
        elif self.weather_patterns == "wet" or self.river_levels == "high":
            print("Migration will not occur")
        else:
            print("Migration did not change")

new_migrate = GreatMigration("dry", "low" )
new_migrate.migrating_animals()


#The Ever-changing you are a fashion designer known for your unique and vibrant Ankara designs. 
# Recently , you have discovered that some of your fabric patterns change their designs based on
#  the temperature and mood of the wearer.You want to create a software application that can predict
#  the changes in the fabric design given the mood and temperature data . Think about the classes you
#  will need to model the changing Ankara and how to predict the changes 


class AnkaraDesign:
    def __init__(self, temperature, mood):
        self.temperature = temperature
        self.mood = mood

    def predictDesign(self):
        temp = 20
        moods = 5
        if self.temperature >= temp or self.mood == moods:
            print("the design changed to floral")
        elif self.temperature < temp or self.mood != moods:
            print("the design changed to black patterns")
        else:
            print("The design was detained")

pattern = AnkaraDesign(25, 3)
pattern.predictDesign()





class FlightBooking:
    def __init__(self):
        self.flights = []

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, flight, customer, seat_number):
        if flight.has_available_seats():
            flight.reserve_seat(customer, seat_number)
            return True
        else:
            return False

    def manage_passenger_info(self, flight, customer, new_info):
        if flight.is_passenger_on_flight(customer):
            flight.update_passenger_info(customer, new_info)
            return True
        else:
            return False

    def generate_booking_confirmation(self, flight, customer):
        if flight.is_passenger_on_flight(customer):
            confirmation = flight.generate_confirmation(customer)
            return confirmation
        else:
            return None


class Flight:
    def __init__(self, destination, date, total_seats):
        self.destination = destination
        self.date = date
        self.total_seats = total_seats
        self.passengers = {}

    def has_available_seats(self):
        return len(self.passengers) < self.total_seats

    def reserve_seat(self, customer, seat_number):
        if self.has_available_seats():
            self.passengers[customer] = seat_number

    def is_passenger_on_flight(self, customer):
        return customer in self.passengers

    def update_passenger_info(self, customer, new_info):
        if self.is_passenger_on_flight(customer):
            self.passengers[customer] = new_info

    def generate_confirmation(self, customer):
        if self.is_passenger_on_flight(customer):
            seat_number = self.passengers[customer]
            confirmation = f"Booking confirmed for {customer}. Seat number: {seat_number}"
            return confirmation
        else:
            return None



