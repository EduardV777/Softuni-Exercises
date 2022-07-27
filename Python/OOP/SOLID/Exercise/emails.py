"""
[Single Responsibility]
You are provided with a code on which you have to apply the DIP (Dependency Inversion Principle) so that when
adding new worker classes, the Manager class will work properly.
"""

from abc import ABCMeta, abstractmethod

class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

class IContent:

    @abstractmethod
    def set_content(self, content):
        pass

class MyContent(IContent):

    def __init__(self, content_type):
        self.content_type = content_type
        self.__content = None

    def set_content(self, content):
        if self.content_type == 'MyML':
            self.__content = '\n'.join(['<myML>', content, '</myML>'])
        else:
            self.__content = content
        
    def get_content(self):
        return self.__content

class Email(IEmail):

    def __init__(self, protocol, contentInfo: MyContent):
        self.protocol = protocol
        self.content_type = contentInfo.content_type
        self.__sender = None
        self.__receiver = None
        self.__content = contentInfo.get_content()

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


content = MyContent("MyML")
content.set_content("Hello, there!")
email = Email('IM', content)
email.set_sender('qmal')
email.set_receiver('james')
#email.set_content('Hello, there!')
print(email)

