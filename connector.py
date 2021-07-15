# imports
from instapy import InstaPy
from instapy import smart_run
from os.path import expanduser
import utils as util



class Connector:
    global session
    global listOfUsers
    def __init__(self,username,password):
        self.session = InstaPy(username=username,
                    password=password,
                    headless_browser=False,
                    browser_executable_path=r"C:\Program Files\Mozilla Firefox\firefox.exe",
                    want_check_browser=True
                    )
        self.session.login()
        self.username = username
        #print('DEBUG')
        #print(vars(self.session))
        #self.listOfUsers = self.session.grab_followers(username=username, amount="full", live_match=True, store_locally=True)
        
        #print('DEBUG')
        #print(self.listOfUsers)
        self.session.set_quota_supervisor(enabled=True,
                sleep_after=["comments_d", "follows", "unfollows", "server_calls_h"],
                sleepyhead=True,
                stochastic_flow=True,
                notify_me=True,
                peak_likes_hourly=57,
                peak_likes_daily=585,
                peak_comments_hourly=21,
                peak_comments_daily=182,
                peak_follows_hourly=48,
                peak_follows_daily=None,
                peak_unfollows_hourly=35,
                peak_unfollows_daily=402,
                peak_server_calls_hourly=None,
                peak_server_calls_daily=4700)

    def autoFollow(self,tags,qtd):
            return self.session.follow_by_tags([tags], amount=qtd)
    def autoLike(self,tags,qtd):
            return self.session.like_by_tags([tags], amount=qtd)
    def autoComment(self,url,qtd,qntdUserPerComment):
            utilitario = util.Utils()
            mapToComment = utilitario.getListOfToComment(self.listOfUsers,qtd,qntdUserPerComment)
            cont=0
            for x, y in mapToComment.items():
                  print(x, y)
                  print('Comentário',cont)
                  print('Usuários',y)
                  cont += 1
            self.session.set_do_comment(enabled=True, percentage=100)
            self.session.set_comments(["Masterful shot"])
            #self.session.set_do_follow(enabled=True, percentage=44)
            self.session.set_user_interact(amount=qtd, randomize=True, percentage=100, media='Photo')
            self.session.interact_by_URL(urls=["https://www.instagram.com/p/CMVhLZ1rKQt/"], randomize=True, interact=True, )
           
    def saveListFollowing(self):
            self.listOfUsers = self.session.grab_following(username=self.username, amount="full", live_match=True, store_locally=True)
            print(self.listOfUsers)

    def getListFollowing(self):
            utilitario =  util.Utils()
            self.listOfUsers = utilitario.getLastFileUsers(self.username)
            for x in self.listOfUsers:
                print(x)
            


    
        