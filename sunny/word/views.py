# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Word
from time import ctime

def index(req):
	print req
	word_use = Word.objects.order_by("-use_times")
	word_times = []
	for i in range(10):
		word_times.append(word_use[i].Word)
	return render_to_response('index.html', {'word_times':word_times})

def search(req):
	errors = []
	if req.method == "GET":
		word = 0
		if not req.GET.get("search_word", ''):
			errors.append("Enter a word!!!")
		else:
			search_word = req.GET['search_word'].strip().lower()
			try:
				word = Word.objects.get(Word = search_word)
			except Word.DoesNotExist, e:
				errors.append(e)
			else:
				word.last_time = ctime()
				try:
					word.use_times += 1
				except TypeError:
					word.use_times = 0
				word.save()
				global search_sentence
				search_sentence = word.Sentence
				global search_word_root 
				search_word_root = word.Root
		return render_to_response('search_result.html', {'word':word, 'errors':errors})
	else:
		return render_to_response("index.html", {'errors':errors})

def sentence(req):
	return HttpResponse(search_sentence)

def word_root(req):
	return HttpResponse(search_word_root)
