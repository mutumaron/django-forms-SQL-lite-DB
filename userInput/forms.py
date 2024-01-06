from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Enter Your Name",max_length=100,error_messages={
#         "required":"Your name must not be empty!",
#         "max_length":"Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=300)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        #exclude = ['owner_comment']
        labels = {
            "first_name":"Enter Your First Name",
            "last_name":"Enter Your Last Name",
            "user_email":"Enter Your Email",
            "user_phone_number":"Enter Your Phone Number",
            "review_text":"Your FeedBack",
            "rating":"Rate us"
        }
        error_message={
            "first_name":{
                "required":"Your name must not be empty!",
                "max_length":"Please Enter a Shorter name!"
            },
            "last_name":{
                "required":"Your name must not be empty!",
                "max_length":"Please Enter a Shorter name!"
            },
              "user_phone_number":{
                "required":"Your phone number must not be empty!",
                "max_length":"Phone number is too long"
            },
              
        }