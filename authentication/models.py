from django.db import models
from django.utils import timezone

# Primero define Country ya que Department lo referencia
class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name or 'Unnamed Country'} {self.abrev or 'Unnamed Country'}{'Active' if self.status else 'Inactive'}"


# Luego Department que depende de Country
class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, default='N/A')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    id_country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='departments'
    )

    def __str__(self):
        return self.name or "Unnamed Department"

# Luego City que depende de Department
class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    id_department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='cities'
    )


    def __str__(self):
        return self.name or "Unnamed City"

# Finalmente User que depende de City
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=False, blank=True, null=True)
    password = models.TextField(default='defaultpassword123')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Agregar la llave foránea a City
    id_city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='users'
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"