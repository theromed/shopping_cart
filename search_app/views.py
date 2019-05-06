from django.shortcuts import render
from django.db.models  import Q
from shop.models import Product


def searchResult(request):
	products = None
	query = None 
	if 'q' in request.GET:
		query = request.GET.get('q')
		products = Product.objects.all().filter(Q(name__contains=query) | Q(description=query)) #В общем sqlite не поддреживает поиск без учета регистра, а вообще 
																								#contains - точное совпадение, icontains - без учета регистра. Уточнить у Миши.
	return render (request, 'search.html', {'query':query, 'products':products})	

