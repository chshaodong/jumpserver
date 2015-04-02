import datetime

from uuidfield import UUIDField

from django.db import models
from juser.models import UserGroup, DEPT
from jasset.models import Asset, BisGroup


class Perm(models.Model):
    user_group = models.ForeignKey(UserGroup)
    asset_group = models.ForeignKey(BisGroup)

    def __unicode__(self):
        return '%s_%s' % (self.user_group.name, self.asset_group.name)


class CmdGroup(models.Model):
    name = models.CharField(max_length=50)
    cmd = models.CharField(max_length=999)
    dept = models.ForeignKey(DEPT)
    comment = models.CharField(blank=True, null=True, max_length=50)

    def __unicode__(self):
        return self.name


class SudoPerm(models.Model):
    name = models.CharField(max_length=20)
    user_runas = models.CharField(max_length=100)
    user_group = models.ManyToManyField(UserGroup)
    asset_group = models.ManyToManyField(BisGroup)
    cmd_group = models.ManyToManyField(CmdGroup)
    comment = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Apply(models.Model):
    uuid = UUIDField(auto=True)
    applyer = models.CharField(max_length=20)
    approver = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    bisgroup = models.CharField(max_length=500)
    asset = models.CharField(max_length=500)
    comment = models.TextField(blank=True, null=True)
    status = models.IntegerField(max_length=2)
    date_add = models.DateTimeField(default=datetime.datetime.now(), null=True)
    date_end = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.applyer
