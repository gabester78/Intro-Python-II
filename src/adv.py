from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# # Items

items = {
    "compass": Item("Compass", """Let the earth guide you."""),
    "canteen": Item("Canteen", """Quench your thirst."""),
    "torch": Item("Torch", """Fire will light your way.""")
}

room['foyer'].items.append(items["compass"])
room['narrow'].items.append(items["canteen"])
room['overlook'].items.append(items["torch"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Gabe', room['outside'])

print("\nWelcome to Text Dungeon!")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    print(
        f"\n{player.name}, you're currently located at the {player.room}.")
    player.room.list_items()
    selection = input(
        "\nWhich direction would you like to travel? (North = n, East = e, South = s, West = w) or press q to quit the game. \nType get to pick up items, drop to remove items and inventory to see your items. ")

    if selection == "q":
        print("")
        print("Game over!")
        break

    elif selection == 'get':
        player.pickup_item(player.room.items)

    elif selection == 'drop':
        player.drop_item(player.items)

    elif selection == 'inventory':
        print("")
        player.player_inventory(items)

    elif player.room == room['outside']:
        if selection == 'n':
            player.room = room['foyer']
        else:
            print("")
            print(f"The road is blocked. Try again.")

    elif player.room == room['foyer']:
        if selection == 'n':
            player.room = room['overlook']
        elif selection == 's':
            player.room = room['outside']
        elif selection == 'e':
            player.room = room['narrow']
        else:
            print("")
            print(f"The road is blocked. Try again.")

    elif player.room == room['overlook']:
        if selection == 's':
            player.room = room['foyer']
        else:
            print("")
            print(f"The road is blocked. Try again.")

    elif player.room == room['narrow']:
        if selection == 'w':
            player.room = room['foyer']
        elif selection == 'n':
            player.room = room['treasure']
        else:
            print("")
            print(f"The road is blocked. Try again.")

    elif player.room == room['treasure']:
        if selection == 's':
            player.room = room['narrow']
        else:
            print("")
            print(f"The road is blocked. Try again.")
