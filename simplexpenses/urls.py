from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from main.api import ExpenseResource

#admin.autodiscover()
expense_resource = ExpenseResource()

urlpatterns = patterns('',
    url(r'^$', include('main.urls')),
	url(r'^api/', include(expense_resource.urls)),
#    url(r'^admin/', include(admin.site.urls)),
)
