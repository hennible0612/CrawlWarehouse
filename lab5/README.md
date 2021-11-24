
# Lab 5
1. Add a posts/forms.py
``` shell
from django.forms import ModelForm, Textarea
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
```

2. Create the function 'new' in post/views.py and import the form
``` shell
form = PostForm()

def new(request):
    form = PostForm(request.POST)
    return render(request, "posts/new.html", {"form": form })

```

3. Create a template named 'new.html'
``` shell
{% extends "base.html" %}
{% block title %}Create Post {% endblock %}
{% block content %}
<h2>Create a Post</h2>
<form method="post">
    <table>
        {{ form }}
    </table>
    {% csrf_token %}
    <button type="submit">Create</button>
</form>
{% endblock %}
```

4. Add URL pattern
``` shell
    path('new', new),
```

5. Add additional logic to posts/new
``` shell
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form })
```

6. 
``` shell
#Add widget to make text field look bigger
        widgets = {
            'body': Textarea()
        }
```