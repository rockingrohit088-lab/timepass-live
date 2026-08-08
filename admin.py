from django.contrib import admin
from .models import Movie

# एडमिन पैनल में मूवी देखने के लिए रजिस्टर करें
admin.site.register(Movie)
