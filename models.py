from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_url = models.URLField()  # पोस्टर के लिए
    backdrop_url = models.URLField(blank=True, null=True)  # बड़े बैनर स्लाइडर के लिए फोटो
    video_url = models.URLField()
    genre = models.CharField(max_length=100)  # Action, Comedy, Drama आदि
    rating = models.FloatField(default=0.0)
    is_featured = models.BooleanField(default=False)  # क्या इसे ऊपर बड़े स्लाइडर में दिखाना है?
    is_premium = models.BooleanField(default=False)  # True मतलब पेड/अर्निंग मूवी, False मतलब फ्री

    def __str__(self):
        return self.title
