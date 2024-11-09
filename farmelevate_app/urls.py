"""farmelevate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('add_farmer',views.add_farmer),
    path('loginss',views.loginss),
    path('farmer_home',views.farmer_home), 
    path('submit_event', views.submit_event, name='submit_event'),
    path('farmer_view_event', views.farmer_view_event, name='farmer_view_event'),
    
    path('event_delete/<id>',views.event_delete),
    path('submit_event_update/<id>',views.submit_event_update),
    path('add_worker',views.add_worker),
    path('worker_home',views.worker_home),
    path('task_form',views.task_form),
    path('admin_view_task',views.admin_view_task),

    
    path('task_update/<id>',views.task_update),
    path('task_delete/<id>',views.task_delete),
    path('task_view',views.task_view),
    path('crop_add',views.crop_add),
    path('admin_view_crop',views.admin_view_crop),

    

    path('admin_add_workshop',views.admin_add_workshop),
    path('admin_view_workshop',views.admin_view_workshop),
    path('workshop_update/<id>',views.workshop_update),
    path('workshop_delete/<id>',views.workshop_delete),



    path('worker_view_workshops',views.worker_view_workshops),

    path('workshop_join/<id>/<reg_fees>',views.workshop_join),
    path('customer_payment/<id>/<reg_fees>',views.customer_payment),

    path('worker_plant_report',views.worker_plant_report),
    path('worker_harvest_report',views.worker_harvest_report),
    path('worker_task_report',views.worker_task_report),

    path('workshop_expire/<id>',views.workshop_expire),



    path('worker_workshop_report',views.worker_workshop_report),
    path('admin_workshop_reportss',views.admin_workshop_reportss),

    
    path('crop_update/<id>',views.crop_update),
    path('crop_delete/<id>',views.crop_delete),
    path('plant_add/<id>/<types>/<variety>/<internal_id>',views.plant_add),
    path('plant_update/<id>',views.plant_update),
    path('plant_delete/<id>',views.plant_delete), 
    path('harvest_add/<id>/<types>/<variety>/<internal_id>',views.harvest_add),
    path('harvesting_update/<id>',views.harvesting_update),
    path('harvesting_delete/<id>',views.harvesting_delete), 
    path('livestock_add',views.livestock_add),
    path('admin_view_live',views.admin_view_live),

    
    path('livestock_delete/<id>',views.livestock_delete),
    path('animal_update/<id>',views.animal_update),
    path('bill_add',views.bill_add),
    path('admin_view_tra',views.admin_view_tra),
    

    
    path('tranction_update/<id>',views.tranction_update),
    path('bill_delete/<id>',views.bill_delete),
    path('send_complaint',views.send_complaint),
    path('view_complaint',views.view_complaint),
    path('complaint_report',views.complaint_report),


    
    path('send_reply/<id>',views.send_reply),
    path('send_leave',views.send_leave),
    path('leave_request_report',views.leave_request_report),


    
    path('worker_view_assigned_work',views.worker_view_assigned_work),
    path('task_completed/<id>',views.task_completed),
    path('inventory_add',views.inventory_add),
    path('admin_view_inventory',views.admin_view_inventory),


    
    path('inventory_delete/<id>',views.inventory_delete),
    path('inventory_update/<id>',views.inventory_update),
    path('events_report',views.events_report),

    path('contact_add',views.contact_add),
    path('admin_view_contact',views.admin_view_contact),
    path('update_contact/<id>',views.update_contact),

    path('contact_delete/<id>',views.contact_delete),
    path('view_worker',views.view_worker),
    path('w_accept/<id>',views.w_accept),
    path('w_reject/<id>',views.w_reject),
    path('worker_plant',views.worker_plant),
    path('planted/<id>',views.planted),
    path('worker_harvest',views.worker_harvest),
    path('harvestingr/<id>',views.harvestingr),
    path('planted_rep',views.planted_rep),
    path('harvesting_rep',views.harvesting_rep),

    path('admin_view_leave',views.admin_view_leave),
    path('fertilizer',views.fertilizer),


    path('l_accept/<id>',views.l_accept),
    path('l_reject/<id>',views.l_reject),

    path('admin_pl',views.admin_pl),
    path('admin_task',views.admin_task),
    path('admin_live_reportss',views.admin_live_reportss),
    path('admin_invent_report',views.admin_invent_report),
    path('admin_view_complaint',views.admin_view_complaint),
    path('admin_trans_report',views.admin_trans_report),
    path('admin_leave_report',views.admin_leave_report),
    path('admin_view_pl',views.admin_view_pl),
    path('add_todoss',views.add_todoss),
    path('worker_add_todoss',views.worker_add_todoss),

    


    

]
