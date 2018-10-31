class Animal(object):
	def __init__(self,sound,name,age,favourite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_color =	favourite_color
	def eat(self,food):
		print("Yummy!!" + self.name + "is eating" + food)
	def description(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color" + self.favourite_color)	
	def make_sound(self,x):
		print((self.sound + " ")*x )

class Person(object):
	def __init__(self,name,age,city,gender, favourite_food):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.favourite_food = favourite_food
	def eat_breakfast(self,food):
		if (food == "none"):
			food = self.favourite_food
		print("yum " + self.name + " is eating " + food)
	def play_game(self, game):
		print("This is so fun! " + self.name + " is playing " + game)


class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for i in self.lyrics:
			print i
		
flower_song = Song(["Roses are red, ","violets are blue, ","I wrote this poem just for you"])
flower_song.sing_me_a_song()

#####################################################################
# problem 1
#dog = Animal("bark","bim",6,"brown")
#dog.eat("meat")
#dog.description()		
#dog.make_sound(4)		

#####################################################################
#problem 2
#i = Person("Ilan",15,"Beit Shemesh","Male","meat")
#i.eat_breakfast("none")
#i.play_game("soccer")				

#####################################################################
#problem 3
#flower_song = Song(["Roses are red, ","violets are blue, ","I wrote this poem just for you"])
#flower_song.sing_me_a_song()