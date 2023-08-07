from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("""<h1>Hey I am a Django Sever.</h1>
    #                     <p>Hey this is a coming soon</p>
    #                     <hr>
    #                     <h3>Hope you are loving it:</h3>""")
#   return render(request,"index.html")  
    peoples = [
        {'name':"lakshman","age":26},
        {'name':"ram","age":24},
        {'name':"rohan","age":25},
        {'name':"deepak","age":29},
        {'name':"sandeep","age":29}
    ]
    
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo aut qui enim iste debitis id vel nulla distinctio harum dolore? Totam perspiciatis fugiat quo obcaecati vitae aliquid debitis optio architecto?"

    return render(request,"home/index.html", context={'peoples':peoples,"text":text})  

def about(request):
    context = {"page":"About"}
    return render(request,"home/about.html",context)

def contact(request):
    context = {"page":"Contact"}
    return render(request,"home/contact.html",context)

def success_page(request):
    return HttpResponse('<h1>Hey This is a success page.</h1>')
