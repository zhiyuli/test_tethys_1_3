from tethys_sdk.base import TethysAppBase, url_map_maker


class Test13(TethysAppBase):
    """
    Tethys app class for test 1 3.
    """

    name = 'test 1 3'
    index = 'my_first_app_1_3:home'
    icon = 'my_first_app_1_3/images/icon.gif'
    package = 'my_first_app_1_3'
    root_url = 'my-first-app-1-3'
    color = '#1abc9c'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='my-first-app-1-3',
                           controller='my_first_app_1_3.controllers.home'),
        )

        return url_maps