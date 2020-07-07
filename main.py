from instapy import InstaPy
import time
#import schedule


#login credentials
username = 'Attar_Souk'
password = 'Attar@123i'

session = InstaPy(
                  username=username,
                  password=password,
                  headless_browser=True
                  )

session.login()

#session.set_do_comment(True, percentage=10)
session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])

'''session.set_do_comment(True, percentage=25)
session.set_comments(['Nice Picture!!','Good Shot','Damnn its nice :)','Good One!','Keep it up!'])'''

#Follow people based on the stated hashtags below
session.follow_by_tags(['diettips'], amount=0)

#Like Post using hashtags given below
#session.like_by_tags(['diettips'], amount=0)

#Comments on post based on
#session.set_do_comment(True, percentage=25)
#session.set_comments(['Nice Picture!!','Good Shot','Damnn its nice :)','Good One!','Keep it up!'], media='Photo')

session.set_delimit_commenting(enabled=True, comments_mandatory_words=['stayfit', 'diettips'])


#Unfollow users who don't follow back
session.unfollow_users(amount=10, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)

#End the bot session
session.end()
