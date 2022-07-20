from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")
    
    def add_room(self, room: Room):
        self.rooms.append(room)
    
    def take_room(self, room_number, people):
        if room_number <= len(self.rooms) and room_number > 0:
            if self.rooms[room_number - 1].take_room(people) == people:
                self.guests += people

    def free_room(self, room_number):
        if room_number <= len(self.rooms) and room_number > 0:
            guestsToLeave = self.rooms[room_number - 1].free_room()
            if not type(guestsToLeave) == str:
                self.guests -= guestsToLeave

    def status(self):
        freeRooms = []
        takenRooms = []
        output = f"Hotel {self.name} has {self.guests} total guests\nFree rooms: "

        for k in range(0, len(self.rooms)):
            if self.rooms[k].is_taken == False:
                freeRooms.append(str(k + 1))
            else:
                takenRooms.append(str(k + 1))

        output += f"{', '.join(freeRooms)}\nTaken rooms: {', '.join(takenRooms)}"
        return output