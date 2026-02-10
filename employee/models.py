from django.db import models

class employees(models.Model):
    Name = models.CharField(max_length=100)
    age = models.IntegerField()
    Salary = models.FloatField()
    join_date = models.DateField()
    post = models.CharField(max_length=100)
    Experience = models.IntegerField(null=True)

    class Meta:
        db_table = "employees"

    def __str__(self):
        return self.Name
