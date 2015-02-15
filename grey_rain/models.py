from django.db import models

# Create your models here.
class Customer(models.Model):
	cust_id=models.AutoField(primary_key=True)
	cust_email=models.CharField(max_length=32, verbose_name='Email Address')
	cust_password=models.CharField(max_length=32, verbose_name='Password')
	cust_prefix=models.CharField(max_length=10, choices=(('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')), verbose_name='Prefix')
	cust_first_name=models.CharField(max_length=32, verbose_name='First Name')
	cust_middle_name=models.CharField(max_length=32, verbose_name='Middle Name')
	cust_last_name=models.CharField(max_length=32, verbose_name='Last Name')
	cust_gender=models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')), verbose_name='Gender')
	cust_birth_date=models.DateField(verbose_name='Birth date')
	cust_phone_number=models.CharField(max_length=20, verbose_name='Phone Number')
	cust_alt_phone=models.CharField(max_length=20, verbose_name='Alt. Phone Number')
	cust_home_address=models.CharField(max_length=64, verbose_name='Home Address')
	cust_alt_home=models.CharField(max_length=64, verbose_name='Provincial Address')
	def __str__(self):
		return self.cust_id+':'+self.cust_email;
	
class ItemCategory(models.Model):
	ic_id=models.AutoField(primary_key=True)
	ic_name=models.CharField(max_length=32, verbose_name='Name')
	ic_desc=models.TextField(verbose_name='Description')
	def __str__(self):
		return self.ic_id+':'+self.ic_name;

class ItemSubcategory(models.Model):
	isc_id=models.AutoField(primary_key=True)
	isc_name=models.CharField(max_length=32, verbose_name='Name')
	isc_desc=models.TextField(max_length=32, verbose_name='Description')
	isc_category=models.ForeignKey(ItemCategory)
	def __str__(self):
		return self.isc_id+':'+self.isc_name;
		
class Item(models.Model):
	item_id=models.AutoField(primary_key=True)
	item_code=models.CharField(max_length=8, verbose_name='Code')
	item_name=models.CharField(max_length=32, verbose_name='Name')
	item_price=models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Price')
	item_short_desc=models.CharField(max_length=32, verbose_name='Short Description')
	item_long_desc=models.TextField(verbose_name='Long Description')
	item_date_added=models.DateField(verbose_name='Date Added', auto_now=True)
	item_subcategory=models.ForeignKey(ItemSubcategory)
	item_rental_day=models.IntegerField(verbose_name='Rental Day')
	item_img_sm=models.ImageField(verbose_name='Image(Small)', upload_to='utopia/templates/item_sm', blank=True)
	item_img_lg=models.ImageField(verbose_name='Image(Large)', upload_to='utopia/templates/item_lg', blank=True)
	item_img_extra1=models.ImageField(verbose_name='Image Extra 1', upload_to='utopia/templates/item_extra_1', blank=True)
	item_img_extra2=models.ImageField(verbose_name='Image Extra 2', upload_to='utopia/templates/item_extra_2', blank=True)
	item_img_extra3=models.ImageField(verbose_name='Image Extra 3', upload_to='utopia/templates/item_extra_3', blank=True)
	def __str__(self):
		return self.item_id+':'+self.item_name;
	
class ItemVariant(models.Model):
	ivar_id=models.AutoField(primary_key=True)
	ivar_item=models.ForeignKey(Item)
	ivar_size=models.CharField(verbose_name='Size', max_length=20, choices=(('Extra Small', 'Extra Small'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large')))
	ivar_color=models.CharField(max_length=36, verbose_name='Color', blank=True)
	ivar_qty=models.IntegerField(verbose_name='Quantity', default=0)
	def __str__(self):
		return self.ivar_id+':'+self.ivar_size;

class Carousel(models.Model):
    caro_id=models.AutoField(verbose_name='ID', primary_key=True)
    caro_name=models.CharField(verbose_name='Name', max_length=36)
    caro_desc=models.TextField(verbose_name='Description', max_length=100)
    caro_img=models.ImageField(verbose_name='Image', upload_to='utopia/templates/carousel')
    caro_link=models.URLField(verbose_name='Landing page')
    def __str__(self):
        return self.caro_id.__str__()+' '+self.caro_name;
