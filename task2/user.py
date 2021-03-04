class Users():
    import re   
    def __init__(self, FN , LN, EM, PW):
        self.first_name = FN
        self.last_name = LN
        self.email = EM
        self.password = PW

    def check_email(self):
        pattern = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if re.match(pattern,self.email) is not None:
            return True
        else:
            return False

    def check_password(self):
        pattern = r"^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$"
        if len(self.password) < 6 or len(self.password) > 12:
            print('password would between 6 and 12 characters in length')
            return False
        elif re.match(pattern,self.password) == None:
            print('password needs to contain at least one lowercase and one uppercase letter as well as a digit between 0 and 9.')
            return False
        else:
            print('valid password')
            return True
