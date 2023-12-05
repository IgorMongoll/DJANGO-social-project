from typing import Any


class CustomMiddleWare:
    def __init__(self,get_response) :
        self.get_response = get_response
        
    def __call__(self,request) :
        response = self.get_response(request)
        print('Finally its weekend')
        print(request.method)
        print(request.META['TZ'])
        print(request.META['HTTP_HOST'])
        print(request.META['LANG'])
        print(request.COOKIES)
        print(response)
        print(response.status_code)
        if hasattr(response,'context_data'):
            print(response.context_data)           
            if 'user' in response.context_data:
                
                print(f"{response.context_data['user'].username} is using the website")
                print(response.context_data['user'].email)
        user = request.user
        print(user)
        if user.is_authenticated:
            print('everything is fine go enjoy your weekend')
        else :
            print('some guy is trying to log in please watch out !!!!!!!!! ')
        return response
        