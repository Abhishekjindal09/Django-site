from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(User, blank=True,null=True)
    remind = models.BooleanField(default=False)

    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u" - " + self.title
        else:
            return unicode(self.creator) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return "<i>%s</i> - %s" % (self.title, self.snippet)
        else:
            return self.title
        short.allow_tags = True

    class Meta:
        verbose_name_plural = "entries"
        TestMode = True
def some_function():
  global TestMode
  TestMode = False
some_function()
print(TestMode) <--Returns False
var_one = 123
def func_one(var_one):
    var_one = 234
    var_three = 'abc'

var_two = 456


def func_two():
    var_four = 123
    print(dir())
func_two()
