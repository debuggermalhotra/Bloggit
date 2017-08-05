from rauth import OAuth1Service, OAuth2Service
from flask import current_app,url_for,request,redirect,session

class OAuthSignIn(object): #OAuthSignIn base class defines the structure that the subclasses that implement each provider must follow
    providers= None

    def _init__(self, provider_name):   #The constructor initializes the provider's name, and the application id and secret assigned by it, which are obtained from the configuration.
        self.provider_name=provider_name
        credentials=current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id=credentials['id']
        self.consumer_secret=credentials['secret']

    def authorize(self): #function for initiation of the authentication process. For this the application needs to redirect to the provider's web site to let the user authenticate there
        pass

    def callback(self): #Once the authentication is completed the provider redirects back to the application.
        pass

    def get_callback_urls(self): # The URL that the provider needs to redirect to is returned by this function
        pass

    @classmethod
    def get_provider(self, provider_name): #The get_provider() class method is used to lookup the correct OAuthSignIn instance given a provider name. This method uses introspection to find all the OAuthSignIn subclasses, and then saves an instance of each in a dictionary.
        if self.providers is None:
            self.provide={}
            for provider_class in self.__subclasses__():
                provider=provider_class
                self.providers[provider,provider_name]=provider
        return self.providers[provider_name]



    class FacebookSignIN(OAuthSignIn) :
        def __init__(self):
            super()


    class TwitterSignIN(OAuthSignIn) :
        pass
