def my_print(msg):
    pass

def my_print_response(response):
    try:
        print(response.json())
    except Exception as e:
        print(e)
