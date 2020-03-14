from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path(
        '', 
        # views.index,
        views.IndexView.as_view(), 
        name="index"
        ),
    # ex: /polls/5/
    # The URL is not hardcoded into the template, the template references the URL with the name attribute
    path(
        # This URL can be changed to anything e.g "specific/<int:pk> no problemo"
        "<int:pk>/",
        # views.detail,
        views.DetailView.as_view(), 
        name="detail"
        ),

    # ex: /polls/5/results/
    path(
        "<int:pk>/results/", 
        # views.result, 
        views.ResultsView.as_view(),
        name="results"
        ),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]