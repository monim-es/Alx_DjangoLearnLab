from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class PostForm(forms.ModelForm):
    # user-friendly tags input (comma-separated)
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g. django, tips, tutorial).",
        widget=forms.TextInput(attrs={"placeholder": "tag1, tag2, tag3"})
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def clean_tags(self):
        raw = self.cleaned_data.get("tags", "")
        # normalize: split by comma, strip whitespace, remove empties, lower-case
        tag_names = [t.strip() for t in raw.split(",") if t.strip()]
        return tag_names


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment..."}),
        }

    def clean_content(self):
        c = self.cleaned_data.get("content", "").strip()
        if not c:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(c) > 5000:
            raise forms.ValidationError("Comment is too long.")
        return c