import sys
import duckduckgo as d
import urllib2
from BeautifulSoup import *
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader, Template
from .models import *
from django.shortcuts import render

def home(request):
    #Load all featured searches
    featured = Featured.objects.all()

    #Load index.html template
    template = loader.get_template('index.html')

    #Define context for the template
    context = RequestContext(request, {
        'featured': featured[0],
    })

    #Return template with context
    return HttpResponse(template.render(context))

def search(request):

    #Get the query from the form
    query = str(request.GET.get('query'))
    
    #If the query is empty
    if query is "":
        #Load the template
        template = loader.get_template('search.html')
        #Make a new temporary template. Will not be stored
        tmpTemplate = Template("<center><h1>Whoops! Looks like we didn't find anything.</h1></center>")
        #Add context
        context = RequestContext(request, {
            "url": "",
            "site": tmpTemplate,
            "link": "",
            #"related": related,
        })

        #Render template with context
        return HttpResponse(template.render(context))
    #If the query contains something
    else:
        #Force character encoding to utf-8 
        reload(sys)
        sys.setdefaultencoding('utf8')
        
        #Array of allowed domain endings
        allowed = [".com", ".org", ".net"]
        #Get all of the sites
        sites = Sites.objects.all()
        
        #Call the duckduckgo instant answers api to get result and url
        result = d.query(query)
        url = result.abstract.url
        
        #Instantiate a variable called simpleUrl
        simpleUrl = None

        #Loop through all of the allowed domain endings
        for i in allowed:
            #If the url ends in one of the allowed url endings
            if i in url:
                #Parse the url along the url ending
                parsed = url.split(i)
                #Take the simple url and add the domain ending back to it
                simpleUrl = parsed[0] + i
                #Break the loop. No need to go on
                break

            #Log url in the database if it is not in it already
            if (url not in str(sites)):
                s = Sites(url=url)
                s.save()

        """
        Get an array of meta data key words from the url
        Go through all of the urls in the database
        if one of the first 10 key words is in the array of the url's meta data then log it as a related keyword
        """
                
        #related = getMetaData(sites, url)
        
        #Load the search.html template
        template = loader.get_template('search.html')
        
        #Open a channel to the site, and retrieve its...
        templateSite = BeautifulSoup(urllib2.urlopen(url))
        #body...
        body = templateSite.body
        #and css href.
        link = templateSite.link["href"]
        

        #Get all of the <a> in the template
        links = body.findAll("a")

        #Loop through all of the <a>
        for l in links:
            #If the link is not formatted correctly...
            if "//" not in str(l) and "#" not in str(l) and "href" in str(l):
                #Put the link into soup
                soup = BeautifulSoup(str(l))
                #Get the a tag out of the soup
                tag = soup.a
                #Take the simple url and add it to the tag's broken reference
                fixedUrl = simpleUrl + str(tag["href"])
                #Replace the malformatted link with the new, properly formatted link
                body = str(body).replace(str(tag["href"]), fixedUrl)
                        
        #Put site's body into a temporary template. This template will not be stored
        tmpTemplate = Template(body)
                        
        #Define the context for the template
        context = RequestContext(request, {
            "url": url,
            "site": tmpTemplate,
            "link": simpleUrl + link,
            #"related": related,
        })
                        
        #Return the template with context
        return HttpResponse(template.render(context))
                    
def getMetaData(sites, url):
    #Instantiate an array of related urls
    related = []
    
    #Open the url
    site = BeautifulSoup(str(urllib2.urlopen(url)))

    #Get all of the meta data keywords
    meta = site.findAll("meta")

    #Go through all of the sites
    for s in sites.all():
        #Open that site and get its meta data keywords
        tmp = BeautifulSoup(urllib2.urlopen(s.url).findAll("meta"))

        #Go through all of the meta keywords in meta
        for m in meta:
            #Go through all of the meta keywords in tmp
            for t in tmp:
                #If m == t...
                if m is t:
                    #It's a related site!
                    related.append(str(s))
    
    return related
