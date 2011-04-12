from django.db import models

# Creates table listing all players for all games
class Player(models.Model):
	name = models.CharField(max_length=32, unique=True)

	def __unicode__(self):
		return self.name

# Creates a table listing all games
class Game(models.Model):
	name = models.CharField(max_length=32, unique=True)

	def __unicode__(self):
		return self.name

# Abstract class for recording the result of each game played
class Common_Game(models.Model):
	game = models.ForeignKey(Game)
	date_played = models.DateField(default=datetime.today())

	def __unicode__(self):
		return self.date_played

	class Meta:
		abstract = True

# Abstract model for the players to be listed in each played game.
class Game_Player(models.Model):
	player = models.ForeignKey(Player)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.player

	class Meta:
		abstract = True

# Abstract model for statistics on each game that a player has played.
class Game_Player_Stats(models.Model):
	game = models.ForeignKey(Game)
	player = moedels.ForeignKey(Player)
	total_games_played = models.IntegerField(default=0,editable=False)
	total_victory_points = models.IntegerField(default=0,editable=False)
	average_victory_points = models.DecimalField(max_digits=5, decimal_places=default=0,editable=False)
	rating = models.IntegerField(default=1000,editable=False)
	wins = models.DecimalField(max_digits=5, decimal_places=3, default=0, editable=False)
	losses = models.DecimalField(max_digits=5, decimal_places=3, default=0, editable=False)

	def __unicode__(self):
		return self.player

	class Meta:
		abstract = True

# fields specific to Settlers of Catan
class Catan_Game(Common_Game):
	game.default = game_set.filter(name='Settlers of Catan')
	game.editable = False

class Catan_Player(models.Model):


class Catan_Player_Stats(Game_Player_Stats):
	game.default = game_set.filter(name='Settlers of Catan')
	game.editable = False

