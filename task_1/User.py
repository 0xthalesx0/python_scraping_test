from Website import Website


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def access_website(self):
        website = Website(self.username, self.password)
        return website.login()


