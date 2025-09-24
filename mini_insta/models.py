from django.db import models

# Create your models here.
class Profile(models.Model):
    # create a database that contains these rows
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=100)
    profile_image_url = models.URLField()
    bio_text = models.TextField()
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # when calling the model, it will display username
        return self.username
    
class Message(models.Model):
    display_name = models.CharField(max_length=100)
    message = models.TextField()
    receiver = models.ForeignKey(
        "Profile", 
        on_delete=models.CASCADE, 
        related_name="received_messages"
    )
    likes = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.display_name} → {self.receiver}"