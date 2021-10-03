"""

Web Scraper for medium.com to automate me from going to the site directly and searching for articles.
Instead this application will send me the top 3 most recent articles Ive saved in my reading list.

An application which uses selenium to login to our my medium account
then, scrapes three articles from my "reading list".
then, sends those three articles to my phone.
then, deletes those three articles after sending them.
then logs out.

This bot is activated every 24 hours to complete this task.

THIS IS THE MAIN FILE TO RUN BOT

"""

from Scrape.logged import Login

inst = Login()
inst.launch_Page()


