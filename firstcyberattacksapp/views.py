from django.shortcuts import render

# Create your views here.
# #domain = "herokuapp.com"
def index(request):
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1
    # context = {
    #     'num_visits': num_visits,
    # }
    arr = request.get_host().split(':')[0].split('.')
    # if we are at subdomain page right now
    # we should delete subdomain using:
    arr.pop(0)
    domain = ".".join(arr)
    response = render(request, 'firstcyberattacksapp/index.html')
    response.set_cookie('city', 'haridwar', domain="."+domain)
    # return render(request, 'firstcyberattacksapp/index.html')# , context=context)
    return response