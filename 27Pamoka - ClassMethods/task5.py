class SpaceStation:
    def __init__(self):
        self.astronauts = []

    def add_astronaut(self, name, nationality, mission_duration):
        astronaut = {'name': name, 'nationality': nationality, 'mission_duration': mission_duration}
        self.astronauts.append(astronaut)

    def find_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut['name'] == name:
                return astronaut
        return None

    def remove_astronaut(self, name):
        astronaut = self.find_astronaut(name)
        if astronaut:
            self.astronauts.remove(astronaut)

    @classmethod
    def from_astronaut_list(cls, astronaut_list):
        space_station = cls()
        space_station.astronauts = astronaut_list
        return space_station

    @staticmethod
    def is_long_term_mission(astronaut):
        return astronaut['mission_duration'] > 6


# Example usage:
# Create a SpaceStation instance and add astronauts
station = SpaceStation()
station.add_astronaut('John Doe', 'USA', 8)
station.add_astronaut('Jane Smith', 'Canada', 5)

# Find an astronaut
found_astronaut = station.find_astronaut('John Doe')
print(found_astronaut)

# Remove an astronaut
station.remove_astronaut('John Doe')
print(station.astronauts)

# Use class method to create a SpaceStation from a list of astronauts
astronaut_list = [{'name': 'Alice', 'nationality': 'UK', 'mission_duration': 7},
                  {'name': 'Bob', 'nationality': 'Australia', 'mission_duration': 4}]
new_station = SpaceStation.from_astronaut_list(astronaut_list)
print(new_station.astronauts)

# Use static method to check if an astronaut is on a long-term mission
print(SpaceStation.is_long_term_mission({'name': 'Alice', 'nationality': 'UK', 'mission_duration': 7}))
print(SpaceStation.is_long_term_mission({'name': 'Bob', 'nationality': 'Australia', 'mission_duration': 4}))
