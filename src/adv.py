from room import Room
from player import Player
import item
import textwrap
import help_file

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item.map, item.torch]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item.atlas, item.flashlight])
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

    user_input = input("\nSelect your next move. ").split(" ")

    # if only one character is entered, it's assumed to be a movement or display request
    if len(user_input) == 1:
        user_input = user_input[0]
        # Movement
        if user_input in ['n', 'e', 's', 'w']:
            new_room = getattr(current_player.current_room, str(user_input + '_to'))
            if new_room != None:
                current_player.current_room = new_room
                print(current_player.current_room)
            else:
                print("That's a void. Try again.")
        # Inventory
        elif user_input in ['i', 'inventory']:
            pass
            # TODO: Print out the items currently held by the player.
        # Help
        elif user_input == 'h':
            print(help_file.help_message)
        # Redisplay Room
        elif user_input in ['r', 'refresh']:
            print(current_player.current_room)
        elif user_input not in ['q']:
            print("\nPlease enter n, e, s, or w to move. Enter h for help.\n")

    # if two words are entered, it's assumed to be a command with a verb and object
    elif len(user_input) == 2:
        verb = user_input[0].lower()
        object = user_input[1].lower()

        # Pick up Item
        if verb in ['get', 'take']:
            room_items = []
            for each_item in current_player.current_room.items:
                room_items.append(each_item.name)
            if object.capitalize() in room_items:
                focused_object = getattr(item, str(object))
                current_player.inventory.append(focused_object)
                current_player.current_room.items.remove(focused_object)
                focused_object.on_take()
            else:
                print(f"There does not seem to be an object: {object}.\n")

        # Discard Item
        elif verb == 'drop':
            player_items = []
            for each_item in current_player.inventory:
                player_items.append(each_item.name)
            if object.capitalize() in player_items:
                focused_object = getattr(item, str(object))
                current_player.current_room.items.append(focused_object)
                current_player.inventory.remove(focused_object)
                focused_object.on_drop()
            else:
                print(f"You don't appear to be carrying an object: {object}.\n")

        else:
            print("\nInvalid request. Enter a valid request or h for help.\n")
