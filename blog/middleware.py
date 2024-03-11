def mdlwr(get_response):
    def wrapper(request):
        print("Hello my middleware")
        return get_response (request)
    return wrapper
