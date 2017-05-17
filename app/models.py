from django.db import models

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=225)
    itype = models.CharField(max_length=225)
    niv = models.IntegerField(default=0)
    img_url = models.CharField(max_length=225)

    def as_json(self):
        return dict(
            name_link= self.get_page_link(),
            name=self.name,
            itype=self.itype,
            niv=self.niv,
            img_url=self.img_url)

    def get_page_link(self):
        return '<a href="/app/display_item/'+str(self.id)+'/" >'+self.name+'</a>'

    def get_img(self):
        return '<img src="'+self.img_url+'">'

    def __str__(self):
        return self.name

class FavoriteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username) + " <---> " + str(self.item.name)

class ItemPrice(models.Model):
    date = models.DateTimeField('date published')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.IntegerField(default=-1)
    size = models.IntegerField(default=0)

    def __str__(self):
        return "( "+str(self.item.name) + " x " + str(self.size) + " ) --> " + str(self.price)


    def as_graph_json(self):
        return dict(
            date=self.date.isoformat(),
            price=self.price)
