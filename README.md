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

Instagram post scheduler:

``
pip install instapy-cli
``

``
pip install schedule
``

folder with photos should have same file formats (all JPG, jpeg, png, etc)


When running this script, run, "nohup python insta.py &", this allows the script to run in the background

-----------------------------------------------------

My Dominos Order: 

Before using:

``
pip install pizzapi
``

The pizzapi library from https://github.com/gamagori/pizzapi is not working with a little research from my friend. This is due a indentation error in the order.py.
When you have pip installed pizzapi, go to env/lib/python3.7/site-packages/pizzapi/order.py
In line 130, add an extra indent to the "return response". There should be two indents on that line.
