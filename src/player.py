# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def pickup_item(self, items):
        if self.room.items:
            self.items.append(items)
            # self.room.items.remove(items)
        else:
            print(f"No items in this room.")

    def drop_item(self, items):
        if self.items:
            self.room.items.append(items)
            self.items.remove(items)
        else:
            print(f"You do not have any items to drop.")

    def inventory(self, items):
        if self.items:
            print(f"{self.items}")
        else:
            print(f"You don't have any items yet.")
