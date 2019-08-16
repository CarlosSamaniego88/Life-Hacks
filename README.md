# Life-Hacks
Cool python scripts for casual/everyday use

``
pip install virtualenv
``

Create an Environment with the following commands:

``
python3 -m venv name_of_env
``

and to activate (in each respective folder, Insta_scheduler, myDominosOrder, etc.)

``
source env/bin/activate
``

_____________________________________________________

To install all necessary packages, can also do:

``
pip install -r requirements.txt
``


-----------------------------------------------------

## Instagram Post Scheduler:

``
pip install instapy-cli
``

``
pip install schedule
``

folder with photos should have same file formats (all JPG, jpeg, png, etc)


When running this script, run, ``nohup python insta.py &``, this allows the script to run in the background

To kill the process, go to the folder with the python script is running, type, ``ps ax | grep insta.py`` and kill the process by doing ``kill PID#``. When running the script, it will return a PID number in the console.

-----------------------------------------------------

## My Dominos Order (In Development): 

Before using:

``
pip install pizzapi
``

The pizzapi library from https://github.com/gamagori/pizzapi is not working with a little research from my friend (@Alina569). This is due a indentation error in the order.py.
When you have pip installed pizzapi, go to env/lib/python3.7/site-packages/pizzapi/order.py.

In line 130, add an extra indent to the "return response". There should be two indents on that line.

-----------------------------------------------------
## Email Text Alerts (In Development):

PLEASE YOU .ENV to secure credentials and other personal information!

Before using:

``
pip install twilio
``

``
pip install imapclient
``

May be difficult to implement in a school email or an email with a advanced security settings. It is best to use your personal email. One must have 2-factor authentication within that email. Gmail specifically will not allow you to access at first the email via python script. You first must go to your gmail security settings, enable 2-factor authentication, then add a Gmail Application-Specific Password by adding an application to sign into google with.

First you must input what topic you would like the python script to search for. Then the script accesses your gmail, looks through unseen messages with that "topic to search for" in the subject and body of an email. If an email is unseen and the topic is in the subject/body of the email, you will get a text notification.  

Sign up for a twilio account @ http://twilio.com/ 
Use the free version
Confirm your email, and cell phone number (if that is the number you want to send texts to)
Make sure you get an accountSID, authToken and confirm your Twilio Number (the sender number to your cell phone number)
Go to https://www.twilio.com/docs/sms/quickstart/python and follow the basic code to send your first text to yourself

For security purposes go to https://www.twilio.com/docs/usage/secure-credentials
This page will guide to make environment variables so that you don't need to hard code confidential information in your scripts. It will guide to make updates on your .gitignore so that when you upload your repo, the file with your confidential info does not show up.

When running this script, run, ``nohup python emtext_alerts.py &``, this allows the script to run in the background

To kill the process, go to the folder with the python script is running, type, ``ps ax | grep emtext_alerts.py`` and kill the process by doing ``kill PID#``. When running the script, it will return a PID number in the console.

-----------------------------------------------------
## Restaurant Picker:

No need to argue with friends and loved ones about where you're going to eat! Let Python Decide! 
Here is a script that will randomly pick a restaurant of your choosing in a location of your choosing!
If you live in South Florida or Winston-Salem, there is a random picker of restaurants in those areas.


