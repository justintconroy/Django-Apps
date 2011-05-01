from django.db import models
from decimal import *
from datetime import *

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
class CommonGame(models.Model):
	game = models.ForeignKey(Game)
	date_played = models.DateField(default=datetime.today())

	def __unicode__(self):
		return str(self.date_played)

	class Meta:
		abstract = True

# Abstract model for the players to be listed in each played game.
class GamePlayer(models.Model):
	player = models.ForeignKey(Player)
	score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.player.name

	class Meta:
		abstract = True

# Abstract model for statistics on each game that a player has played.
class GamePlayerStats(models.Model):
	game = models.ForeignKey(Game)
	player = models.ForeignKey(Player)
	total_games_played = models.IntegerField(default=0,editable=False)
	total_victory_points = models.IntegerField(default=0,editable=False)
#	average_victory_points = models.DecimalField(max_digits=5, decimal_places=default=0,editable=False)
	rating = models.IntegerField(default=1000,editable=False)
	wins = models.DecimalField(max_digits=5, decimal_places=3, default=0, editable=False)
	losses = models.DecimalField(max_digits=5, decimal_places=3, default=0, editable=False)

	def __unicode__(self):
		return self.player.name

	# Returns average number of victory points per game
	def _get_average_victory_points(self):
		if (self.total_games_played > 0):
			return Decimal(self.total_victory_points)/self.total_games_played
		else:
			return 0

	# Returns ratio of wins to losses
	def _get_win_loss_ratio(self):
		if (self.losses > 0):
			return self.wins/self.losses
		else:
			if (self.wins > 0):
				return 999999999999999.99
			else:
				return 0

	average_victory_points = property(_get_average_victory_points)
	win_loss_ratio = property(_get_win_loss_ratio)
	
	# Calculate a new rating
#	def calculate_rating(self, 


	class Meta:
		abstract = True

# fields specific to Settlers of Catan
class CatanGame(CommonGame):
#	game.default = Common_Game.gamefilter(name='Settlers of Catan')
	CommonGame.game.default = 1
	CommonGame.game.editable = False

class CatanPlayer(GamePlayer):
	game = models.ForeignKey(CatanGame)

class CatanPlayerStats(GamePlayerStats):
#	game.default = game_set.filter(name='Settlers of Catan')
	CommonGame.game.default = 1
	CommonGame.game.editable = False

