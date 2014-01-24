#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from text.models import Book, Paragraph, Unit
from time import ctime

def Index(req):
	texts = Paragraph.objects.order_by('para')
	return render_to_response('text_index.html', {'texts':texts})

def AddText(req):
	errors = dict()
	if req.method == "POST":
		book_title 	= req.POST['book_title'].strip().lower()
		book_author	= req.POST['book_author'].strip()
		unit		= req.POST['unit'].strip().lower()
		text_title	= req.POST['text_title'].strip().lower()
		text_author	= req.POST['text_author'].strip()
		paragraph	= req.POST['paragraph'].strip().lower()
		# print "Para ", paragraph
		text_text	= req.POST['text_text'].strip()
		text_translation = req.POST['text_translation'].strip()
		errors = {
				'book_title'	: '',
				'book_author'	: '',
				'unit'			: '',
				'text_title'	: '',
				'text_author'	: '',
				'paragraph'		: '',
				'text_text'		: '',
				'text_translation' : '',
		}

		if not book_title:
			errors['book_title'] = "* " + "book title cannot be empty.".capitalize()
		if not book_author:
			errors['book_author'] = "* " + "book author cannot be empty.".capitalize()
		if not unit:
			errors['unit'] = "* " + "unit cannot be empty.".capitalize()
		if not text_title:
			errors['text_title'] = "* " + "text title cannot be empty.".capitalize()
		if not text_author:
			errors['text_author'] = "* " + "text author cannot be empty.".capitalize()
		if not paragraph:
			errors['paragraph'] = "* " + "paragraph cannot be empty.".capitalize()
		if not text_text:
			errors['text_text'] = "* " + "text cannot be empty.".capitalize()
		if not text_translation:
			errors['text_translation'] = "* " + "translation cannot be empty.".capitalize()

		flag = 0
		for key, value in errors.items():
			# print key, value
			if value:
				flag = 1
				break

		# print errors
		# print flag
		if flag:
			info = {
				'book_title'	: book_title,
				'book_author'	: book_author,
				'unit'			: unit,
				'text_title'	: text_title,
				'text_author'	: text_author,
				'paragraph'		: paragraph,
				'text_text'		: text_text,
				'text_translation' : text_translation,
			}
			return render_to_response('text_add.html', {'info':info, 'errors':errors})
		else:
			try:
				book = Book.objects.get(name=book_title, author=book_author)
			except Book.DoesNotExist, e:
				book = Book.objects.create(name=book_title, author=book_author)
			
			try:
				unit = Unit.objects.get(
					unit		= unit,
					text_title	= text_title,
					text_author = text_author,
					# paragraph	= para,
				)
			except Unit.DoesNotExist, e:
				unit = Unit.objects.create(
					book		= book,
					unit		= unit,
					text_title	= text_title,
					text_author = text_author,
				)
			
			try:
				para = Paragraph.objects.get(
					para = paragraph,
					# para_text	= text_text,
					# para_translation = text_translation,
					# add_time	= ctime()
				) 
			except Paragraph.DoesNotExist, e:
				para = Paragraph.objects.create(
					book = book,
					unit = unit,
					para		= paragraph,
					para_text	= text_text,
					para_translation = text_translation,
					add_time	= ctime()
				) 
				
				
			#try:
			#	text = TextTranslation.objects.create(
			#		book	= book,
			#		unit	= unit,
			#	)
			#except TextTranslation.DoesNotExist, e:
			#	text = TextTranslation.objects.create(
			#		book	= book,
			#		unit	= unit,
			#	)
			

			return HttpResponseRedirect('../index')
	else:
		return render_to_response('text_add.html', {"errors":errors})

def SearchText(req):
	pass
