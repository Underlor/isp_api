from .sessions import Session


# More info in DOC: https://doc.ispsystem.ru/index.php/ISPmanager_API

class Methods:
    def __init__(self, session: Session):
        self.session = session if session else Session()

    def edit_domain(self, **input_params):
        func = 'webdomain.edit'
        params = {
            'sok': 'ok',
            **input_params
        }

        response = self.session.send_request(func, params)
        return response

    def del_domain(self, elid: str):
        """
        :param elid: Domain name
        """
        func = 'webdomain.delete'
        params = {
            'elid': elid,
        }

        response = self.session.send_request(func, params)
        return response

    def edit_user(self, name, password, **input_params):
        func = 'user.edit'
        params = {
            'sok': 'ok',
            'name': name,
            'passwod': password,
            **input_params,
        }

        response = self.session.send_request(func, params)
        return response

    def edit_email(self, name, domainname, password, **input_params):
        func = 'email.edit'
        params = {
            'sok': 'ok',
            'name': name,
            'domainname': domainname,
            'passwd': password,
            'confirm': password,
            **input_params,
        }

        response = self.session.send_request(func, params)
        return response

    def email_delete(self, name):
        func = 'email.delete'
        params = {
            'elid': name,
        }

        response = self.session.send_request(func, params)
        return response
