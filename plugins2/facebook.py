#!/usr/bin/python                                                                                                                                                                   
# -*- coding: utf-8 -*-    
#by Daniel "P4r4doX" Zaťovič

#This plugin is using "fbconsole" Python library by "pcardune". License :
# Copyright 2010-present Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.



from plugin import *
import fbconsole

class facebookNews(Plugin): 	
	fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
	fbconsole.authenticate()
    	@register("en-US", "(.*facebook.*news.*)")
	def newsFeed(self, speech, language):
                statuses = 10 #how many statuses you want to fetch
                limit = 0
                error = 0
		if (language == "en-US"):	  
			for post in fbconsole.iter_pages(fbconsole.get('/me/home')):
				if(error == 1):
					error = 0
				else :
					limit = limit + 1
				try: 
					post['message']
					ansewer = post['from']['name'] + " wrote : " + post['message'] 
					print ansewer 
					self.say(ansewer)
				except KeyError as (strerror):     
					#print "Key error({0})".format(strerror)
					error = 1
					continue			
				if(limit == statuses): 
					break

class facebookStatus(Plugin): 
    fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins', 'read_stream', 'offline_access']
    fbconsole.authenticate()
    @register("en-US", "(update status.*)|(facebook status.*)|(post status.*)")
    def updateStatus(self, speech, language):
        if (language == "en-US"):
            if (speech.find('Update status') == 0):
                speech = speech.replace('Update status', ' ',1)
            elif (speech.find('Facebook status') == 0):
                speech = speech.replace('Facebook status',' ',1)
            elif (speech.find('Post status') == 0):
                speech = speech.replace('Post status',' ',1)            
            speech = speech.strip()
            if speech == "":
                speech = self.ask("What is your status?")
        self.say("Your status is :")
        self.say(speech);
        ansewer =  self.ask("Are you sure want post it ?")
        if (ansewer == "Yes"):
	  fbconsole.post('/me/feed', {'message': speech})
	  self.say ("Your status was posted !")
	  self.complete_request()
	else :
	  self.say("OK, I wont post it.")
	  self.complete_request()

    @register("en-US", "(.*facebook.*name.*)")
    def facebookName(self, speech, language):
        if (language == "en-US"):
	  self.say(fbconsole.get('/me')['name'])
	  self.complete_request()
	  


	  

    
