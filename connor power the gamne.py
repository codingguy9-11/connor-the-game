class Game:
    def __init__(self):
        self.rooms = {
            'hall': {
                'description': 'You are in a hall also your name is connor power . There are doors to the left and right.',
                'exits': {'left': 'classroom', 'right': 'library'},
            },
            'classroom': {
                'description': 'Your in a classroom. Theres a bunch of teachers chatting.',
                'exits': {'right': 'hall'},
            },
            'library': {
                'description': 'You are in a 1st year classroom. Books are everywhere also the most strictest teacher is here.',
                'exits': {'left': 'hall'},
            }
        }
        self.current_room = 'hall'

    def play(self):
        while True:
            self.show_room()
            command = input("What do you want to do? ").strip().lower()
            self.process_command(command)

    def show_room(self):
        room = self.rooms[self.current_room]
        print(room['description'])
        print("Exits:", ', '.join(room['exits'].keys()))

    def process_command(self, command):
        if command in ['exit', 'quit']:
            print("Thanks for playing sigma!")
            exit()
        elif command in self.rooms[self.current_room]['exits']:
            self.current_room = self.rooms[self.current_room]['exits'][command]
        else:
            print("I don't understand that.")

if __name__ == "__main__":
    game = Game()
    game.play()
