#coding:utf-8
import sae

from librarysearch import wsgi                         #将pythondjangotest换成你的应用名

application = sae.create_wsgi_app(wsgi.application)
