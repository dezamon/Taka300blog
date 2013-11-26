from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from blog.models import Entry
from blog import views
from blog.views import listing

urlpatterns = patterns('',
                       url(r'^$',
                          ListView.as_view(queryset = Entry.objects.all(),paginate_by=5),
                          name='list'),
                       url(r'^detail/(?P<pk>\d+)/$',
                           DetailView.as_view(model=Entry),
                           name='detail'),
                       url(r'^create/$',
                           CreateView.as_view(model=Entry),
                           name='create'),
                       url(r'^update/(?P<pk>\d+)/$',
                           UpdateView.as_view(model=Entry),
                           name='update'),
                       url(r'^delete/(?P<pk>\d+)/$',
                           DeleteView.as_view(model=Entry,
                                              success_url="/blog/"),
                           name='delete'),
                       )

urlpatterns += patterns('',
                        (r'^login/$','django.contrib.auth.views.login',{'template_name':'blog/registration/login.html'}),
                        (r'^logout/$','django.contrib.auth.views.logout',
                          {'template_name':'blog/registration/logout.html'}),
                        (r'^about/$',views.hello),
                        #url(r'^$',EntryCreateView.as_view(),name='list'),
  )