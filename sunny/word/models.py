from django.db import models

class Version(models.Model):
	Version = models.CharField(max_length=1001)


class Word(models.Model):
	ad_time = models.CharField(max_length=255)
	last_time = models.CharField(max_length=255)
	use_times = models.IntegerField()
	Word = models.CharField(max_length=255)
	Description = models.CharField(max_length=1001)
	Phonetic = models.CharField(max_length=1001)
	Root = models.CharField(max_length=1001)
	Sentence = models.CharField(max_length=1000)


