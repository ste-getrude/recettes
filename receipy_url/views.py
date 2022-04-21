from urllib.parse import urlparse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



from .forms import UrlForm
from .models import ReceipyUrl

from receipy_url.common import comm_class


def index():
    return HttpResponse("Hello, world. You're at the polls index.")

def get_url(request):
    # we receive a post from our form
    if request.method == "POST":
        
        data = UrlForm(request.POST) # the data is placed in the UrlForm class data.url_name
        if data.is_valid(): # <- how do we add to validation (by field i guess)
            # on split le URL
            url_parse = urlparse(data.cleaned_data["url_name"])
            
            r = comm_class.WebSite(url_parse)
            
            r.get_scraping_factory().scrape_data()
            
            
            context = {}
            
            context['url_parse'] = r
            
            # check if data is already in the table
            
            if ReceipyUrl.objects.filter(netloc=url_parse.netloc, path=url_parse.path, params=url_parse.params, query=url_parse.query,fragment=url_parse.fragment).exists():
                # go to recipy
                # return HttpResponseRedirect(urlnametoindivudualreceipy + ReceipyObj.id)
                pass
            elif ReceipyUrl.objects.filter(netloc=url_parse.netloc).exists(): #check if netloc exist, meaning scraping script exist
                # insert object
                # get the data with the scraping script
                # redirect to receipy page
                # return HttpResponseRedirect(NEWurlnametoindivudualreceipy + ReceipyObj.id)
                pass
            else: # new domaine, scraping script must be coded
                # redirect to error page
                # save object
                # downlaod 
                return render(request, 'not_in_system.html', context) # this is the url 
    else: # the form hasn't been seen yet by the user, generate empty form
        form = UrlForm() # Intsantiate a form instance
        
    return render(request, 'form_get_url.html', {'form':form})

def not_in_systeme(request, ):
    return render(request, 'not_in_system.html')
    
        