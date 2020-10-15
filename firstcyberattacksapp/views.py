from django.shortcuts import render

# Create your views here.
domain = "ecommerce-mac2.herokuapp.com"
def index(request):
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1
    # context = {
    #     'num_visits': num_visits,
    # }
    response = render(request, 'firstcyberattacksapp/index.html')
    response.set_cookie('city', 'haridwar', domain="."+domain)
    # return render(request, 'firstcyberattacksapp/index.html')# , context=context)
    return response