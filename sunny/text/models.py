from django.db import models

class Book(models.Model):
	name 	= models.CharField(max_length=50)
	author 	= models.CharField(max_length=30) 

	def __unicode__(self):
		return self.name

class Paragraph(models.Model):
	para 			= models.CharField(max_length=4)
	para_text		= models.TextField()
	para_translation= models.TextField()
	add_time		= models.CharField(max_length=30)

	def __unicode__(self):
		return self.para

class Unit(models.Model):
	unit 		= models.CharField(max_length=4)
	text_title 	= models.CharField(max_length=100)
	text_author	= models.CharField(max_length=30)
	paragraph	= models.ForeignKey(Paragraph)

	def __unicode__(self):
		return self.unit

class TextTranslation(models.Model):
	name		= "TextTranslation"
	book		= models.ForeignKey(Book)
	unit 		= models.ForeignKey(Unit)

	def __unicode__(self):
		return self.name


