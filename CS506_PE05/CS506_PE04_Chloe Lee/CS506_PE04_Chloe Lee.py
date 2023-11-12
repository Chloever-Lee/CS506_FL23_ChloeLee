#CS506_FL23_PE04: Chloe Lee

#PE04- Class
#1. class Restaurant w/ 2 attributes: name, cuisine type.

class Restaurant():
    def __init__ (self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
       
#describe_restaurant() to print resturants info.
    def describe_restaurant(self):
        return '{}, {}'.format(self.name, self.cuisine_type)

 #open_restaurant() to message indicating the restaurant is'open'.   
    def open_restaurant(self):
        return '{}'.format(self.name)+ " is open"
       
#2
#update above program by creating three different instances from the class
Restaurant1 = Restaurant('Palace BBQ', 'Korean')
Restaurant2 = Restaurant('Pho Bac', 'Vietnamese')
Restaurant3 = Restaurant('Din Tai Fung','Chinese')

#call describe_restaurant() for each instance
print(Restaurant1.describe_restaurant())
print(Restaurant2.describe_restaurant())
print(Restaurant3.describe_restaurant())
print("\t")
print(Restaurant1.open_restaurant())
print(Restaurant2.open_restaurant())
print(Restaurant3.open_restaurant())

print("\n")
#PE04- Object Oriented Programming
#1. class- User(). w/ create two attributes (first_name, last_name)
#Then,create several other attributes that are typically stored in a user profile

class User():
    def __init__(self, first_name, last_name,location,userID, video_game):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.userID = userID
        self.video_game = video_game
        
#method- describe_user() to print a summary of user info
    def describe_user(self):
        print ('{} {}'.format(self.first_name,self.last_name))
        print("\tUserID: ", self.userID)
        print("\tLocation: ", self.location)
        print("\tFavorite Video Game: ", self.video_game)
#another method- greet_user() to print a personalized greeting to the user   
    def greet_user(self):
        print("Greetings, ", self.userID, "!")

#driver code    
user1 = User('Chloe', 'Lee', 'Auburn, WA', 'Chloe-ever', 'Zelda')
user2 = User('Mark', 'Strong', 'Auburn, WA','TheMawz', 'Final Fantasy')  

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

#2.write a program to show how multilevel inheritance works
print("\n")
#parent class
class Profile():
    def __init__(self,user_ID, name):
        self.user_ID = user_ID
        self.name = name
    def get_profile(self):
        print(f"{self.name}'s ID is {self.user_ID}")

#child class
class Gamer(Profile):
    def __init__(self, user_ID, name, video_game):
        super().__init__(user_ID, name)
        self.video_game = video_game
    
    def Favorite_game(self):
        print('Gamer class')
        print(f"{self.user_ID}'is currently playing: {self.video_game}")

profile1 = Profile('Chloe-ever','Chloe')
profile2 = Profile('TheMawz', 'Mark')
profile1.get_profile()
profile2.get_profile()

gamer1 = Gamer('Chloe-ever','Chloe','Skyword Sword' )
gamer2 = Gamer('TheMawz', 'Mark', 'Overwatch' )
gamer1.Favorite_game()
gamer2.Favorite_game()


#PE04- Working with Files:
#1.Python takes a text file and returns the number of words
#variable to store number of words: start w/0
count_words = 0
#open file with open()
with open('CountingWords.txt') as file:
    text = file.read()
    #spliting text into seperate lines w/ split() function
    lines = text.split()
    #each lines from spliting will be counted with += operator
    count_words += len(lines)
    print("How many words in 'CountingWords.txt'?")
    print(f"{count_words} words")

#2.while loop that prompts users for name


print("\n")

while True:
    print("Please enter 'q' to quit")
    inp = input("Leave your name on my guest book: ")
    
    if inp == 'q':
        break
    else:
        print(f"Hello, {inp.title()}!") #print a greeting to the screen 
        guest_list =open('GuestBook.txt', 'a')
        #And add a line recording visits in a file called guest_book.txt
        guest_list.write(f"\n{inp.title()} visited here")
        guest_list.close()

print("\n")

#3. cats.txt & dogs.txt
#read cats & dogs files and print to the screen
#try-except block to catch "FileNotFound" error & friendly message to inform
try:
    with open('cats.txt', 'r') as cats:
        cats = cats.read()
    with open('dogs.txt', 'r') as dogs:
        dogs = dogs.read()
        print(f"Names for cats: \n{cats}")
        print(f"Names for dogs: \n{dogs}")
except FileNotFoundError:
    print("Lost cats, dogs.txt! Please to be found.")
    
















    
   

        
    
    

