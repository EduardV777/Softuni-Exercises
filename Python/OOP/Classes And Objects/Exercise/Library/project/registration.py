from .user import User
from .library import Library

class Registration:

    def __init__(serf):
        pass

    def add_user(self, user: User, library: Library):
        for username in library.user_records:
            if username.username == user.username:
                return f"User with id = {user.user_id} already registered in the library!"
        
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for u in range(0, len(library.user_records)):
            if library.user_records[u] == user.username:
                del library.user_records[u]
                return
        
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for k in range(0, len(library.user_records)):
            if library.user_records[k].user_id == user_id:
                if library.user_records[k].username != new_username:
                    for username in library.rented_books:
                        if username == library.user_records[k].username:
                            library.rented_books[new_username] = library.rented_books[username]
                            del library.rented_books[username]

                    library.user_records[k].username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                else:
                    return "Please check again the provided username - it should be different than the username used so far!"
        
        return f"There is no user with id = {user_id}!"