from django.db import models

class User (models.Model):
    PUBLIC_ACCOUNT = 1
    PRIVATE_ACCOUNT = 2

    class Meta:
        db_table = "user"

    userName = models.CharField(max_length = 255, null = True)
    email = models.CharField(max_length = 255, null = False)
    password = models.CharField(max_length = 255, null = True)
    type = models.IntegerField()

    def delete(self, using = None, keep_parents = False):
        self.save()

    @property
    def is_anonymous(self):
        return True

    @property
    def is_authenticated(self):
        return True