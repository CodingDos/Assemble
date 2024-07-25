from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        response = JsonResponse({'Logged in successfully'})
        response['Location'] = '/auth/'
        response.status_code = 302
        return response
    else: 
        return JsonResponse({'Invalid Credentials'}, status=400)
    
def userLogout(request):
    logout(request)
    response = JsonResponse({'Logged out successfully'})
    response['Location'] = '/'
    response.status_code = 302
    return response
