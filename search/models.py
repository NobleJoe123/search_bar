from django.db import models
import random
import hashlib
import string

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phonenum = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='search_images/', blank=True, null=True)
    ssn = models.CharField(max_length=20, unique=True, blank=True, null=True)


    def __str__(self):
        return f"{self.name} - SSN: {self.ssn}"

    def save(self, *args, **kwargs):
        if not self.ssn:  # Only generate SSN if it doesn't already exist
            self.ssn = self.generate_ssn()
        super(Person, self).save(*args, **kwargs)

    def generate_ssn(self):

        name_part = self.get_name_part(self.name)
        phone_part = self.get_phone_part(self.phonenum)
        gender_part = self.get_address_part(self.sex)
        address_part = self.get_address_part(self.address)
        age_part = str(self.age).zfill(2)
        # Use a combination of name, phone number, and age to create a hash for SSN
        unique_data = f"{name_part}{phone_part}{age_part}{gender_part}{address_part}"
        hash_object = hashlib.sha256(unique_data.encode())
        # Get the first 9 digits of the hash, add dashes like SSN format: XXX-XX-XXXX
        ssn_raw = hash_object.hexdigest().upper()
        
        part1 = name_part[:1] + phone_part[:2]  # 1 letter from name + 2 digits from phone
        part2 = age_part[:2] + gender_part[:1]  # 2 digits from age
        part3 = address_part[:1] + ssn_raw[:2] 
        
        return f"{part1}-{part2}-{part3}"
    
    
    
    def get_name_part(self, name):
        """Extract initials from the name."""
        return ''.join([c for c in name if c.isalpha()]).upper()[:2]

    def get_phone_part(self, phonenum):
        """Extract the last 3 digits of the phone number."""
        return ''.join([c for c in phonenum if c.isdigit()])[-3:]
    

    def get_address_part(self, address):
        """Extract the first alphabetic character from the address."""
        return ''.join([c for c in address if c.isalpha()]).upper()[:1]



class BankDetail(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bank_detail')
    bank_used = models.CharField(max_length=255)
    bvn = models.CharField(max_length=11, unique=True)
    nin = models.CharField(max_length=11, unique=True)
    account_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.person.name} - {self.bank_used}'
    










    

# class SocialDetail(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='social_detail')
#     bank_used = models.CharField(max_length=255)
#     bvn = models.CharField(max_length=11, unique=True)
#     nin = models.CharField(max_length=11, unique=True)
#     account_number = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return f'{self.person.name} - {self.bank_used}'

























    # def generate_ssn(self):
    #     # Use a combination of name, phone number, and age to create a hash for SSN
    #     unique_data = f"{self.name}{self.phonenum}{self.age}{self.sex}{self.address}{random.randint(100, 999)}"
    #     hash_object = hashlib.sha256(unique_data.encode())
    #     # Get the first 9 digits of the hash, add dashes like SSN format: XXX-XX-XXXX
    #     ssn_raw = str(int(hash_object.hexdigest(), 16))[:9]
    #     return f"{ssn_raw[:3]}-{ssn_raw[3:5]}-{ssn_raw[5:]}"





    # def __str__(self):
    #     return f"{self.name} - SSN: {self.ssn}"
    
    # def generate_ssn(self):
    #     # Use a combination of name, phone number, and age to create a hash for SSN
    #     unique_data = f"{self.name}{self.phonenum}{self.age}{self.sex}{random.randint(100, 999)}"
    #     hash_object = hashlib.sha256(unique_data.encode())
    #     # Get the first 9 digits of the hash, add dashes like SSN format: XXX-XX-XXXX
    #     ssn_raw = str(int(hash_object.hexdigest(), 16))[:9]
    #     return f"{ssn_raw[:3]}-{ssn_raw[3:5]}-{ssn_raw[5:]}"
    

    # def save(self, *args, **kwargs):
    #     if not self.ssn:  # Only generate SSN if it doesn't already exist
    #         self.ssn = self.generate_ssn()
    #     super(Person, self).save(*args, **kwargs)

    


