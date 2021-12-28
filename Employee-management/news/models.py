from django.db import models
from django.utils.translation import gettext as _
from employees.models import User
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from colorfield.fields import ColorField
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel



class BirthdayPage(Page):

    birthday_date = models.DateField(auto_now_add=False)
    employee_name = models.CharField(max_length=500)
    emp_image = models.ImageField(upload_to="upload/")
    body = RichTextField()

    content_panels = Page.content_panels + [
    FieldPanel('employee_name'),
    FieldPanel('emp_image'),
    FieldPanel('birthday_date'),
    RichTextFieldPanel('body')
    ] 
    
    
class UpcomingHolidayPage(Page):

    date = models.DateField(auto_now_add=False)
    name =  models.CharField(max_length=500)
    emp_image = models.ImageField(upload_to="upload/")
    body = RichTextField()

    content_panels = Page.content_panels + [
    FieldPanel('name'),
    FieldPanel('emp_image'),
    FieldPanel('date'),
    
    RichTextFieldPanel('body')
    
    ] 

class NewsAddPage(Page):

    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    from_time = models.TimeField(auto_now_add=False)
    to_time = models.TimeField(auto_now_add=False)
    emp_image = models.ImageField(upload_to="upload/")
    body = RichTextField()
    color = ColorField()

    content_panels = Page.content_panels + [
    FieldPanel('event_name'),
    FieldPanel('event_date'),
    FieldPanel('from_time'),
    FieldPanel('to_time'),
    FieldPanel('emp_image'),
    NativeColorPanel('color'),
    RichTextFieldPanel('body')]
    
    
class NewjoineePage(Page):
    
    name = models.CharField(_("Employee Name"),max_length=500)
    designation= models.CharField(_("Emploee Designation"),max_length=255)
    emp_image=models.ImageField(upload_to="upload/")
    body = RichTextField()
    joining_date = models.DateField()
    

    content_panels = Page.content_panels + [
    FieldPanel('name'),
    FieldPanel('designation'),
    FieldPanel('emp_image'),
    FieldPanel('joining_date'),
    
    RichTextFieldPanel('body')]
