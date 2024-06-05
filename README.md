# EDM EMAIL DIGEST PYTHON

<!--![DocFinder Python GIF Demonstration](https://github.com/smhussain5/HCP-Django-Python/blob/main/DOCFINDER_PYTHON.gif?raw=true)--->

## Problem 🤔

Taking a long walk outside with some good music is one of my favorite ways to relax, but I noticed that I only update my playlist every so often. I was thinking of how I could find new music on a regular basis. The answer? With Python, duh! 😉

## Solution 💡

This application is powered by Selenium and GitHub Actions to deliver weekly music recommendations to my email. I used Selenium to open a headless Chrome webdriver and search Future House Music's YouTube page for their latest and most popular tracks. The resulting information would be stored an array and sent via email using smtplib and some HTML/CSS. To schedule those emails, I used GitHub Actions to run this script every week in the afternoon.

## Technologies Used ⚙

- CSS3
- EmailMessage (Library)
- GitHub Actions
- HTML5
- PyCharm
- Python
- Selenium
- SMTP (Library)

## Challenges 💢

<!--Originally, I wanted to add a "bookmark" feature so users can find their physicians of interest. From my research, it seems this would require knowledge of jQuery, which I have yet to learn. Deployment to Heroku was challenging to say the least. Migrating from SQLite to PostgreSQL produced errors due to mismatching of variable types. After some research on StackOverflow, I decided to delete the original SQLite database and migrate all models to the new PostgreSQL database and repopulate it via the front-end model forms and admin panel.--->

## Insights 💭

<!--I enjoyed developing this feature-rich application and I really believe there's potential to add more features (eg, bookmarks, reviews, etc) and scale this further. If this were to use real, active physicians, I would consider a verification step via email and include their profile picture and NPI number in their profile page. Although the complexity of Django seems daunting initially, it becomes much easier after the steep learning curve.--->

## Contact 📲

[![Static Badge](https://img.shields.io/badge/Send%20me%20an%20email-212121?style=flat-square&logo=gmail&logoColor=EA4335)](mailto:shababhussain525@gmail.com?)<br>
[![Static Badge](https://img.shields.io/badge/Connect_with_me_on_LinkedIn-212121?style=flat-square&logo=linkedin&logoColor=0A66C2)](https://www.linkedin.com/in/shabab-h)<br>
[![Static Badge](https://img.shields.io/badge/Follow_me_on_Twitter-212121?style=flat-square&logo=twitter&logoColor=1D9BF0)](https://twitter.com/shussain_5)<br>
[![Static Badge](https://img.shields.io/badge/Follow_me_on_GitHub-212121?style=flat-square&logo=github&logoColor=FAFAFA)](https://github.com/smhussain5)<br>
