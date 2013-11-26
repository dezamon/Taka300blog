from django.db import models
from django.core.urlresolvers import reverse
from django import forms
from django.http import HttpResponse
from sky_thumbnails.fields import EnhancedImageField

class Entry(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	pub_date = models.DateField(auto_now=True)
	good = models.CharField(max_length=1000,blank=True)

	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("detail",args=[self.id])

	def testlength(self):
		con = self.content
		if len(con) > 1:
			con = True
		else:
			con = False
		return con

	def amount_of_contents(self):
		num = int(len(self.content))
		return num

	def short_contents(self):
		return ''.join(unicode(self.content).splitlines())[:100]

	def progress(self):
		num = int(len(self.content))
		numper = (float(num) / 300)*100
		text = '%s' % numper
		text = text + "%"
		text = "<div class=\"bar\" style=\"width:%s;\"></div>" % text
		return text

	def check_length_cont(self):
		message = self.content
		num_words = len(message)

		if num_words > 300:
			raise forms.ValidationError("too long")
		return message





