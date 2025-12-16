from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    re_path(r'^about/index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('index/', views.index, name='index'),
    path("blog/", views.page),
    path("blog/page<int:num>/", views.page),
    path("articles/2003/", views.special_case_2003),
 	path("articles/<int:year>/", views.year_archive),
	path("articles/<int:year>/<int:month>/", views.month_archive),
 	path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    path("articles/2003/", views.special_case_2003),
	re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
 	re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.month_archive),
	re_path( r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$", views.article_detail, ),
    path("detail/<int:store_id>/<str:location>/", views.detail, name="detail"),
    path("detail-dict/", views.detailDict, name="detailDict"),
    path('flash/', views.flash_message, name='flash'),
    path('index-template/', views.userinfo, name='index-template'),
    path('tag-example/', views.tag_example, name='tag-example'),
    path('extend-example/', views.test_block, name='extend-example'),
    path('block-super-example/', views.test_block_super, name='block-super-example'),
    path('test-include/', views.test_include, name='test-include'),
]