from django.db import models
from django.urls import reverse


class ieltsstories(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IELTSStories'
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('ieltsstories-detail', args=[str(self.id)])
    def __str__(self):
        return self.title


class ieltstest(models.Model):
    sublevel = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    qnumber = models.IntegerField( blank=True, primary_key=True)  # Field name made lowercase.
    qcontent = models.TextField( blank=True, null=True)  # Field name made lowercase.
    answera = models.TextField( blank=True, null=True)  # Field name made lowercase.
    answerb = models.TextField( blank=True, null=True)  # Field name made lowercase.
    answerc = models.TextField(blank=True, null=True)  # Field name made lowercase.
    answerd = models.TextField(blank=True, null=True)  # Field name made lowercase.
    correctanswer = models.TextField( blank=True, null=True)  # Field name made lowercase.
    passed = models.IntegerField( blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IELTSTest'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('test-detail', args=[str(self.id)])

    def __str__(self):
        return self.sublevel
