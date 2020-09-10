from room import Room
from player import Player
import item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item.level_map, item.torch]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item.large_map, item.flashlight])
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
input_name = input("\n\nWelcome explorer!\n\nPlease enter your name: ")
if input_name == "":
    input_name = 'Player1'
current_player = Player(input_name, room['outside'])
print(f"\nStart your adventure, {current_player.name}...\n\n{current_player.current_room}")


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

user_input = ""
while user_input != 'q':

    user_input = input("\nSelect your next move. ")
    if user_input in ['n', 'e', 's', 'w']:
        new_room = getattr(current_player.current_room, str(user_input + '_to'))
        if new_room != None:
            current_player.current_room = new_room
            print(current_player.current_room)
        else:
            print("That's a void. Try again.")
    elif user_input not in ['q']:
        print("Please enter n, e, s, or w to move. Enter q to quit.")


# The following block demonstrates how to handle a movement to a room that doesn't exist
# test_room = 'foyer'
# try:
#     new_room = room[test_room].e_to
#     print(new_room)
# except AttributeError:
#     print("Nothing")