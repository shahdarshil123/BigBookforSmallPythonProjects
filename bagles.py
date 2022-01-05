import random
class Player:
    def __init__(self,name,points = 0,no_of_guesses = 10):
        self.__name = name
        self.__no_of_guesses = no_of_guesses
        self.__points = points
        print(self.__name + ', Welcome to Bagles!')
        print('You will have ' + str(self.__no_of_guesses) + ' guesses\n')

    def get_name(self):
        return self.__name

    def get_no_of_guesses(self):
        return self.__no_of_guesses

    def get_points(self):
        return self.__points

    def set_points(self,points):
        self.__points = points

class Bagles:
    winner = ' '
    def __init__(self,rounds = 1):
        self.__rounds = rounds

    def start_game(self):
        print("Welcome to Bagles!")
        print("Each player will get the chance to enter 3 digit number")
        print("Who scores more points wins the game")
        print('Fermi means one or more digits entered by user is correct but at wrong positions')
        print('Pico means one or more digits are at correct positions\n')

    def generate_number(self):
        self.__random_number = str(random.randint(100,999))

    def get_random_number(self):
        return self.__random_number

    def get_rounds(self):
        return self.__rounds

    def set_rounds(self,rounds):
        self.__rounds = rounds

    def is_fermi(self,guess_number):
        for i in range(3):
            if(guess_number[i] == self.__random_number[i]):
                return True
        return False

    def is_pico(self,guess_number):
        for i in guess_number:
            if(i in self.__random_number):
                return True
        return False

    def dashboard(self):
        print("-----Dashboard--------")
        print('Rank    Players    Points\n')

        for index, player in enumerate(players):
            print(str(index + 1).ljust(7, ' '), player.get_name().ljust(10, ' '), player.get_points())
        print()

    def create_players(self,players):
        no_of_players = int(input('Enter number of players'))
        for i in range(no_of_players):
            players.append(Player(input('Enter player name')))
        return players

    def display_winner(self):
        winner = []
        max = 0
        for player in players:
            if (player.get_points() >= max):
               max = player.get_points()
        for player in players:
            if(player.get_points() == max):
                winner.append(player.get_name())
        if(len(winner)==0):
            print('No player has won the game')
        elif(len(winner)>1):
            print('It is a tie and the winners are',','.join(winner))
        else:
            print('The winner is ',winner[0])




game = Bagles()

#Create players
players = []
game.create_players(players)
#Create Dashboard

game.start_game()
while game.get_rounds() > 0:
    game.generate_number()
    number = game.get_random_number()
    print(number)
    for player in players:
        print(player.get_name()+'\'s turn')
        guess_number = str(input('Enter a number'))
        if(guess_number == number):
            player.set_points(player.get_points() + 50)
            print('Perfect Score\n')
        elif(game.is_fermi(guess_number)):
            player.set_points(player.get_points() + 10)
            print('Fermi\n')
        elif(game.is_pico(guess_number)):
            player.set_points(player.get_points() + 10)
            print('Pico\n')
        else:
            print('Bagles\n')
    game.dashboard()
    game.set_rounds(game.get_rounds()-1)

winner = game.display_winner()















