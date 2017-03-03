import world
import player


def play():
    world.load_tiles()
    fighter = player.Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(fighter.location_x, fighter.location_y)
    print(room.intro_text())
    while fighter.is_alive():
        room = world.tile_exists(fighter.location_x, fighter.location_y)
        # room.modify_player(fighter)
        # Check again since the room could have changed the fighter's state
        if fighter.is_alive():
            # print("\nChoose an action:\n")
            print()
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            print()
            for action in available_actions:
                if action_input == action.hotkey:
                    fighter.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()