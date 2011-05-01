from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=255, unique=True)
	email = models.CharField(max_length=255, unique=True)

	def __unicode__(self):
		return self.name

# Creates a table listing all games
class Game(models.Model):
	name = models.CharField(max_length=255, unique=True)

	def __unicode__(self):
		return self.name

class Score(models.Model):
	game = models.ForeignKey(Game)

class PlayerStats(models.Model):
	score = models.ForeignKey(Score)
	player = models.ForeignKey(Player)
	type = models.ForeignKey(ScoreType)
	score = models.IntegerField(default=1)
