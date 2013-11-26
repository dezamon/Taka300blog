from django.shortcuts import render_to_response

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from blog.models import Entry
from apps.paginate import Paginate

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
	contact_list = Entry.objects.all()
	paginator = Paginator(contact_list, 5)

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	return render_to_response('/blog/templates/entry_list.html',{"contacts":contacts})

"""
class EntryCreateView(CreateView):
	template_name = '{{ STATIC_URL }}templates/entry_list.html'

	def get_context_data(self, **kwargs):
		entry = Entry.objects.order_by('-pub_date')
		paginate = Paginate(self.request, entry,5)
		kwargs['entry'] = paginate.get_paginator()
		return kwargs
"""

def about(request):
	return render_to_response('blog/about.html',{'message':'this is the test page'})

from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello world")


"""
def index(request):
	entry = Entry.objects.all()
	paginator = Paginator(plan,3)

	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
	try:
		fp = paginator.page(page)
    except (EmptyPage, InvalidPage):
    	fp = paginator.page(paginator.num_pages)

	return render_to_response('blog/index.html',{"entry":fp})
"""