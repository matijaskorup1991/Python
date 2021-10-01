import functools


# def broj_unaprijed(n1, n2):
#     if n2 > n1:
#         broj_unaprijed(n1, n2-1)
#         print(n2)
#     else:
#         print(n2)


# broj_unaprijed(2, 5)

user = {
    "username": "matija"
}


# @tag nam govori da ce funkcija koju navedemo iza @ taga biti parent funkcija funkciji koju navedemo ispod @ taga

def make_secure(access_level):
    def decorator(func):
        # ovo radimo da bi sacuvali ime funkcije koja je dolje prikazana kao get_admin_password a ako ne koristimo functools ona mijenja ime u secure_function
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["username"] == "Admin":
                return func(*args, **kwargs)
            else:
                return f"no admin permissions for user :  {user['username']} "
        return secure_function
    return decorator


# sa decoratorom ce nasa get_admin_password funkcija biti zamjenjena sa secure_funkcijom a kao sto smo vec rekli, sa functools ona ne mjenja ime
@make_secure("username")
def get_admin_password():
    return "1234"


print(get_admin_password())
# print(get_admin_password.__name__)

# da bi dobili lokaciju nekog objekta u memoriji mozemo koristiti id() funkciju koju nam python pruza
