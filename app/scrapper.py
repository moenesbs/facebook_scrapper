from bs4 import BeautifulSoup
from datetime import date ,datetime, timedelta
import pprint
import json
from utils import *
from chromedriver import *

def navigate_page():
    logger.info("Start Navigating the page")
    scroll()
    time.sleep(5)
    openSeeMore()
    openComment()
    openSeeMoreComment()
    openreplies()
    logger.info('Done Navigating the page')

def scrap():
    navigate_page()
    soup = BeautifulSoup(driver.page_source,"lxml")
    posts = soup.find_all("div",{"class" : "x1ja2u2z xh8yej3 x1n2onr6 x1yztbdb"})
    posts_scrapped = []
    for post in posts:
        if post is not None:
            post_description = post.find("span", {"class" :"x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"})
            if post_description is None:
                post_description = "No description for this post"
            else:
                post_description = post_description.text
        
            post_date = post.find("a", {"class" : "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv xo1l8bm"}).text
            if post_date[-1] == "m":
                post_date = str(date.today())
            elif post_date[-1] == "d":
                post_date = str((datetime.today() - timedelta(days=int(post_date[0]))).date())
            elif post_date[-1] =='h':
                post_date = str((datetime.today() - timedelta(hours=int(int(post_date.replace('h',''))))).date())
            else:
                post_date = str(post_date)

            comments_details = []
            interactions = post.find("div",{"class" : "x1jx94hy x12nagc"})
            comments = interactions.find_all("div", {"class" : "xmjcpbm x1tlxs6b x1g8br2z x1gn5b1j x230xth x9f619 xzsf02u x1rg5ohu xdj266r x11i5rnm xat24cr x1mh8g0r x193iq5w x1mzt3pk x1n2onr6 xeaf4i8 x13faqbe"})
            for comment in comments:
                commentor_name = comment.find("span", {"class" : "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1tu3fi x3x7a5m x1nxh6w3 x1sibtaa x1s688f xzsf02u"}).text
                comment_text = comment.find("div",{"class" : "xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs"}).text
                comments_details.append({str(commentor_name) : comment_text })
            comments_number = post.find("span", {"class" : "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xi81zsa"})
            if comments_number is None:
                comments_number = "No comments for this post"
            else:
                comments_number = comments_number.text

            reactions_number = post.find("span", {"class" : "x16hj40l"}).text
            reactions = post.find("span", {"class" : "x6s0dn4 x78zum5 x1e558r4"})
            reaction_details = {}
            children = reactions.findChildren("span" , recursive=False)
            for child in children:
                reaction = child.find("div", {"class" : "x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz"})
                todict(reaction.get("aria-label"))
                reaction_details[todict(reaction.get("aria-label"))[0]] = todict(reaction.get("aria-label"))[1]

            post_link = "None"
            post_type = "None"
            #Blog
            if post.find("a", {"class" : "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x5yr21d xh8yej3"}) is not None:
                post_link = post.find("a", {"class" : "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x5yr21d xh8yej3"})
                post_link = post_link.get("href")
                post_type = "blog"


            #Img
            if post.find("a", {"class" : "x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lliihq x1pdlv7q"}) is not None:
                post_link = post.find("a", {"class" : "x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lliihq x1pdlv7q"})
                post_type = "img"
                post_link = post_link.get("href")

            #Video
            if post.find("video", {"class" : "xh8yej3 x5yr21d x1lliihq"}) is not None:
                post_link = post.find("video", {"class" : "xh8yej3 x5yr21d x1lliihq"})
                post_type = "video"
                post_link = post_link.get("src")

            
            post_details = {
                "post_type" : post_type,
                "post_link" : post_link,
                "post_description" : post_description,
                "post_date" : post_date,
                "comments_number" : comments_number,
                "comments" : comments_details,
                "reactions_number" : reactions_number,
                "reaction_details" : reaction_details,
            }
            #pprint.pprint(post_details)
            logger.info('Done Scrapping a post')
            posts_scrapped.append(post_details)
    return json.dumps(posts_scrapped)

