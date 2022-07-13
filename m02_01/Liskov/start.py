from abc import abstractmethod, ABC


class Notification(ABC):

    @abstractmethod
    def notify(self, message, email):
        ...


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')


class NotificationService:
    def __init__(self, contact_, notification):
        self.contact = contact_
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, self.contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, self.contact.phone)
        else:
            raise Exception('The method notification not supported')


if __name__ == '__main__':
    contact = Contact('Andrij', 'adnrij@gmail.com', '+380501234567')
    notification_service = NotificationService(contact, Email())
    notification_service.send('Hello bro!')

    notification_service_sms = NotificationService(contact, SMS())
    notification_service_sms.send('Hello bro!')
