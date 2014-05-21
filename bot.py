#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
import re
import twikey
import sys

class twitter:
    @staticmethod
    def getAuth():
        auth=tweepy.OAuthHandler(twikey.keys['consumer_key'],
                                 twikey.keys['consumer_secret'])
        auth.set_access_token(twikey.keys['access_token'],
                              twikey.keys['access_token_secret'])
        return auth

    def __init__(self,debug=False,dryrun=False):
        auth=self.getAuth()
        self._api=tweepy.API(auth)
        self._debug=debug
        self._dryrun=dryrun
        self._restricted=False
        self._error=0

    def tweet(self,text,id=None):
        if id:
            self._api.update_status(text,in_reply_to_status_id=id)
        else:
            self._api.update_status(text)
        return True


import gori
def botmain(debug=False,dryrun=False):
    tw=twitter(debug=debug,dryrun=dryrun)
    tw.tweet(gori.gori())


if __name__=="__main__":
    botmain()
