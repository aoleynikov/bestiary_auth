from users_repo import UsersRepo


class TestUsersRepo(UsersRepo):
    def delete_all(self):
        self.collection.remove({})
        return None
