from django.db import models

# Create your models here.

class Konsultatsiya(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Teachers/img')

    def __str__(self):
        return self.name


class About(models.Model):
    img1 = models.ImageField('About/img')
    img2 = models.ImageField('About/img')
    img3 = models.ImageField('About/img')
    img4 = models.ImageField('About/img')





class Aboutus(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Aboutus/img')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    teacher = models.CharField(max_length=100)
    soat = models.IntegerField()
    pupil = models.IntegerField()
    img = models.ImageField(upload_to='Course/img')

    def __str__(self):
        return self.name

class Categoriya(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pupils(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Pupil/img')
    fan = models.ForeignKey(Categoriya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pupils2(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Pupil/img')
    fan = models.ForeignKey(Categoriya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pupils3(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Pupil/img')
    fan = models.ForeignKey(Categoriya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pupils4(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Pupil/img')
    fan = models.ForeignKey(Categoriya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Pupils5(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Pupil/img')
    fan = models.ForeignKey(Categoriya, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teamtopbar(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='Teamtopbar/img')
    bio2 = models.TextField()
    img2 = models.ImageField(upload_to='Teamtopbar/img2')


class Itcourse(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Itcourse/img')
    time = models.TimeField()
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kids(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Kids/img')
    time = models.TimeField()
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ittopbar(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Ittopbar/img')

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    img = models.ImageField(upload_to='News/img')

    def __str__(self):
        return self.name
