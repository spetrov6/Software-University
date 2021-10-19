class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, peoples):
        room = list(filter(lambda r: r.number == room_number, self.rooms))[0]
        output = room.take_room(peoples)
        if not output:
            self.guests += peoples

    def free_room(self, room_number):
        room = list(filter(lambda r: r.number == room_number, self.rooms))[0]
        self.guests -= room.guests
        room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join([str(x.number) for x in self.rooms if x.guests == 0])}\n"\
               f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.guests > 0])}"
