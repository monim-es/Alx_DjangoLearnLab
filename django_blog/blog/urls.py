from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),

    # Blog Posts CRUD
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    # comments
    path("post/<int:post_pk>/comment/new/", views.CommentCreateView.as_view(), name="comment-create"),
    path("post/<int:post_pk>/comment/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("post/<int:post_pk>/comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]





