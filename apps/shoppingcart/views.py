# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):

	return render(request,'shoppingcart/index.html')

def buy(request):

	request.session['quantity'] = request.POST['quantity']
	request.session['product'] = request.POST['product_id']
	print type (request.session['product'])
	price_list = [19.99, 29.99, 99.99, 9.99]

	if int(request.session['product']) == 1:
		request.session['product'] = price_list[0] * int(request.session['quantity'])

	if int(request.session['product']) == 2:
		request.session['product'] = price_list[1] * int(request.session['quantity'])
	if int(request.session['product']) == 3:
		request.session['product'] = price_list[2] * int(request.session['quantity'])
	if int(request.session['product']) == 4:
		request.session['product'] = price_list[3] * int(request.session['quantity'])

	return redirect('/results')


def results(request):

	return render(request,'shoppingcart/results.html')


	# 	request.session['list'] += [{
	# 	"word": request.POST['word'],
	# 	"color": request.POST['color'],
	# 	"font": request.POST['font'],
	# 	"time": strftime("%Y-%m-%d %I:%M %p", gmtime())

	# }]	