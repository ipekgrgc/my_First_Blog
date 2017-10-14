from django.db import models
from django.utils import timezone



class Post(models.Model): #Modeli tanımlar ve nesnedir
    author = models.ForeignKey('auth.User') #Başka bir model ile bağlantı
    title = models.CharField(max_length=200) #Kısıtlı uzunlukta metin tanımlar
    text = models.TextField() #Uzun metinleri tanımlar
    date_Of_Creation = models.DateTimeField(default=timezone.now) #Gün ve saati tanımlar
    date_Of_Publish = models.DateTimeField(blank=True, null=True)

    def publish(self): #yayınlama methodu
        self.date_Of_Publish = timezone.now()
        self.save()

    def __str__(self): #Post başlığının yazısı elde edilir
        return self.title
