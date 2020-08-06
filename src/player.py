# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def pickup_item(self, items):
        if len(self.room.items) > 0:
            self.items.append(items[0])
            print('')
            print(f'You grabbed the {items[0]}')
            self.room.items.remove(items[0])
        else:
            print(f"No items in this room.")

    def drop_item(self, items):
        if self.items:
            self.room.items.append(items[0])
            print('')
            print(f'You dropped the {items[0]}')
            self.items.remove(items[0])
        else:
            print(f"You do not have any items to drop.")

    def player_inventory(self, items):
        if self.items:
            for item in range(len(self.items)):
                print(self.items[item].name)
        else:
            print(f"You don't have any items yet.")
