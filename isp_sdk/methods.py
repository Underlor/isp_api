from .sessions import Session


# More info in DOC: https://doc.ispsystem.ru/index.php/ISPmanager_API

class Methods:
    def __init__(self, session: Session):
        self.session = session

    def edit_domain(self, **input_params):
        func = 'webdomain.edit'
        params = {
            'sok': 'ok',
            **input_params
        }

        response = self.session.send_request(func, params)
        return response

    def del_domain(self, domain_name: str):
        """
        :param domain_name: Domain name
        """
        func = 'webdomain.delete'
        params = {
            'elid': domain_name,
        }

        response = self.session.send_request(func, params)
        return response

    def edit_user(self, name: str, **input_params):
        """
        Управление учетными записями пользователей
        Данная функция одновременно используется для просмотра параметров объекта,
        изменения объекта и создания нового объекта.

        :param name: Логин
        :param input_params: дополнительные параметры
        """
        func = 'user.edit'
        params = {
            'sok': 'ok',
            'name': name,
            **input_params,
        }

        response = self.session.send_request(func, params)
        return response

    def edit_email(self, name: str):
        """
        Управление почтовыми ящиками

        Документация метода:
        https://doc.ispsystem.ru/index.php/ISPmanager_API#.D0.9F.D0.BE.D1.87.D1.82.D0.BE.D0.B2.D1.8B.D0.B5_.D1.8F.D1.89.D0.B8.D0.BA.D0.B8

        :param: name: один или несколько уникальных идентификаторов объекта,
        разделенных запятой и следующим за ней пробелом ", ".
        Уникальный идентификатор - это элемент name из функции email.
        """

        func = 'email.edit'
        params = {
            'sok': 'ok',
            'name': name,
        }

        response = self.session.send_request(func, params)
        return response

    def email_delete(self, name):
        """
        Удаление почтового ящика
        """
        func = 'email.delete'
        params = {
            'elid': name,
        }

        response = self.session.send_request(func, params)
        return response
