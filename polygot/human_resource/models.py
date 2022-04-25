from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=200)
    staff_id = models.CharField("Staff ID", max_length=200, null=True, blank=True)
    position = models.CharField(choices=(("Backend Developer", "Backend Developer"),
                                        ("Frontend Developer", "Frontend Developer"),
                                        ("Fullstack Developer", "Fullstack Developer")), max_length=100, null=True, blank = True)
    salary = DecimalField(max_digits=10, decimal_places=2)
    date_hired = models.DateTimeField()
    note = models.CharField(max_length=600, null=True, blank = True)

    def __str__(self):
        return self.name
    
    def total_load(self):
        load = 0
        for x in self.stafftimeallocation_set.all():
            load = load + x.time
        return round(float(load), 2)

    def squads(self):
        arr = []
        for x in self.stafftimeallocation_set.all():
            arr.append(x.squad.name + "(" + str(x.time) + ")")
        return arr

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600, null=True, blank = True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    note = models.CharField(max_length=600, null=True, blank = True)

    def __str__(self):
        return self.name
    
    def squads(self):
        arr = []
        for squad in self.squad_set.all():
            arr.append(squad.name)
        return arr

class Squad(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600, null=True, blank = True)
    
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.CharField(max_length=600, null=True, blank = True)
	
    def __str__(self):
        return self.name

    def staffs(self):
        result = ""
        count = 0
        for x in self.stafftimeallocation_set.all():
            result = result + (x.staff.name + "(" + str(x.time) + "), ")
            count = count + 1
            if (count == 50):
                result = result + "...  "
                break			
        return result[:-2]
    
    def budget(self):
        budget_money = 0.0
        for x in self.stafftimeallocation_set.all():
            budget_money = x.staff.salary * x.time
        return round(float(budget_money), 2)


class StaffTimeAllocation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)
    time = models.DecimalField(max_digits=3, decimal_places=2)
    def __str__(self):
        return ("Assignment " + str(self.id))	