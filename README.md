# StatusNet Conversation API
This site gives you APIs to access the conversation data locked away in StatusNet sites.
## Usage
It's pretty simple just put the URL of a conversation in to the address bar and it will return you JSON data of the conversation.
You can also use a message as a seed conversation by putting the URL for that message in to the address bar too.
Sorry, no XML yet. You shouldn't be using it anyway. I'll add it in if there are enough requests.
You can use the callback query value to assign a callback function as per the JSONP standard.
### Examples
*   Conversation example
*   Seed message example
## Why
There is currently no API available in StatusNet instances to get conversation data out of them. This is a serious omission and is starting to cause problems in some areas.
I expect in the near future they will release official APIs but until then this will do.
## Background
This was also done in about 7 hours, so please excuse the mess. I'll tidy it as I go.
## How
Screen-scrapping
## Installation
### Requirements
1.  Python 2.6 (not 3 or above)
1.  Flask http://flask.pocoo.org/
### Setup
1.  execute run.py with Python
1.  There is no configuration file so if you want to change anything to do with the Flask setup have a look in run.py. Port, allowed IPs and debug options can be found in the Flask documentation.
## Idiot
I probably could have better spent my time adding the functionality in PHP and submitting a patch. The only problem is I don't understand much PHP and I understand Python very well. So well infact I knocked this all up in one day.
## Can I use it?
Yeah, it's GPL licensed, see below. If you have a StatusNet client and you want to include the Conversation.py you will have to be away of a few things.
*   Conversation.py is initialised with a URL. You will probably want to change this.
*   The date object returned is only a String. This decision was made to make it easier to jsonify it. You will probably want to return the datetime object. It's there waiting for you. Hopefully at some point I'll integrate the two methods.
*   There are a few things that are currently a bit fudged. So be careful with them to code things faster.
*   The returned object after initiated won't give you an array. You have to use the `simple` variable. This was done because future versions will have the `complex` function which will pull down all the data including all User data and all Message data.
*   Of course if you have a better way of doing something, don't hesitate to send me a patch.
## Contact
See my site here [localhosy.net](http://localhosy.net)
## License
I'm putting this all under the GPLv3 license. Code is available on [GitHub](http://github.com/yamatt).
## Ugly!
Yeah, this page is ugly. It's the front end to some API, only developers will use it and they have probably stopped reading by now.
