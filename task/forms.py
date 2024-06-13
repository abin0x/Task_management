from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ['taskTitle', 'taskDescription', 'is_completed']
        fields = '__all__'



# from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta: 
#         model = Post
#         fields = '__all__'