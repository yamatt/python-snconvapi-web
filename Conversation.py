""" StatusNet Conversation API
    Copyright (C) 2011  Matt (yaMatt) Copperwaite

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from BeautifulSoup import BeautifulSoup
from urllib2 import Request, urlopen
from os import path
import time
from datetime import datetime

class Conversation:
  default_statusnet_instance = "http://identi.ca/notice/%d"
  def __init__ (self, url):
    #bit of an ugly hack, but it's just one way of doing it
    if str(url).isdigit():
      url = self.default_statusnet_instance % int(url)
    #determine if message seed or conversation
    soup = self._soup_(url)
    #test if page is message and has context
    if not self._page_is_conversation_(soup):
      conversation_url = self._find_message_context_(soup)
      soup = self._soup_(conversation_url)
    #build conversation tuple
    self.simple = self._build_conversation_(soup, True)[0]
  
  def _download_page_ (self, url):
    req = Request(url)
    stream = urlopen(req)
    data = stream.read()
    return data
    
  def _soup_ (self, url):
    data = self._download_page_ (url)
    soup = BeautifulSoup(data)
    return soup
    
  def _page_is_conversation_ (self, soup):
    #language problems?
    if soup.html.body.find('div', id='content').h1.text == u'Conversation':
      return True
    return False
    
  def _find_message_context_ (self, soup):
    #probably worth going to API rather than screen scraping again -- oh well
    conversation_url = soup.html.body.find('div', id='content').find('a', attrs={'class' : 'response'})['href']
    return conversation_url
    
  def _build_conversation_ (self, soup, primary=False):
    notice_list = []
    if primary:
      soup = soup.html.body.find('div', id='notices_primary').ol
    notices = soup.findAll('li', recursive=False)
    for notice in notices:
      url = notice.find('div', attrs={'class' : 'entry-content'}).a['href']
      id = path.basename(url) #horrible way of doing this, but it works, if you want to do something quickly, don't use regex
      message_parts = notice.find('div', attrs={'class' : 'entry-title'}).p.findAll(text=True) #also a hack thanks to BeautifulSoup trimming when it shouldn't
      message = ''.join(message_parts)
      username = notice.find('div', attrs={'class' : 'entry-title'}).span.a.span.getText()
      user_url = notice.find('div', attrs={'class' : 'entry-title'}).span.a['href']
      date_str = notice.find('div', attrs={'class' : 'entry-content'}).a.abbr['title'] #2011-06-22T23:36:32+00:00
      time_obj = time.strptime(date_str, u"%Y-%m-%dT%H:%M:%S+00:00") #%z often fails
      date_obj = datetime.fromtimestamp(time.mktime(time_obj))
      notice_data = {
                  'id': id,
                  'url': url,
                  'message': message,
                  'user': {
                    'username': username,
                    'user_url': user_url
                  },
                  'date_native': date_str,
                  'rfc822': date_obj.strftime('%a, %d %b %Y %H:%M:%S'),
                  'iso8601': date_obj.strftime('%Y-%m-%d %H:%M:%S'),
                }
      if bool(notice.ol):
        notice_data['responses'] = self._build_conversation_(notice.ol)
      notice_list.append(notice_data)
    return notice_list
