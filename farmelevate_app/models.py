from django.db import models

# Create your models here.

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    usertype = models.CharField(max_length=150)


class Farmer(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    farm_address = models.CharField(max_length=100)
    farm_size = models.CharField(max_length=100)
    farm_type = models.CharField(max_length=100)

class Event(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    Event_title = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Start_date = models.CharField(max_length=100)
    End_date = models.CharField(max_length=100)
    Priority = models.CharField(max_length=100)


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    due_date = models.DateField()
    assigned_worker = models.ForeignKey('Worker', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    Priority = models.CharField(max_length=100)


class Worker(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    country = models.CharField(max_length=100)


class Crop(models.Model):
    type = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    farmer =models.ForeignKey(Farmer, on_delete=models.CASCADE)    
    internal_id=models.CharField( max_length=50)


class plant(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    farmer =models.ForeignKey(Farmer, on_delete=models.CASCADE)
    internal_id=models.CharField( max_length=50)
    location_type = models.CharField(max_length=100)
    planting_fomate = models.CharField(max_length=100)
    Plant_date = models.CharField(max_length=200)
    status = models.CharField(max_length=100)


class harvesting(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    farmer =models.ForeignKey(Farmer, on_delete=models.CASCADE)
    internal_id=models.CharField( max_length=50)
    location_type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    harvesting_date = models.CharField(max_length=200)
    status = models.CharField(max_length=100)



class Animal(models.Model):

    internal_id = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField('Date of Birth')
    status = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    breeding_status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/uploads', blank=True, null=True)
    documents = models.FileField(upload_to='static/uploads', blank=True, null=True)



class Complaint(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    Resolution_expt = models.CharField(max_length=100)
    complaint_text = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.CharField(max_length=100)



class Leave(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    Reason = models.CharField(max_length=100)
    leave_type = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    startdate = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class Transaction(models.Model):
    farmer =models.ForeignKey(Farmer, on_delete=models.CASCADE)

    date = models.DateField()
    payee = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=7)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.FileField(upload_to='static/uploads', blank=True, null=True)



class contact(models.Model):
    Company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


class inventory(models.Model):
    farmer =models.ForeignKey(Farmer, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    ls = models.CharField(max_length=100)


class workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_time = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    no_of_slots = models.CharField(max_length=100)    
    reg_fees = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class worker_join(models.Model):
    workshop =models.ForeignKey(workshop, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    planguage = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)



class payments(models.Model):
    workshop =models.ForeignKey(workshop, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    cname = models.CharField(max_length=100)
    cnumber = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    expiry = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)




class Fertilizer(models.Model):
    soil_type = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    moisture = models.CharField(max_length=100)
    nitrogen = models.CharField(max_length=100)
    potassium = models.CharField(max_length=100)
    phosphorus = models.CharField(max_length=100)
    out = models.CharField(max_length=100)



