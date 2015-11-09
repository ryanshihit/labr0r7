from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythondjangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'search.views.index'),#主页用于显示图书
    url(r'^addauthorpre/$', 'search.views.addauthorpre'),#显示添加作者页面
    url(r'^addauthor/$', 'search.views.addauthor'),#执行添加作者
    url(r'^addbookpre/$', 'search.views.addbookpre'),#显示添加书籍页面
    url(r'^addbook/$', 'search.views.addbook'),#执行添加数据
    url(r'^showbook/$', 'search.views.showbook'),#显示图书
    url(r'^showauthor/$', 'search.views.showauthor'),#显示作者
    url(r'^showbook/delbook$', 'search.views.delbook'),#删除图书
    url(r'^lackauthor$', 'search.views.showerror'),#显示错误
    url(r'^updatebook/$', 'search.views.updatebook'),#执行更新图书
    url(r'^searchauthor/$', 'search.views.searchauthor'),#搜索作者
    url(r'^showbook/del/(.+)/$', 'search.views.delbook'),#删除图书
    url(r'^showbook/upd/(.+)/$', 'search.views.updatebookpre'),#显示更新图书页面
    url(r'^bookdetail/(.+)/$', 'search.views.showbookinfo'),#显示图书详细信息
    url(r'^authordetail/(.+)/$', 'search.views.showauthorinfobybook'),#显示作者详细信息
    url(r'^showauthor/authordetail1/(.+)/$', 'search.views.showauthorinfobyself'),#显示作者详细信息
    url(r'^initial/$', 'search.views.initial'),#初始化页面(内部测试)
    url(r'^admin/', include(admin.site.urls)),
    
)
