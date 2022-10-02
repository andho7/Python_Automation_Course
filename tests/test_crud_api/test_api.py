class TestAPI:
    def test_create_user(self, api):
        username = api.generate_username()
        assert not api.is_username(username)
        api.create_user(username)
        assert api.is_username(username)
        api.delete_user()

    def test_get_user_data(self, api):
        username = api.generate_username()
        api.create_user(username)
        assert api.is_user_data_equal()
        api.delete_user()

    def test_edir_user_data(self, api):
        username = api.generate_username()
        api.create_user(username)
        assert api.is_username(username)
        api.update_username()
        assert api.is_username(api.username)
        api.delete_user()

    def test_delete_user(self, api):
        username = api.generate_username()
        api.create_user(username)
        assert api.is_username(username)
        api.delete_user()
        assert not api.is_username(username)
