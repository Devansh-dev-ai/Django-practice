import hospital_project.views as project_view 
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",project_view.home, name = "Home"),
    path("about/",TemplateView.as_view(template_name = "Templates/about.html"), name = "About"),
    path("service/",TemplateView.as_view(template_name = "Templates/service.html"), name = "Service"),
    path("portfolio/",TemplateView.as_view(template_name = "Templates/portfolio.html"), name = "Portfolio"),
    path("team/",TemplateView.as_view(template_name = "Templates/team.html"), name = "Team"),
    path("blog/",TemplateView.as_view(template_name = "Templates/blog.html"), name = "Blog"),
    ]
