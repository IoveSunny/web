from django.db import models

class Book(models.Model):
	name 	= models.CharField(max_length=50)
	author 	= models.CharField(max_length=30) 

	def __unicode__(self):
		return self.name

	class Admin:
		pass

class Unit(models.Model):
	book		= models.ForeignKey(Book)
	unit 		= models.CharField(max_length=4)
	text_title 	= models.CharField(max_length=100)
	text_author	= models.CharField(max_length=30)

	def __unicode__(self):
		return self.unit
	
	class Admin:
		pass

class Paragraph(models.Model):
	book			= models.ForeignKey(Book)
	unit			= models.ForeignKey(Unit)
	para 			= models.IntegerField()
	para_text		= models.TextField()
	para_translation= models.TextField()
	add_time		= models.CharField(max_length=30)

	def __unicode__(self):
		return self.para

	class Admin:
		pass

#class TextTranslation(models.Model):
#	name		= "TextTranslation"
#	book		= models.ForeignKey(Book)
#	unit 		= models.ForeignKey(Unit)
#
#	def __unicode__(self):
#		return self.name


