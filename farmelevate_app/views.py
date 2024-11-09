from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect

from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import *
from .fertilizerpredict import *

from datetime import date, timedelta
def home(request):
    return render(request,'Home.html')

def loginss(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['password']
        print(uname, pwd)
        try:
            lg = Login.objects.get(username=uname, password=pwd)
            print(lg, "........................")
            request.session['login_id'] = lg.pk
            lid = request.session['login_id']
            if lg.usertype == 'admin':
                request.session['lid'] = lg.pk
                # ob1 = auth.authenticate(username='admin', password='MyPassword')
                # if ob1 is not None:
                #     auth.login(request, ob1)
                #     print("Haiiiiiiiiiiiiiiiiiiii")
                #     print("Haiiiiiiiiiiiiiiiiiddddddiii")
                return HttpResponse("<script>alert('login successfully!');window.location='/farmer_home';</script>")
            # if lg.usertype == 'farmer':
            #     qq = Farmer.objects.filter(login_id=lid)
            #     if qq:
            #         farmer_id = qq[0].id
            #         request.session['farmer_id'] = farmer_id
            #         # ob1 = auth.authenticate(username='admin', password='MyPassword')
            #         # if ob1 is not None:
            #         #     auth.login(request, ob1)
            #         # print(request.session['provider_id'],'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            #         return HttpResponse("<script>alert('login successfully!');window.location='/farmer_home';</script>")
            elif lg.usertype == 'worker':
                qq = Worker.objects.filter(login_id=lid)
                if qq:
                    w_id = qq[0].id
                    request.session['w_id'] = w_id
                    # ob1 = auth.authenticate(username='admin', password='MyPassword')
                    # if ob1 is not None:
                    #         auth.login(request, ob1)
                    # print(request.session['user_id'],'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
                    print(request.session['w_id'])
                    return HttpResponse("<script>alert('login successfully!');window.location='/worker_home';</script>")

        except:
            return HttpResponse("<script>alert('login Failed...!!!!');window.location='/loginss';</script>")
    return render(request, 'login.html')


# def add_farmer(request):

#     q=Farmer.object.get(login_id=request.session['login_id'])




#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         dob = request.POST.get('dob')
#         gender = request.POST.get('gender')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         country = request.POST.get('country')
#         farm_name = request.POST.get('farm_name')
#         farm_address = request.POST.get('farm_address')
#         farm_size = request.POST.get('farm_size')
#         farm_type = request.POST.get('farm_type')
#         uname = request.POST.get('uname')
#         pwd = request.POST['pwd']          
#         try:
#             obj=Login.objects.get(username=uname)
#             return HttpResponse("<script>alert('Username Already Exists!!');window.location='/user_register'</script>")
#         except:
#             lid=Login(username=uname,password=pwd,usertype='farmer')
#             lid.save()
#             farmer = Farmer(
#                 first_name=first_name,
#                 last_name=last_name,
#                 dob=dob,
#                 gender=gender,
#                 phone=phone,
#                 email=email,
#                 address=address,
#                 country=country,
#                 farm_name=farm_name,
#                 farm_address=farm_address,
#                 farm_size=farm_size,
#                 farm_type=farm_type,
#                 login_id=lid.pk
#             )
#             farmer.save()
#             return HttpResponse("<script>alert('Register Successfully');window.location='/'</script>")



#     return render(request, 'farm_reg.html',{'q':q})



# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Farmer, Login

def add_farmer(request):
    # Check if the farmer exists based on the session login ID
    try:
        q = Farmer.objects.get(login_id=request.session['login_id'])
    except Farmer.DoesNotExist:
        q = None

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        farm_name = request.POST.get('farm_name')
        farm_address = request.POST.get('farm_address')
        farm_size = request.POST.get('farm_size')
        farm_type = request.POST.get('farm_type')
        # uname = request.POST.get('uname')
        # pwd = request.POST['pwd']

        if q:
            # Update existing farmer
            q.first_name = first_name
            q.last_name = last_name
            q.dob = dob
            q.gender = gender
            q.phone = phone
            q.email = email
            q.address = address
            q.country = country
            q.farm_name = farm_name
            q.farm_address = farm_address
            q.farm_size = farm_size
            q.farm_type = farm_type
            q.save()
            return HttpResponse("<script>alert('Farmer Updated Successfully');window.location='/farmer_home'</script>")
        else:
            # Check if username already exists
            try:
                obj = Login.objects.get(username=uname)
                return HttpResponse("<script>alert('Username Already Exists!!');window.location='/farmer_home'</script>")
            except Login.DoesNotExist:
                # Create new farmer
                lid = Login(username=uname, password=pwd, usertype='farmer')
                lid.save()
                farmer = Farmer(
                    first_name=first_name,
                    last_name=last_name,
                    dob=dob,
                    gender=gender,
                    phone=phone,
                    email=email,
                    address=address,
                    country=country,
                    farm_name=farm_name,
                    farm_address=farm_address,
                    farm_size=farm_size,
                    farm_type=farm_type,
                    login_id=lid.pk
                )
                farmer.save()
                return HttpResponse("<script>alert('Register Successfully');window.location='/'</script>")

    return render(request, 'farm_reg.html', {'q': q})



def farmer_home(request):
    return render(request, 'farmer_home.html')


def submit_event(request):
    # q=Event.objects.all()
    if request.method == 'POST':
        event_title = request.POST['name']
        description = request.POST['desc']
        start_date = request.POST['sdate']
        end_date = request.POST['edate']
        priority = request.POST['priority']

        # Assuming you have an Event model with these fields
        Event.objects.create(
            Event_title=event_title,
            Description=description,
            Start_date=start_date,
            End_date=end_date,
            Priority=priority,
            farmer_id=request.session['login_id']
        )
        return redirect('submit_event')  # Redirect to an event list page or another appropriate page
    # return render(request, 'farmer_event.html',{'q':q})
    return render(request, 'farmer_event.html')

def farmer_view_event(request):

    q=Event.objects.all()
        
    return render(request,'farmer_view_event.html',{'q':q})



def submit_event_update(request,id):

    q=Event.objects.all()
    qa=Event.objects.get(id=id)

    if 'update' in request.POST:
      
            event_title = request.POST['name']
            description = request.POST['desc']
            start_date = request.POST['sdate']
            end_date = request.POST['edate']
            priority = request.POST['priority']
           
            qa.Event_title=event_title
            qa.Description=description
            qa.Start_date=start_date
            qa.End_date=end_date
            qa.Priority=priority
            qa.save()
            return HttpResponse("<script>alert('Successfully Updated');window.location='/farmer_view_event'</script>")

        
    return render(request,'farmer_view_event.html',{'q':q,'qa':qa})

def event_delete(request,id):
    qa=Event.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/submit_event'</script>")



    
#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully deleted 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/submit_event';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)




# def list_farmers(request):
#     farmers = Farmer.objects.all()
#     return render(request, 'list_farmers.html', {'farmers': farmers})





def task_form(request):
    today = date.today().strftime('%Y-%m-%d')

    workers = Worker.objects.all()
    # task = Task.objects.all()

    if request.method == 'POST':
        # Handle form submission
        task_name = request.POST['tname']
        description = request.POST['desc']
        assigned_worker_id = request.POST['worker']
        due_date = request.POST['ddate']
        priority = request.POST['priority']
        
        # Assuming you have a Task model to save the data
        # assigned_worker = Worker.objects.get(id=assigned_worker_id)
        Task.objects.create(
            task_name=task_name,
            description=description,
            assigned_worker_id=assigned_worker_id,
            due_date=due_date,
            Priority=priority,
            farmer_id=request.session['login_id'],
            status='pending'
        )

        return HttpResponse("<script>alert('Successfully Added');window.location='/task_form'</script>")



    return render(request, 'farmer_task.html', {'w':workers,'today':today})


def add_worker(request):
    today = date.today().strftime('%Y-%m-%d')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        department = request.POST.get('department')
        position = request.POST.get('position')
        employee_id = request.POST.get('employee_id')
        uname = request.POST.get('uname')
        pwd = request.POST['pwd']
        status='pending'     
        # try:
        #     obj=Login.objects.get(username=uname)
        #     return HttpResponse("<script>alert('Username Already Exists!!');window.location='/'</script>")
        # except:
        lid=Login(username=uname,password=pwd,usertype=status)
        lid.save()
        wk = Worker(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            country=country,
            login_id=lid.pk,
            emp_id=employee_id,
            department=department,
            position=position

        )
        wk.save()
        return HttpResponse("<script>alert('Register Successfully');window.location='/loginss'</script>")
    return render(request, 'worker_reg.html',{'today':today})


def worker_home(request):
    return render(request, 'worker_home.html')


# def admin_view_task(request):

#     q=Task.objects.all()
    
    
#     return render(request,'admin_view_task.html',{'q':q})


# def admin_view_task(request):

#     q = Task.objects.all()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(task_name=sname)
#             q |= Q(Priority=sname)
#             q |= Q(assigned_worker__first_name=sname)
#             q |= Q(status=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(due_date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(due_date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(due_date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         q = Task.objects.filter(q)










#     paginator = Paginator(q, 5)
#     page_number = request.GET.get('page')
#     q= paginator.get_page(page_number)
    
#     for index, item in enumerate(q.object_list, start=q.start_index()):
#         item.row_number = index
    
#     context = {
#         'q':q  # Use page_obj instead of q
#     }
#     return render(request, 'admin_view_task.html', context)

def admin_view_task(request):
    # Initial query to get all tasks
    query = Task.objects.all()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        search_conditions = Q()

        if sname:
            search_conditions |= (
                Q(task_name__icontains=sname) |
                Q(Priority__icontains=sname) |
                Q(assigned_worker__first_name__icontains=sname) |
                Q(status__icontains=sname)
            )

            # Additionally check if 'sname' can be interpreted as a date and apply to due_date field
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(due_date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(due_date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(due_date__lte=end_date)
            except ValueError:
                pass

        # Apply the search conditions to the queryset
        query = Task.objects.filter(search_conditions)

    # Pagination
    paginator = Paginator(query, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    paginated_tasks = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(paginated_tasks.object_list, start=paginated_tasks.start_index()):
        item.row_number = index  # Row numbers starting from 1

    context = {
        'q': paginated_tasks  # Use paginated_tasks instead of query
    }
    return render(request, 'admin_view_task.html', context)
 

def task_update(request,id):

    # q=Task.objects.all()
    qa=Task.objects.get(id=id)
    workers = Worker.objects.all()
    if 'update' in request.POST:
      
        task_name = request.POST['name']
        description = request.POST['desc']
        assigned_worker_id = request.POST['worker']
        due_date = request.POST['edate']
        priority = request.POST['priority']
           
        qa.task_name=task_name
        qa.description=description
        qa.due_date=due_date
        qa.assigned_worker_id=assigned_worker_id
        qa.Priority=priority
        qa.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_view_task'</script>")


    return render(request,'farmer_task.html',{'qa':qa,'w':workers})

def task_delete(request,id):
    qa=Task.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_task'</script>")


    
#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully deleted 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/task_form';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)

def task_view(request):
    qa=Task.objects.all()
    return render(request,'farmer_view_task.html',{'q':qa})


def admin_add_workshop(request):

    # Crop1 = Crop.objects.all()

    if request.method == 'POST':
        # Handle form submission
        wt = request.POST['wt']
        de = request.POST['de']
        dt = request.POST['dt']
        st = request.POST['st']
        lo = request.POST['lo']
        rf = request.POST['rf']
        workshop.objects.create(
            title=wt,
            description=de,
            date_time=dt,
            location=lo,
            no_of_slots=st,
            reg_fees=rf,
            status='pending'
        )
        return HttpResponse("<script>alert('Successfully Added');window.location='/admin_add_workshop'</script>")

   
    return render(request, 'admin_add_workshop.html')




def admin_view_workshop(request):

    q = workshop.objects.all()
    
    paginator = Paginator(q, 5)  # Assuming 10 items per page
    page_number = request.GET.get('page', 1)
    q = paginator.get_page(page_number)
    # Calculate row numbers based on page_obj
    for index, item in enumerate(q.object_list, start=q.start_index()):
        item.row_number = index
    
   
    return render(request, 'admin_view_workshop.html', {'q':q})


def workshop_update(request,id):

    # q=workshop.objects.all()
    qa=workshop.objects.get(id=id)
    if request.method == 'POST':
      
        wt = request.POST['wt']
        de = request.POST['de']
        dt = request.POST['dt']
        st = request.POST['st']
        lo = request.POST['lo']
        rf = request.POST['rf']

        qa.title=wt
        qa.description=de
        qa.date_time=dt
        qa.location=lo
        qa.no_of_slots=st
        qa.reg_fees=rf
        qa.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_view_workshop'</script>")


    return render(request,'admin_view_workshop.html',{'qa':qa,})

def workshop_delete(request,id):
    qa=workshop.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_workshop'</script>")



def worker_view_workshops(request):

    obj = workshop.objects.filter(status='pending')

    # Filter the complaints based on the query
    paginator = Paginator(obj, 4)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)
    
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index


    # paginator = Paginator(obj, 5)  # Assuming 5 items per page
    # page_number = request.GET.get('page')
    # obj = paginator.get_page(page_number)

    # # Calculate row numbers based on page_obj
    # for index, item in enumerate(obj.object_list, start=obj.start_index()):
    #     item.row_number = index + 1  # Adjust to ensure row numbers start from 1

   
    return render(request, 'worker_view_workshops.html', {'obj':obj})








def workshop_join(request,id,reg_fees):

    # q=Worker.objects.get(id=request.session['w_id'])
    # print(q)
    qw = worker_join.objects.filter(worker_id=request.session['w_id'], workshop_id=id)
    if qw:
        return HttpResponse("<script>alert('Already joined this workshop');window.location='/worker_view_workshops'</script>")
    else:
        qw=Worker.objects.get(id=request.session['w_id'])

        if request.method=='POST':
            pl=request.POST['pl']
            ebs=request.POST['esb']
            ta=request.POST['ta']
            q=worker_join(workshop_id=id,worker_id=request.session['w_id'],planguage=pl,education=ebs,amount=ta)
            q.save()
            return HttpResponse("<script>alert(' joined this workshop');window.location='/customer_payment/%s/%s'</script>"%(id,reg_fees) )




    return render(request,'workshop_join.html',{'qa':qw,'reg_fees':reg_fees})






def customer_payment(request,id,reg_fees):
    from datetime import datetime,date
    today=date.today()
    lid=request.session['login_id']

    if request.method=="POST":
        names = request.POST['names']
        number = request.POST['number']
        exry = request.POST['exry']
        cvv = request.POST['cvv']

        q=payments(cname=names,cnumber=number,cvv=cvv,expiry=exry,amount=reg_fees,workshop_id=id,worker_id=request.session['w_id'])
        q.save()
        q1=workshop.objects.get(id=id)
        print("-----------------",q1)
        if q1:
            slots=q1.no_of_slots
            slotss=int(slots)-int(1)
            print("-----------------",slotss)
            q1.no_of_slots=slotss
            q1.save()
            return HttpResponse("<script>alert('paid successfully....!!!');window.location='/worker_view_workshops';</script>")

    return render(request,'customer_payment.html',{'total':reg_fees})




def workshop_expire(request,id):

    # q=workshop.objects.all()
    qa=workshop.objects.get(id=id)
    if qa:
        qa.status='expired'
        qa.save()
        return HttpResponse("<script>alert(' Expired Successfully');window.location='/admin_view_workshop'</script>")


    return render(request,'admin_view_workshop.html',{'qa':qa})



def crop_add(request):

    # Crop1 = Crop.objects.all()

    if request.method == 'POST':
        # Handle form submission
        ct = request.POST['ct']
        vt = request.POST['vt']
        ii = request.POST['ii']
        Crop.objects.create(
            type=ct,
            variety=vt,
            internal_id=ii,
            farmer_id=request.session['login_id'],
        )
        return HttpResponse("<script>alert('Successfully Added');window.location='/crop_add'</script>")

   
    return render(request, 'farmer_crop.html')




# def admin_view_crop(request):

#     Crop1 = Crop.objects.all()
   
#     return render(request, 'admin_view_crop.html', {'q':Crop1})


def admin_view_crop(request):

    q = Crop.objects.all()
    # q = queryset_for_crops  # Replace with your queryset

    if request.method == "POST":
        sname = request.POST['sname']

        q=Crop.objects.filter(internal_id=sname)|Crop.objects.filter(type=sname)|Crop.objects.filter(variety=sname)


    paginator = Paginator(q, 5)  # Assuming 10 items per page
    page_number = request.GET.get('page', 1)
    q = paginator.get_page(page_number)
    # Calculate row numbers based on page_obj
    for index, item in enumerate(q.object_list, start=q.start_index()):
        item.row_number = index
        
    return render(request, 'admin_view_crop.html', {'q':q})





def crop_update(request,id):

    # q=Crop.objects.all()
    qa=Crop.objects.get(id=id)
    if 'update' in request.POST:
      
        ct = request.POST['ct']
        vt = request.POST['vt']
        ii = request.POST['ii']
        qa.type=ct
        qa.variety=vt
        qa.internal_id=ii
        qa.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_view_crop'</script>")


    return render(request,'farmer_crop.html',{'qa':qa,})

def crop_delete(request,id):
    qa=Crop.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_crop'</script>")



def plant_add(request,id,types,variety,internal_id):
    today = date.today().strftime('%Y-%m-%d')

    Crop1 = plant.objects.all()
    workers = Worker.objects.all()

    if request.method == 'POST':
        # Handle form submission
        name = request.POST['name']
        ct = request.POST['lt']
        vt = request.POST['vt']
        ii = request.POST['ii']
        pf = request.POST['pf']
        pd = request.POST['pd']
        worker = request.POST['worker']
        plant.objects.create(
            name=name,
            variety=vt,
            internal_id=ii,
            location_type=ct,
            planting_fomate=pf,
            Plant_date=pd,
            crop_id=id,
            worker_id=worker,
            status='pending',
            farmer_id='1',
        )
        return HttpResponse("<script>alert('Successfully Added');window.location='/admin_view_crop'</script>")
    return render(request, 'plant.html', {'q':Crop1,'type':types,'variety':variety,'internal_id':internal_id,'w':workers,'today':today})




def plant_update(request,id):
    workers = Worker.objects.all()

    q=plant.objects.all()
    qa=plant.objects.get(id=id)
    if 'update' in request.POST:
      
        name = request.POST['name']
        ct = request.POST['lt']
        vt = request.POST['vt']
        ii = request.POST['ii']
        pf = request.POST['pf']
        pd = request.POST['pd']
        worker = request.POST['worker']
        qa.worker_id = worker


        qa.name=name
        qa.location_type=ct
        qa.planting_fomate=pf
        qa.Plant_date=pd
        qa.variety=vt
        qa.internal_id=ii
        
        qa.save()
        return HttpResponse("<script>alert('Successfully Updated');window.location='/admin_view_crop'</script>")

       
    return render(request,'plant.html',{'q':q,'qa':qa,'w':workers})

def plant_delete(request,id):
    qa=plant.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_crop'</script>")



  



def harvest_add(request,id,types,variety,internal_id):
    today = date.today().strftime('%Y-%m-%d')

    workers = Worker.objects.all()

    Crop1 = harvesting.objects.all()

    if request.method == 'POST':
        # Handle form submission
        name = request.POST['name']
        ct = request.POST['lt']
        vt = request.POST['vt']
        ii = request.POST['ii']
        size =request.POST['size']
        pd = request.POST['hd']
        worker = request.POST['worker']

        harvesting.objects.create(
            name=name,
            variety=vt,
            internal_id=ii,
            location_type=ct,
            size=size,
            harvesting_date=pd,
            crop_id=id,
            status='pending',
            farmer_id='1',
            worker_id=worker,

        )

        return HttpResponse("<script>alert('Successfully Added');window.location='/admin_view_crop'</script>")


    return render(request, 'harvesting.html', {'q':Crop1,'type':types,'variety':variety,'internal_id':internal_id,'w':workers,'today':today})




def harvesting_update(request,id):

    workers = Worker.objects.all()

    q=harvesting.objects.all()
    qa=harvesting.objects.get(id=id)
    if 'update' in request.POST:
      
        name = request.POST['name']
        ct = request.POST['lt']
        vt = request.POST['vt']
        ii = request.POST['ii']

        size =request.POST['size']

        pd = request.POST['hd']
        worker = request.POST['worker']
        qa.worker_id = worker
        qa.name=name
        qa.location_type=ct
        qa.harvesting_date=pd
        qa.size=size
        qa.variety=vt
        qa.internal_id=ii
        
        qa.save()
        return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_crop'</script>")


    return render(request,'harvesting.html',{'q':q,'qa':qa,'w':workers})

def harvesting_delete(request,id):
    qa=harvesting.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_crop'</script>")




#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully deleted 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/crop_add';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)






def livestock_add(request):
    # animals = Animal.objects.all()
    today = date.today().strftime('%Y-%m-%d')
    print("---------------",today)
    if request.method == 'POST':
        animal_name = request.POST.get('animal')
        animal_type = request.POST.get('type')
        breed = request.POST.get('breed')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        status = request.POST.get('status')
        weight = request.POST.get('weight')
        breeding_status = request.POST.get('breeding_status')
        d = request.FILES.get('image')
        fs=FileSystemStorage()
        fn=fs.save(d.name,d)



        documents = request.FILES.get('documents')
        fss=FileSystemStorage()
        fnn=fss.save(documents.name,documents)


        intid = request.POST.get('intid')

        
        new_animal = Animal(
            animal=animal_name,
            type=animal_type,
            breed=breed,
            gender=gender,
            dob=dob,
            status=status,
            weight=weight,
            breeding_status=breeding_status,
            image=fn,
            documents=fnn,
            internal_id=intid
        )
        new_animal.save()
        return HttpResponse("<script>alert('Successfully Added');window.location='/livestock_add'</script>")




    # print(animals)
    return render(request, 'livestock.html',{'today':today})



def livestock_delete(request,id):
    qa=Animal.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_live'</script>")




# def admin_view_live(request):

#     q=Animal.objects.all()
   
#     return render(request,'admin_view_live.html',{'q':q})

def admin_view_live(request):

    q=Animal.objects.all()
    paginator = Paginator(q,4)
    page_number = request.GET.get('page')
    q= paginator.get_page(page_number)
    
    for index, item in enumerate(q.object_list, start=q.start_index()):
        item.row_number = index
   
    return render(request,'admin_view_live.html',{'q':q})




# from django.utils.dateparse import parse_date


# def animal_update(request,id):

#     q=Animal.objects.all()
#     qa=Animal.objects.get(id=id)
#     if 'update' in request.POST:
#         animal_name = request.POST.get('animal')
#         animal_type = request.POST.get('type')
#         breed = request.POST.get('breed')
#         gender = request.POST.get('gender')
#         dob = request.POST.get('dob')


        
#         status = request.POST.get('status')
#         weight = request.POST.get('weight')
#         breeding_status = request.POST.get('breeding_status')


#         d = request.FILES.get('dds')
#         fs=FileSystemStorage()
#         fn=fs.save(d.name,d)



#         documents = request.FILES.get('documents')
#         fss=FileSystemStorage()
#         fnn=fss.save(documents.name,documents)

#         qa.animal=animal_name
#         qa.type=animal_type
#         qa.breed=breed
#         qa.breeding_status=breeding_status
#         qa.dob=dob
#         qa.gender=gender
#         qa.status=status
#         qa.weight=weight
#         qa.image=fn
#         qa.documents=fnn
#         qa.save()
#         return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_live'</script>")

 
#     return render(request,'livestock.html',{'qa':qa,'q':q})

def animal_update(request, id):
    today = date.today().strftime('%Y-%m-%d')


    # q = Animal.objects.all()
    qa = get_object_or_404(Animal, id=id)
    if 'update' in request.POST:
        animal_name = request.POST.get('animal')
        animal_type = request.POST.get('type')
        breed = request.POST.get('breed')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        status = request.POST.get('status')
        weight = request.POST.get('weight')
        breeding_status = request.POST.get('breeding_status')
        
        if request.FILES.get('dds'):
            d = request.FILES['dds']
            fs = FileSystemStorage()
            fn = fs.save(d.name, d)
            qa.image = fn
        
        if request.FILES.get('documents'):
            documents = request.FILES['documents']
            fss = FileSystemStorage()
            fnn = fss.save(documents.name, documents)
            qa.documents = fnn

        qa.animal = animal_name
        qa.type = animal_type
        qa.breed = breed
        qa.breeding_status = breeding_status
        qa.dob = dob
        qa.gender = gender
        qa.status = status
        qa.weight = weight
        qa.save()
        return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_live'</script>")
    
    return render(request, 'admin_view_live.html', {'qa': qa})



def bill_add(request):
    # animals = Transaction.objects.all()
    if request.method == 'POST':
        t = request.POST.get('t')
        p = request.POST.get('p')
        c = request.POST.get('c')
        a = request.POST.get('a')
        d = request.FILES.get('b')
        fs=FileSystemStorage()
        fn=fs.save(d.name,d)
        
        new_animal = Transaction(
            type=t,
            payee=p,
            category=c,
            amount=a,
            bill=fn,
            farmer_id=request.session['login_id'],
            date=date.today()

        )
        new_animal.save()
        return HttpResponse("<script>alert('Successfully Added');window.location='/bill_add'</script>")



    # print(animals)
    return render(request, 'tranction.html')




# def admin_view_tra(request):

#     animals = Transaction.objects.all()
   

#     return render(request, 'admin_view_tra.html',{'q':animals})

def admin_view_tra(request):

    q = Transaction.objects.all()
    paginator = Paginator(q, 5)
    page_number = request.GET.get('page')
    q= paginator.get_page(page_number)
    
    for index, item in enumerate(q.object_list, start=q.start_index()):
        item.row_number = index
   

    return render(request, 'admin_view_tra.html',{'q':q})

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Transaction
from datetime import date

def tranction_update(request, id):
    qa = get_object_or_404(Transaction, id=id)
    
    if request.method == "POST":
        h = request.POST.get('ffff')
        p = request.POST.get('p')
        c = request.POST.get('c')
        a = request.POST.get('a')
        b = request.FILES.get('b')

        if h:
            qa.type = h
        if p:
            qa.payee = p
        if c:
            qa.category = c
        if a:
            qa.amount = a
        if b:
            fs = FileSystemStorage()
            fn = fs.save(b.name, b)
            qa.bill = fn

        qa.date = date.today()
        qa.save()
        return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_tra'</script>")

    return render(request, 'admin_view_tra.html', {'qa': qa})


# def tranction_update(request, id):
#     animals = Transaction.objects.all()
#     qa=Transaction.objects.get(id=id)
    
#     if request.method == "POST":
#         h = request.POST.get('ffff')  # Use get() method to handle missing keys
#         print("---------------",h)
#         p = request.POST.get('p')
#         c = request.POST.get('c')
#         a = request.POST.get('a')
#         b = request.FILES.get('b')

#         if h:
#             qa.type = h
#         if p:
#             qa.payee = p
#         if c:
#             qa.category = c
#         if a:
#             qa.amount = a
#         if b:
#             fs = FileSystemStorage()
#             fn = fs.save(b.name, b)
#             qa.bill = fn

#         qa.date = date.today()
#         qa.save()
#         return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_tra'</script>")


#     return render(request, 'admin_view_tra.html',{'qa':qa})

# def tranction_update(request,id):

#     # animals = Transaction.objects.all()
#     qa=Transaction.objects.get(id=id)
#     if request.method=="POST":

#         f = request.POST['f']
#         print("============",f)
#         p = request.POST['p']
#         c = request.POST['c']
#         a = request.POST['a']
#         b = request.FILES['b']
#         fs=FileSystemStorage()
#         fn=fs.save(b.name,b)
#         qa.type=f
#         qa.payee=p
#         qa.category=c
#         qa.amount=a
#         qa.bill=fn
#         qa.date=date.today()
#         qa.save()
#         return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_tra'</script>")


#     return render(request, 'admin_view_tra.html',{'qa':qa})


def bill_delete(request,id):
    qa=Transaction.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_tra'</script>")








from django.db.models import Sum


from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction

def admin_view_pl(request):
    # Get all income transactions
    animals = Transaction.objects.filter(type='income')
    tot_in = Transaction.objects.filter(type='income').aggregate(total_income=Sum('amount'))
    total_income = tot_in['total_income'] if tot_in['total_income'] else 0

    # Get all expense transactions
    ex = Transaction.objects.filter(type='Expense')
    tot_ex = Transaction.objects.filter(type='Expense').aggregate(total_expense=Sum('amount'))
    total_expense = tot_ex['total_expense'] if tot_ex['total_expense'] else 0

    # Calculate net amount
    net_amount =total_income - total_expense
    print("----------------------", net_amount)

    return render(request, 'admin_view_pl.html', {'q': animals, 'ex': ex, 'tot_in': total_income, 'tot_ex': total_expense, 'net_amount': net_amount})




def admin_pl(request):
    # Assuming your Transaction model has a field `amount` and a field `type` which can be 'expense' or 'profit'
    # expenses = Transaction.objects.filter(type='Expense').aggregate(total_expense=Sum('amount'))['total_expense'] or 0
    expenses = Transaction.objects.filter(type='Expense').count()
    profits = Transaction.objects.filter(type='income').count()
    # profits = Transaction.objects.filter(type='income').aggregate(total_profit=Sum('amount'))['total_profit'] or 0

    return render(request, 'admin_pl.html', {'cus': expenses, 'sel': profits})



def add_todoss(request):
    return render(request,'add_todo.html')



def worker_add_todoss(request):
    return render(request,'worker_add_todo.html')


# def view_complaint(request):
#     obj=Complaint.objects.all()
#     return render(request,'view_complaint.html',{'obj':obj})


def view_complaint(request):
    obj=Complaint.objects.all()
    
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)
    
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index
    return render(request,'view_complaint.html',{'obj':obj})



def send_reply(request,id):
    ob=Complaint.objects.get(id=id)
    if 'submit' in request.POST:
        reply=request.POST['reply']
        ob.reply=reply
        ob.save()
        return HttpResponse("<script>alert('REPLY SENT');window.location='/view_complaint'</script>")

    return render(request,'view_complaint.html',{'ob':ob})



def send_complaint(request):
    u_id=request.session['w_id']
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",u_id)
    w=Worker.objects.get(id=request.session['w_id'])
    cdate=date.today()
    if request.method=="POST":
        feedbacks=request.POST['com']
        re = request.POST['re']
        posi = request.POST['posi']
        dept = request.POST['dept']
        q=Complaint(worker_id=request.session['w_id'],department=dept,position=posi,Resolution_expt=re,date=cdate,complaint_text=feedbacks,reply='pending')
        q.save()
        return HttpResponse("<script>alert('send successfully');window.location='/send_complaint'</script>" )
    cus=Complaint.objects.all()
    return render(request,'send_complaint.html',{'q':cus,'w':w})



def send_leave(request):
    today = date.today().strftime('%Y-%m-%d')

    w=Worker.objects.get(id=request.session['w_id'])
    cdate = date.today()
    
    if request.method == "POST":
        feedbacks = request.POST['com']
        # emp_id = request.POST['emp_id']
        posi = request.POST['posi']
        dept = request.POST['dept']
        type = request.POST['type']
        total1 = request.POST['total']
        eda = request.POST['eda']
        da = request.POST['da']
        
        q = Leave(
            worker_id = request.session['w_id'],
            department = dept,
            position = posi,
            leave_type = type,
            total = total1,
            startdate = da,
            date = eda,  # Ensure this is the correct usage based on your model's fields
            Reason = feedbacks,
            status = 'pending',
            farmer_id = '1'
        )
        
        q.save()
        return HttpResponse("<script>alert('send successfully');window.location='/send_leave'</script>")
    
    cus = Leave.objects.filter(worker_id=request.session['w_id'])
    return render(request, 'leave_req.html', {'q': cus, 'w': w,'today':today})

# def leave_request_report(request):
#     cus = Leave.objects.filter(worker_id=request.session['w_id'])
#     return render(request,'leave_request_report.html',{'q':cus})




from datetime import datetime
from django.shortcuts import render
from django.db.models import Q
from .models import Leave  # Assuming your model is named Leave


def leave_request_report(request):
    # Initial query filtering by worker_id
    query = Q(worker_id=request.session.get('w_id'))

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        search_conditions = Q()

        # Apply search filter across all relevant fields
        if sname:
            search_conditions |= (
                Q(Reason__icontains=sname) |
                Q(status__icontains=sname)
            )

            # Additionally check if 'sname' can be interpreted as a date and apply to date field
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(date=sname_date)
            except ValueError:
                pass

        # Apply date range filters
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(date__lte=end_date)
            except ValueError:
                pass

        # Combine the search conditions with the initial query
        query &= search_conditions

    # Apply the constructed query to filter the queryset
    obj = Leave.objects.filter(query)
    total_leaves = obj.count()  # Calculate total leaves after filtering

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    return render(request, 'leave_request_report.html', {'obj': obj, 'total_leaves': total_leaves})











# def leave_request_report(request):
#     obj = Leave.objects.filter(worker_id=request.session.get('w_id'))
#     total_leaves =obj.count()  # Initialize total_leaves here

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(Reason__icontains=sname)
#             q |= Q(status__icontains=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = Leave.objects.filter(q, worker_id=request.session.get('w_id'))
#         total_leaves = obj.count()
#         print(total_leaves,"----------------------------")


#     paginator = Paginator(obj, 5)
#     page_number = request.GET.get('page')
#     obj = paginator.get_page(page_number)
    
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index



#     return render(request, 'leave_request_report.html', {'obj': obj, 'total_leaves': total_leaves})



# def admin_view_leave(request):
#    cus = Leave.objects.all()
# #    paginator = Paginator(cus, 4)
# #    page_number = request.GET.get('page')
# #    cus= paginator.get_page(page_number)
    
# #    for index, item in enumerate(cus.object_list, start=cus.start_index()):
# #         item.row_number = index
   
#    return render(request,'admin_view_leave.html',{'q':cus})

    
def admin_view_leave(request):
    obj = Leave.objects.all()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        q = Q()
        if sname:
            q |= Q(Reason__icontains=sname)
            q |= Q(worker__first_name__icontains=sname)
            q |= Q(status__icontains=sname)
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                q |= Q(date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                q |= Q(date=start_date)
                if end_date_str:
                    try:
                        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                        q |= Q(date__range=[start_date, end_date])
                    except ValueError:
                        pass
            except ValueError:
                pass

        obj = Leave.objects.filter(q)

    
    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)
    
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index

    
    return render(request, 'admin_view_leave.html', {'obj': obj})
    





def l_accept(request,id):
    obj1=Leave.objects.get(id=id)
    obj1.status="Accepted"
    obj1.save()
    return HttpResponse("<script>alert('Successfully Accepted ');window.location='/admin_view_leave'</script>")




def l_reject(request,id):
    obj1=Leave.objects.get(id=id)
    obj1.status="Rejected"
    obj1.save()
    return HttpResponse("<script>alert('Successfully Rejected ');window.location='/admin_view_leave'</script>")


# def complaint_report(request):
#     cus = Complaint.objects.filter(worker_id=request.session['w_id'])
#     return render(request,'complaint_report.html',{'q':cus})



















# def complaint_report(request):
#     obj = Complaint.objects.filter(worker_id=request.session['w_id'])
#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(complaint_text__icontains=sname)
#             q |= Q(reply__icontains=sname)
#             # q |= Q(location_type__icontains=sname)
#              # Correct field name assumed here
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = Complaint.objects.filter(q,worker_id=request.session['w_id'])

#     # obj=Complaint.objects.all()
    
#     paginator = Paginator(obj, 5)
#     page_number = request.GET.get('page')
#     obj = paginator.get_page(page_number)
    
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index


#     return render(request, 'complaint_report.html', {'obj': obj})

def complaint_report(request):
    # Initial query filtering by worker_id
    query = Q(worker_id=request.session['w_id'])

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        # Apply search filter across all relevant fields
        if sname or start_date_str or end_date_str:
            search_conditions = Q()

            # Use OR conditions across all relevant fields for sname
            if sname:
                search_conditions |= (
                    Q(complaint_text__icontains=sname) |
                    Q(reply__icontains=sname)
                )

                # Additionally check if 'sname' can be interpreted as a date and apply to date field
                try:
                    sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                    search_conditions |= Q(date=sname_date)
                except ValueError:
                    pass

            # Apply date range filters
            if start_date_str:
                try:
                    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                    search_conditions &= Q(date__gte=start_date)
                except ValueError:
                    pass

            if end_date_str:
                try:
                    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                    search_conditions &= Q(date__lte=end_date)
                except ValueError:
                    pass

            # Combine the search conditions with the initial query
            query &= search_conditions

    # Apply the constructed query to filter the queryset
    obj = Complaint.objects.filter(query)

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    return render(request, 'complaint_report.html', {'obj': obj})



# from django.shortcuts import render
# from django.db.models import Q
# from .models import Task  # Make sure to import the Task model
# from datetime import datetime

# def admin_task(request):
#     obj = Task.objects.filter(status='completed')
#     total_task=obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(task_name=sname)
#             q |= Q(Priority=sname)
#             q |= Q(assigned_worker__first_name=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(due_date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(due_date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(due_date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = Task.objects.filter(q)
#         total_task=obj.count()




#     paginator = Paginator(obj, 4)
#     page_number = request.GET.get('page')
#     obj= paginator.get_page(page_number)
    
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index
    
#     context = {
#         'obj':obj,  # Use page_obj instead of q
#         # 'q':tasks,
#         'total_task':total_task
#     }
#     return render(request, 'admin_task_reportsss.html', context)


    # return render(request, 'admin_task_reportsss.html', {'q': tasks})


from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
from .models import Task

# def admin_task(request):
#     obj = Task.objects.filter(status='completed')
#     total_task = obj.count()

#     sname = request.POST.get('sname', '')
#     start_date_str = request.POST.get('start_date', '')
#     end_date_str = request.POST.get('end_date', '')

#     q = Q()
#     if sname:
#         q |= Q(task_name__icontains=sname)
#         q |= Q(Priority__icontains=sname)
#         q |= Q(assigned_worker__first_name__icontains=sname)
#         try:
#             sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#             q |= Q(due_date=sname_date)
#         except ValueError:
#             pass

#     if start_date_str:
#         try:
#             start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#             q |= Q(due_date=start_date)
#             if end_date_str:
#                 try:
#                     end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                     q |= Q(due_date__range=[start_date, end_date])
#                 except ValueError:
#                     pass
#         except ValueError:
#             pass

#     if q:
#         obj = Task.objects.filter(q,status='completed')
#         total_task = obj.count()

#     paginator = Paginator(obj, 4)
#     page_number = request.GET.get('page')
#     obj = paginator.get_page(page_number)

#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index

#     context = {
#         'obj': obj,
#         'total_task': total_task,
#         'sname': sname,
#         'start_date': start_date_str,
#         'end_date': end_date_str
#     }
#     return render(request, 'admin_task_reportsss.html', context)


# def admin_task(request):
#     obj = Task.objects.filter(status='completed')
#     total_task = obj.count()

#     sname = request.POST.get('sname', '')
#     start_date_str = request.POST.get('start_date', '')
#     end_date_str = request.POST.get('end_date', '')

#     q = Q()
#     if sname:
#         q |= Q(task_name__icontains=sname)
#         q |= Q(Priority__icontains=sname)
#         q |= Q(assigned_worker__first_name__icontains=sname)
#         try:
#             sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#             q |= Q(due_date=sname_date)
#         except ValueError:
#             pass

#     if start_date_str:
#         try:
#             start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#             q |= Q(due_date=start_date)
#             if end_date_str:
#                 try:
#                     end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                     q |= Q(due_date__range=[start_date, end_date])
#                 except ValueError:
#                     pass
#         except ValueError:
#             pass

#     if q:
#         obj = Task.objects.filter(q,status='completed')
#         total_task = obj.count()

#     paginator = Paginator(obj, 4)
#     page_number = request.GET.get('page')
#     obj = paginator.get_page(page_number)

#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index

#     context = {
#         'obj': obj,
#         'total_task': total_task,
#         'sname': sname,
#         'start_date': start_date_str,
#         'end_date': end_date_str
#     }
#     return render(request, 'admin_task_reportsss.html', context)




# def admin_task(request):
#     # Initial query filtering by status 'completed'
#     obj = Task.objects.filter(status='completed')
#     total_task = obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         # Apply search filter across all relevant fields if sname is provided
#         if sname:
#             q |= (
#                 Q(task_name__icontains=sname) |
#                 Q(Priority__icontains=sname) |
#                 Q(assigned_worker__first_name__icontains=sname)
#             )

#             # Additionally check if 'sname' can be interpreted as a date and apply to due_date
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(due_date=sname_date)
#             except ValueError:
#                 pass

#         # Apply date range filters
#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q &= Q(due_date__gte=start_date)
#             except ValueError:
#                 pass

#         if end_date_str:
#             try:
#                 end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                 q &= Q(due_date__lte=end_date)
#             except ValueError:
#                 pass

#         if q:
#             obj = Task.objects.filter(q, status='completed')
#             total_task = obj.count()

#     # Pagination
#     paginator = Paginator(obj, 4)  # Paginate with 4 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)

#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index  # Row numbers starting from 1

#     context = {
#         'obj': obj,
#         'total_task': total_task,
#         'sname': sname,
#         'start_date': start_date_str,
#         'end_date': end_date_str
#     }
#     return render(request, 'admin_task_reportsss.html', context)

def admin_task(request):
    # Initial query filtering by status 'completed'
    obj = Task.objects.filter(status='completed')
    total_task = obj.count()

    # Initialize search parameters
    sname = ''
    start_date_str = ''
    end_date_str = ''

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        q = Q()
        # Apply search filter across all relevant fields if sname is provided
        if sname:
            q |= (
                Q(task_name__icontains=sname) |
                Q(Priority__icontains=sname) |
                Q(assigned_worker__first_name__icontains=sname)
            )

            # Additionally check if 'sname' can be interpreted as a date and apply to due_date
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                q |= Q(due_date=sname_date)
            except ValueError:
                pass

        # Apply date range filters
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                q &= Q(due_date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                q &= Q(due_date__lte=end_date)
            except ValueError:
                pass

        if q:
            obj = Task.objects.filter(q, status='completed')
            total_task = obj.count()

    # Pagination
    paginator = Paginator(obj, 4)  # Paginate with 4 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    context = {
        'obj': obj,
        'total_task': total_task,
        'sname': sname,
        'start_date': start_date_str,
        'end_date': end_date_str
    }
    return render(request, 'admin_task_reportsss.html', context)

def admin_live_reportss(request):
    q = Animal.objects.all()
    live=q.count()
    print("---------------",live)

    if request.method == "POST":
        sname = request.POST['sname']

        q=Animal.objects.filter(internal_id=sname)|Animal.objects.filter(animal=sname)|Animal.objects.filter(type=sname)|Animal.objects.filter(breed=sname)|Animal.objects.filter(breeding_status=sname)|Animal.objects.filter(status=sname)|Animal.objects.filter(gender=sname)
        live=q.count()

    paginator = Paginator(q,4)
    page_number = request.GET.get('page')
    q= paginator.get_page(page_number)
    
    for index, item in enumerate(q.object_list, start=q.start_index()):
        item.row_number = index
   
    return render(request, 'admin_live_report.html', {'q': q,'live':live})







# def admin_invent_report(request):
#     q = inventory.objects.all()
#     live=q.count()
#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(name=sname)
#             q |= Q(type=sname)
#             q |= Q(brand=sname)
#             q |= Q(model=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(ls=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(ls=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(ls__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         q = inventory.objects.filter(q)
#     paginator = Paginator(q, 5)
#     page_number = request.GET.get('page')
#     q= paginator.get_page(page_number)
    
#     for index, item in enumerate(q.object_list, start=q.start_index()):
#         item.row_number = index
#     return render(request, 'admin_invent_report.html', {'q': q,'live':live})

def admin_invent_report(request):
    # Initialize base query for inventory
    query = Q()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        search_conditions = Q()
        if sname:
            search_conditions |= (
                Q(name__icontains=sname) |
                Q(type__icontains=sname) |
                Q(brand__icontains=sname) |
                Q(model__icontains=sname)
            )
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(ls=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(ls__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(ls__lte=end_date)
            except ValueError:
                pass

        # Apply the search conditions to the queryset
        query &= search_conditions

    # Filter the queryset based on the constructed query
    obj = inventory.objects.filter(query)
    live = obj.count()

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    context = {
        'q': obj,
        'live': live
    }

    return render(request, 'admin_invent_report.html', context)

# def admin_view_complaint(request):
#     obj = Complaint.objects.exclude(reply='pending')
#     com_count=obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(department=sname)
#             q |= Q(complaint_text=sname)
#             q |= Q(position=sname)
#             q |= Q(worker__first_name__icontains=sname)

#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = Complaint.objects.filter(q).exclude(reply='pending')
#         com_count=obj.count()

#     paginator = Paginator(obj, 4)
#     page_number = request.GET.get('page')
#     obj= paginator.get_page(page_number)
    
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index
    
#     context = {
#         'obj':obj,  # Use page_obj instead of q
#         'com_count':com_count,
#         # 'total_task':total_task
#     }
#     return render(request, 'admin_view_complaint.html', context)


def admin_view_complaint(request):
    # Start with complaints excluding those with 'pending' replies
    base_query = Complaint.objects.exclude(reply='pending')
    com_count = base_query.count()  # Initial count of all non-pending complaints

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        # Apply search conditions
        search_conditions = Q()
        if sname:
            search_conditions |= (
                Q(department__icontains=sname) |
                Q(complaint_text__icontains=sname) |
                Q(position__icontains=sname) |
                Q(worker__first_name__icontains=sname)
            )
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(date=sname_date)
            except ValueError:
                pass

        # Apply date range filtering
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(date__lte=end_date)
            except ValueError:
                pass

        # Filter based on search conditions
        obj = base_query.filter(search_conditions)
        com_count = obj.count()  # Update count based on filtered results

    else:
        # Use base_query if it's a GET request
        obj = base_query

    # Pagination
    paginator = Paginator(obj, 4)  # Paginate with 4 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    # Prepare context for the template
    context = {
        'obj': obj,  # Paginated result
        'com_count': com_count,  # Total count of non-pending complaints
    }

    return render(request, 'admin_view_complaint.html', context)


# def admin_trans_report(request):
#     q = Transaction.objects.all()
#     tra_count=q.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             try:
#                 # Check if sname can be a decimal number
#                 if sname.replace('.', '', 1).isdigit():
#                     q |= Q(amount=float(sname))
#             except ValueError:
#                 pass

#             q |= Q(payee__icontains=sname)
#             q |= Q(category__icontains=sname)
#             q |= Q(type__icontains=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         q = Transaction.objects.filter(q)
#         tra_count=q.count()


#     paginator = Paginator(q, 5)
#     page_number = request.GET.get('page')
#     q= paginator.get_page(page_number)
    
#     for index, item in enumerate(q.object_list, start=q.start_index()):
#         item.row_number = index
#     return render(request, 'admin_trans_report.html', {'q': q,'tra_count':tra_count})
def admin_trans_report(request):
    # Start with all transactions
    base_query = Transaction.objects.all()
    tra_count = base_query.count()  # Initial count of all transactions

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        search_conditions = Q()
        if sname:
            # Check if sname can be interpreted as a decimal number
            try:
                if sname.replace('.', '', 1).isdigit():
                    search_conditions |= Q(amount=float(sname))
            except ValueError:
                pass

            search_conditions |= Q(payee__icontains=sname)
            search_conditions |= Q(category__icontains=sname)
            search_conditions |= Q(type__icontains=sname)
            
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(date__lte=end_date)
            except ValueError:
                pass

        # Apply search conditions to the base query
        obj = base_query.filter(search_conditions)
        tra_count = obj.count()  # Update count based on filtered results
    else:
        # Use base_query if it's a GET request
        obj = base_query

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    # Prepare context for the template
    context = {
        'q': obj,  # Paginated result
        'tra_count': tra_count,  # Total count of transactions
    }

    return render(request, 'admin_trans_report.html', context)

# def admin_trans_report(request):
#     tasks = Transaction.objects.all()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(payee=sname)
#             q |= Q(category=sname)
#             q |= Q(amount=sname)
#             q |= Q(type=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         tasks = Transaction.objects.filter(q)

#     return render(request, 'admin_trans_report.html', {'q': tasks})



# def admin_leave_report(request):
#     q = Leave.objects.all().exclude(status='pending')
#     lea_count=q.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(leave_type=sname)
#             q |= Q(status=sname)
#             q |= Q(worker__first_name=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         q = Leave.objects.filter(q).exclude(status='pending')

#         lea_count=q.count()



#     paginator = Paginator(q, 5)
#     page_number = request.GET.get('page')
#     q= paginator.get_page(page_number)
    
#     for index, item in enumerate(q.object_list, start=q.start_index()):
#         item.row_number = index
#     return render(request, 'admin_leave_report.html', {'q': q,'lea_count':lea_count})




def admin_leave_report(request):
    # Start with all leaves excluding those with status 'pending'
    base_query = Leave.objects.exclude(status='pending')
    lea_count = base_query.count()  # Initial count of all leaves

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        # Build the query based on search parameters
        q = Q()
        if sname:
            q |= Q(leave_type__icontains=sname)
            q |= Q(status__icontains=sname)
            q |= Q(worker__first_name__icontains=sname)
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                q |= Q(date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                q &= Q(date__gte=start_date)
                if end_date_str:
                    try:
                        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                        q &= Q(date__lte=end_date)
                    except ValueError:
                        pass
            except ValueError:
                pass

        # Apply the filter and exclude 'pending' status
        obj = Leave.objects.filter(q).exclude(status='pending')
        lea_count = obj.count()  # Update count after filtering

    else:
        obj = base_query

    # Pagination
    paginator = Paginator(obj, 5)  # 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index

    # Render the response
    return render(request, 'admin_leave_report.html', {'q': obj, 'lea_count': lea_count})



# def admin_workshop_reportss(request):
#     q = workshop.objects.all()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(title=sname)
#             q |= Q(description=sname)
#             q |= Q(location=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(date_time=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(date_time=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(date_time__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         q = workshop.objects.filter(q)
#     paginator = Paginator(q, 5)
#     page_number = request.GET.get('page')
#     q= paginator.get_page(page_number)
    
#     for index, item in enumerate(q.object_list, start=q.start_index()):
#         item.row_number = index
#     return render(request, 'admin_workshop_report.html', {'q': q})


from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render


def admin_workshop_reportss(request):
    from django.db.models import Sum

    obj = worker_join.objects.all()
    wcount = obj.count()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_datetime_str = request.POST.get('start_datetime', '')
        end_datetime_str = request.POST.get('end_datetime', '')

        q = Q()
        if sname:
            q |= Q(workshop__title__icontains=sname)
            q |= Q(amount__icontains=sname)
            q |= Q(planguage__icontains=sname)
            q |= Q(worker__first_name__icontains=sname)
            q |= Q(worker__department__icontains=sname)
            try:
                sname_datetime = datetime.strptime(sname, '%Y-%m-%dT%H:%M')
                q |= Q(workshop__date_time=sname_datetime)
            except ValueError:
                pass

        if start_datetime_str:
            try:
                start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%dT%H:%M')
                q &= Q(workshop__date_time__gte=start_datetime)
            except ValueError:
                pass

        if end_datetime_str:
            try:
                end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%dT%H:%M')
                q &= Q(workshop__date_time__lte=end_datetime)
            except ValueError:
                pass

        obj = worker_join.objects.filter(q)
        wcount = obj.count()

    # Calculate the total amount
    total_amount = obj.aggregate(Sum('amount'))['amount__sum'] or 0

    paginator = Paginator(obj, 5)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)

        
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index

    return render(request, 'admin_workshop_report.html', {'obj': obj, 'wcount': wcount, 'total_amount': total_amount})





# def admin_workshop_reportss(request):
#     obj = worker_join.objects.all()
#     wcount = obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_datetime_str = request.POST.get('start_datetime', '')
#         end_datetime_str = request.POST.get('end_datetime', '')

#         q = Q()
#         if sname:
#             q |= Q(workshop__title__icontains=sname)
#             q |= Q(amount__icontains=sname)
#             q |= Q(planguage__icontains=sname)
#             try:
#                 sname_datetime = datetime.strptime(sname, '%Y-%m-%dT%H:%M')
#                 q |= Q(workshop__date_time=sname_datetime)
#             except ValueError:
#                 pass

#         if start_datetime_str:
#             try:
#                 start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%dT%H:%M')
#                 q &= Q(workshop__date_time__gte=start_datetime)
#             except ValueError:
#                 pass

#         if end_datetime_str:
#             try:
#                 end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%dT%H:%M')
#                 q &= Q(workshop__date_time__lte=end_datetime)
#             except ValueError:
#                 pass

#         obj = worker_join.objects.filter(q)
#         wcount = obj.count()

#     paginator = Paginator(obj, 5)
#     page_number = request.GET.get('page')
#     obj = paginator.get_page(page_number)

#     return render(request, 'admin_workshop_report.html', {'obj': obj, 'wcount': wcount})



# def admin_workshop_reportss(request):
#     obj = worker_join.objects.all()
#     wcount=obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_datetime_str = request.POST.get('start_datetime', '')
#         print("----------------",start_datetime_str)
#         end_datetime_str = request.POST.get('end_datetime', '')
#         print("----------------",end_datetime_str)

#         q = Q()
#         if sname:
#             q |= Q(worker__title__icontains=sname)
#             q |= Q(amount__icontains=sname)
#             q |= Q(planguage__icontains=sname)
#             try:
#                 sname_datetime = datetime.strptime(sname, '%Y-%m-%dT%H:%M')
#                 q |= Q(worker_join__date_time=sname_datetime)
#             except ValueError:
#                 pass

#         if start_datetime_str:
#             try:
#                 start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%dT%H:%M')
#                 q &= Q(worker_join__date_time=start_datetime_str)
#                 print("----------------",q)
                
#             except ValueError:
#                 pass
#         if end_datetime_str:
#             if start_datetime_str:
#                 try:
#                     # start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%dT%H:%M')
#                     start_datetime_str = "2024-07-01T13:06:00"
#                     formatted_datetime_str = start_datetime_str.replace('T', ' ')
#                     print(formatted_datetime_str)
#                     q &= Q(worker_join__date_time__gte=formatted_datetime_str)
#                     print("----------------", q)
#                     if end_datetime_str:
#                         try:
#                             end_datetime_str = "2024-08-31T13:06:00"
#                             formatted_datetime_str = end_datetime_str.replace('T', ' ')
#                             print(formatted_datetime_str)
#                             # end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%dT%H:%M')
#                             q &= Q(worker_join__date_time__lte=formatted_datetime_str)
#                             print("----------------", q)
#                         except ValueError:
#                             pass
#                 except ValueError:
#                     pass

#         obj = worker_join.objects.filter(q)
#         print("-----------------",obj)
#         wcount=obj.count()

#     paginator = Paginator(obj, 5)
#     page_number = request.GET.get('page')
#     obj = paginator.get_page(page_number)

#     return render(request, 'admin_workshop_report.html', {'q': obj,'wcount':wcount})









def worker_workshop_report(request):
    obj = worker_join.objects.filter(worker_id=request.session['w_id'])
    wcount = obj.count()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_datetime_str = request.POST.get('start_datetime', '')
        end_datetime_str = request.POST.get('end_datetime', '')

        q = Q()
        if sname:
            q |= Q(workshop__title__icontains=sname)
            q |= Q(amount__icontains=sname)
            q |= Q(planguage__icontains=sname)
            try:
                sname_datetime = datetime.strptime(sname, '%Y-%m-%dT%H:%M')
                q |= Q(workshop__date_time=sname_datetime)
            except ValueError:
                pass

        if start_datetime_str:
            try:
                start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%dT%H:%M')
                q &= Q(workshop__date_time__gte=start_datetime)
            except ValueError:
                pass

        if end_datetime_str:
            try:
                end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%dT%H:%M')
                q &= Q(workshop__date_time__lte=end_datetime)
            except ValueError:
                pass

        obj = worker_join.objects.filter(q,worker_id=request.session['w_id'])
        wcount = obj.count()

    paginator = Paginator(obj, 5)  # Assuming 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index + 1  # Adjust to ensure row numbers start from 1

    return render(request, 'worker_workshop_report.html', {'obj': obj, 'wcount': wcount})



# def worker_workshop_report(request):
#     workshops = workshop.objects.all()
    
#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()

#         if sname:
#             q |= Q(title__icontains=sname)
#             q |= Q(description__icontains=sname)
#             q |= Q(location__icontains=sname)
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d')
#                 q |= Q(date_time__date=sname_date.date())
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
#                         q &= Q(date_time__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#                 else:
#                     q &= Q(date_time__date=start_date.date())
#             except ValueError:
#                 pass

#         workshops = workshop.objects.filter(q)

#     paginator = Paginator(workshops, 5)
#     page_number = request.GET.get('page')
#     paginated_workshops = paginator.get_page(page_number)
    
#     for index, item in enumerate(paginated_workshops.object_list, start=paginated_workshops.start_index()):
#         item.row_number = index + 1  # Adjusting to start at 1

#     return render(request, 'worker_workshop_report.html', {'q': paginated_workshops})


# def admin_task(request):
#     print("------------------------")

#     q=Task.objects.all()
#     print("------------------------")

#     if request.method=="POST":
#         print("-------------")
#         sname=request.POST['sname']
#         start_date=request.POST['start_date']
#         end_date=request.POST['end_date']
#         print("------------",sname)
#         q = (Q(task_name=sname) |
#             Q(Priority=sname) |
#             Q(assigned_worker__first_name=sname) |
#             Q(due_date=sname) |  # Assuming sname can be a date string
#             Q(due_date=start_date) |  # Adding single date search
#             Q(due_date__range=[start_date, end_date]))
#     print("------------",q)

#         tasks = Task.objects.filter(q)
#     return render(request,'admin_task_reportsss.html',{'q':q})

# def admin_task_reportsss(request):

#     if request.method=="POST":
#         sname=request.POST['sname']
#         q=Task.objects.filter(task_name__icontains=sname)
#         print(q)
        
        
#         # |Task.objects.filter(Priority==sname)|Task.objects.filter(due_date==sname)


#     return render(request, 'admin_task_reportsss.html', {'q': q})






# def worker_view_assigned_work(request):
#     q=Task.objects.filter(assigned_worker_id=request.session['w_id'])
#     return render(request,'worker_view_assigned_work.html',{'q':q})

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
from .models import Task  # Ensure to import your Task model

def worker_view_assigned_work(request):
    worker_id = request.session.get('w_id')
    if not worker_id:
        # Handle case where worker ID is not in session
        return render(request, 'worker_view_assigned_work.html', {'error': 'Worker ID not found in session.'})

    # Initial query for tasks assigned to the worker
    tasks = Task.objects.filter(assigned_worker_id=worker_id)

    # Search parameters
    sname = request.GET.get('sname', '')
    start_date_str = request.GET.get('start_date', '')
    end_date_str = request.GET.get('end_date', '')

    # Build the Q object for filtering
    q = Q()
    if sname:
        q |= Q(task_name__icontains=sname)
        q |= Q(status__icontains=sname)
        q |= Q(Priority__icontains=sname)  # Assuming 'priority' is the correct field name
        try:
            sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
            q |= Q(due_date=sname_date)
        except ValueError:
            pass

    if start_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            q &= Q(due_date__gte=start_date)
        except ValueError:
            pass

    if end_date_str:
        try:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            q &= Q(due_date__lte=end_date)
        except ValueError:
            pass

    # Apply filters
    filtered_tasks = tasks.filter(q)

    # Pagination
    paginator = Paginator(filtered_tasks, 5)  # Assuming 5 items per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(page_obj.object_list, start=page_obj.start_index()):
        item.row_number = index  # Adjust to ensure row numbers start from 1

    # Retain search parameters in pagination links
    query_params = request.GET.copy()
    query_params.pop('page', True)
    query_string = query_params.urlencode()

    return render(request, 'worker_view_assigned_work.html', {
        'page_obj': page_obj,
        'filtered_tasks': page_obj.object_list,
        'sname': sname,
        'start_date': start_date_str,
        'end_date': end_date_str,
        'query_string': query_string
    })


# def worker_view_assigned_work(request):
#     worker_id = request.session.get('w_id')
#     if not worker_id:
#         # Handle case where worker ID is not in session
#         return render(request, 'worker_view_assigned_work.html', {'error': 'Worker ID not found in session.'})

#     tasks = Task.objects.filter(assigned_worker_id=worker_id)

#     sname = request.GET.get('sname', '')
#     start_date_str = request.GET.get('start_date', '')
#     end_date_str = request.GET.get('end_date', '')

#     q = Q()
#     if sname:
#         q |= Q(task_name__icontains=sname)
#         q |= Q(status__icontains=sname)
#         q |= Q(Priority__icontains=sname)  # Assuming 'priority' is the correct field name
#         try:
#             sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#             q |= Q(due_date=sname_date)
#         except ValueError:
#             pass

#     if start_date_str:
#         try:
#             start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#             q &= Q(due_date__gte=start_date)
#         except ValueError:
#             pass

#     if end_date_str:
#         try:
#             end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#             q &= Q(due_date__lte=end_date)
#         except ValueError:
#             pass

#     tasks = tasks.filter(q)

#     paginator = Paginator(tasks, 5)  # Assuming 5 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)

#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index  # Adjust to ensure row numbers start from 1

#     # Retain search parameters in pagination links
#     query_params = request.GET.copy()
#     query_params.pop('page', True)
#     query_string = query_params.urlencode()

#     return render(request, 'worker_view_assigned_work.html', {
#         'q': tasks, 
#         'obj': obj, 
#         'sname': sname, 
#         'start_date': start_date_str, 
#         'end_date': end_date_str,
#         'query_string': query_string
#     })




def worker_task_report(request):
    obj = Task.objects.filter(assigned_worker_id=request.session['w_id'], status='completed')
    tasksss=obj.count()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        q = Q(assigned_worker_id=request.session['w_id'], status='completed')
        
        if sname:
            q &= Q(task_name__icontains=sname) | Q(status__icontains=sname) | Q(Priority__icontains=sname)
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                q |= Q(due_date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                q &= Q(due_date__gte=start_date)
                if end_date_str:
                    try:
                        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                        q &= Q(due_date__lte=end_date)
                    except ValueError:
                        pass
            except ValueError:
                pass

        obj = Task.objects.filter(q)
        tasksss=obj.count()

    paginator = Paginator(obj, 5)  # Assuming 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index   # Adjust to ensure row numbers start from 1

    return render(request, 'worker_task_report.html', {'obj': obj,'tasksss':tasksss})











def task_completed(request,id):
    qa=Task.objects.get(id=id)
    qa.status='completed'
    qa.save()

    return HttpResponse("<script>alert('Successfully updated');window.location='/worker_view_assigned_work'</script>")


#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully Updated 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/worker_home';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)  


def inventory_add(request):
    # animals = inventory.objects.all()
    if request.method == 'POST':
        t = request.POST.get('t')
        p = request.POST.get('name')
        c = request.POST.get('model')
        # a = request.POST.get('s')
        b = request.POST.get('b')

        
        new_animal = inventory(
            type=t,
            name=p,
            brand=b,
            model=c,
            farmer_id=request.session['login_id'],
            ls='none'

        )
        new_animal.save()
        return HttpResponse("<script>alert('Successfully Added');window.location='/inventory_add'</script>")


    return render(request, 'inventory.html')



def inventory_delete(request,id):
    qa=inventory.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_inventory'</script>")


# def admin_view_inventory(request):

#     q=inventory.objects.all()
#     return render(request,'admin_view_inventory.html',{'q':q})


def admin_view_inventory(request):

    q=inventory.objects.all()
    paginator = Paginator(q, 5)
    page_number = request.GET.get('page')
    q= paginator.get_page(page_number)
    
    for index, item in enumerate(q.object_list, start=q.start_index()):
        item.row_number = index

    
    return render(request,'admin_view_inventory.html',{'q':q})






def inventory_update(request,id):
    today = date.today().strftime('%Y-%m-%d')

    # q=inventory.objects.all()
    qa=inventory.objects.get(id=id)
    if 'update' in request.POST:
        t = request.POST.get('t')
        p = request.POST.get('name')
        c = request.POST.get('model')
        a = request.POST.get('s')
        b = request.POST.get('b')

        qa.type=t
        qa.name=p
        qa.model=c
        qa.ls=a
        qa.brand=b

        qa.save()
        return HttpResponse("<script>alert('Successfully updated');window.location='/admin_view_inventory'</script>")
    

   

    return render(request,'admin_view_inventory.html',{'qa':qa,'today':today})




def events_report(request):
    today = date.today()
    q = Event.objects.filter(End_date__gte=today)
    return render(request, 'event_report.html', {'q': q})



def contact_add(request):
    animals =contact.objects.all()
    if request.method == 'POST':
        t = request.POST.get('t')
        p = request.POST.get('name')
        c = request.POST.get('c')
        a = request.POST.get('e')
        b = request.POST.get('p')
        ci = request.POST.get('ci')
        
        new_animal = contact(
            type=t,
            name=p,
            Company=c,
            email=a,
            phone=b,
            city=ci

        )
        new_animal.save()

        return HttpResponse("<script>alert('Successfully Added');window.location='/contact_add'</script>")


    return render(request, 'contac.html')








def admin_view_contact(request):
    obj = contact.objects.all()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
    

        q = Q()
        if sname:
            q |= Q(name__icontains=sname)
            q |= Q(Company__icontains=sname)
            q |= Q(type__icontains=sname)
         

      

        obj = contact.objects.filter(q)


    # Filter the complaints based on the query
    paginator = Paginator(obj, 4)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)
    
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index


    return render(request, 'admin_view_contact.html', {'obj': obj})







def update_contact(request,id):
    # animals =contact.objects.all()
    qa =contact.objects.get(id=id)

    if request.method == 'POST':
        t = request.POST.get('t')
        p = request.POST.get('name')
        c = request.POST.get('c')
        a = request.POST.get('e')
        b = request.POST.get('p')
        ci = request.POST.get('ci')
        print("---------------",t)
    
        qa.type=t
        qa.name=p
        qa.Company=c
        qa.email=a
        qa.phone=b
        qa.city=ci
        qa.save()

        return HttpResponse("<script>alert('Successfully Added');window.location='/admin_view_contact'</script>")

    return render(request, 'admin_view_contact.html',{'qa':qa})




def contact_delete(request,id):
    qa=contact.objects.get(id=id)
    qa.delete()
    return HttpResponse("<script>alert('Successfully deleted');window.location='/admin_view_contact'</script>")

#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully deleted 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/contact_add';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)

def view_worker(request):
    obj = Worker.objects.all()
    paginator = Paginator(obj, 4)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)

    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index

    return render(request, 'view_worker.html', {'obj': obj})

def w_accept(request,id):
    obj1=Login.objects.get(login_id=id)
    obj=Worker.objects.get(login_id=id)

    obj1.usertype="worker"
    obj.farmer_id=request.session['login_id']
    obj1.save()
    obj.save()
    return HttpResponse("<script>alert('Successfully Accepted ');window.location='/farmer_home'</script>")

#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully Accepted 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/farmer_home';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)

def w_reject(request,id):
    obj=Worker.objects.get(login_id=id)
    obj1=Login.objects.get(login_id=id)
    obj.delete()
    obj1.delete()
    return HttpResponse("<script>alert('Successfully Rejected');window.location='/farmer_home'</script>")




#     return HttpResponse( """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
       
#         <h3 style="color:red;">Successfully Reject 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = '/farmer_home';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """)



# def worker_plant(request):
#     q=Worker.objects.get(id=request.session['w_id'])
#     e=q.id
#     print('eeeeeeeeee',e)
#     obj=plant.objects.filter(farmer_id=e)
#     return render(request,'worker_plant.html',{'obj':obj})

def worker_plant(request):
    # Initial query filtering by worker_id from session
    obj = plant.objects.filter(worker_id=request.session['w_id'])

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        q = Q()
        # Apply search filter across all relevant fields if sname is provided
        if sname:
            q |= (
                Q(name__icontains=sname) |
                Q(location_type__icontains=sname) |
                Q(planting_fomate__icontains=sname) |
                Q(variety__icontains=sname)
            )

            # Additionally check if 'sname' can be interpreted as a date and apply to Plant_date
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                q |= Q(Plant_date=sname_date)
            except ValueError:
                pass

        # Apply date range filters
        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                q &= Q(Plant_date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                q &= Q(Plant_date__lte=end_date)
            except ValueError:
                pass

        obj = plant.objects.filter(q, worker_id=request.session['w_id'])

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    return render(request, 'worker_plant.html', {'obj': obj})


# def worker_plant(request):
#     obj = plant.objects.filter(worker_id=request.session['w_id'])

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(name__icontains=sname)
#             q |= Q(location_type__icontains=sname)
#             q |= Q(planting_fomate__icontains=sname)
#             q |= Q(variety__icontains=sname) # Correct field name assumed here
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(Plant_date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(Plant_date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(Plant_date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = plant.objects.filter(q, worker_id=request.session['w_id'])
#     paginator = Paginator(obj, 5)  # Paginate with 5 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)

#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index  # Row numbers starting from 1
#     return render(request, 'worker_plant.html', {'obj': obj})




# from django.shortcuts import render
# from django.core.paginator import Paginator
# from django.db.models import Q
# from datetime import datetime

# def worker_plant_report(request):
#     # Initial query
#     obj = plant.objects.filter(worker_id=request.session['w_id'], status='completed')
#     pcount = obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         # Initialize Q object for filtering
#         q = Q(worker_id=request.session['w_id'], status='completed')
        
#         # Apply search name filter
#         if sname:
#             q &= (Q(name__icontains=sname) | Q(location_type__icontains=sname) | Q(planting_fomate__icontains=sname) | Q(variety__icontains=sname))
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(Plant_date=sname_date)
#             except ValueError:
#                 pass

#         # Apply date range filters
#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q &= Q(Plant_date__gte=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q &= Q(Plant_date__lte=end_date)
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         # Apply the filter to the queryset
#         obj = plant.objects.filter(q)
#         pcount = obj.count()

#     paginator = Paginator(obj, 5)  # Paginate with 5 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)

#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index   # Row numbers starting from 1

#     return render(request, 'worker_plant_report.html', {'obj': obj, 'pcount': pcount})





from django.db.models import Q
from datetime import datetime

def worker_plant_report(request):
    # Initial query filtering by worker_id and status 'completed'
    query = Q(worker_id=request.session['w_id'], status='completed')
    
    if request.method == "POST":
        search_query = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        # Apply search filter across all relevant fields
        if search_query or start_date_str or end_date_str:
            search_conditions = Q()

            # Use OR conditions across all relevant fields for search_query
            if search_query:
                search_conditions |= (
                    Q(name__icontains=search_query) |
                    Q(location_type__icontains=search_query) |
                    Q(planting_fomate__icontains=search_query) |
                    Q(variety__icontains=search_query) |
                    Q(Plant_date__icontains=search_query) |
                    Q(status__icontains=search_query)
                )

                # Additionally check if 'sname' can be interpreted as a date and apply to Plant_date
                try:
                    search_date = datetime.strptime(search_query, '%Y-%m-%d').date()
                    search_conditions |= Q(Plant_date=search_date)
                except ValueError:
                    pass

            # Apply date range filters
            if start_date_str:
                try:
                    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                    search_conditions &= Q(Plant_date__gte=start_date)
                except ValueError:
                    pass

            if end_date_str:
                try:
                    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                    search_conditions &= Q(Plant_date__lte=end_date)
                except ValueError:
                    pass

            # Combine the search conditions with the initial query
            query &= search_conditions

    # Apply the constructed query to filter the queryset
    obj = plant.objects.filter(query)
    print("----------------", obj)
    pcount = obj.count()

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index   # Row numbers starting from 1

    return render(request, 'worker_plant_report.html', {'obj': obj, 'pcount': pcount})





# def worker_harvest(request):
#     obj = harvesting.objects.filter(worker_id=request.session['w_id'])

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(name__icontains=sname)
#             q |= Q(size__icontains=sname)
#             q |= Q(variety__icontains=sname)
#             q |= Q(location_type__icontains=sname)
            
#              # Correct field name assumed here
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(harvesting_date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(harvesting_date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(harvesting_date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = harvesting.objects.filter(q, worker_id=request.session['w_id'])

#     paginator = Paginator(obj, 5)  # Paginate with 5 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)

#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index  # Row numbers starting from 1

#     return render(request, 'worker_harvesting.html', {'obj': obj})



def worker_harvest(request):
    # Initial query filtering by worker_id
    query = Q(worker_id=request.session['w_id'])

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        # Apply search filter across all relevant fields
        if sname or start_date_str or end_date_str:
            search_conditions = Q()

            # Use OR conditions across all relevant fields for sname
            if sname:
                search_conditions |= (
                    Q(name__icontains=sname) |
                    Q(size__icontains=sname) |
                    Q(variety__icontains=sname) |
                    Q(location_type__icontains=sname)
                )

                # Additionally check if 'sname' can be interpreted as a date and apply to harvesting_date
                try:
                    sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                    search_conditions |= Q(harvesting_date=sname_date)
                except ValueError:
                    pass

            # Apply date range filters
            if start_date_str:
                try:
                    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                    search_conditions &= Q(harvesting_date__gte=start_date)
                except ValueError:
                    pass

            if end_date_str:
                try:
                    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                    search_conditions &= Q(harvesting_date__lte=end_date)
                except ValueError:
                    pass

            # Combine the search conditions with the initial query
            query &= search_conditions

    # Apply the constructed query to filter the queryset
    obj = harvesting.objects.filter(query)

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    return render(request, 'worker_harvesting.html', {'obj': obj})

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime

def worker_harvest_report(request):
    obj = harvesting.objects.filter(worker_id=request.session['w_id'], status='completed')
    pcount = obj.count()

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        q = Q(worker_id=request.session['w_id'], status='completed')
        
        if sname:
            q &= Q(name__icontains=sname) | Q(size__icontains=sname) | Q(location_type__icontains=sname)
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                q |= Q(harvesting_date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                q &= Q(harvesting_date__gte=start_date)
                if end_date_str:
                    try:
                        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                        q &= Q(harvesting_date__lte=end_date)
                    except ValueError:
                        pass
            except ValueError:
                pass

        # Apply the filter to the queryset
        obj = harvesting.objects.filter(q)
        pcount = obj.count()

    paginator = Paginator(obj, 5)  # Assuming 5 items per page
    page_number = request.GET.get('page', 1)
    obj = paginator.get_page(page_number)
    
    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Adjust to ensure row numbers start from 1
    
    return render(request, 'worker_harvest_report.html', {'obj': obj, 'pcount': pcount})






def planted(request,id):
    obj=plant.objects.get(id=id)
    obj.status='completed'
    obj.save()
    return HttpResponse("<script>alert('Successfully Updated');window.location='/worker_plant'</script>")






def harvestingr(request,id):
    obj=harvesting.objects.get(id=id)
    obj.status='completed'
    obj.save()

    return HttpResponse("<script>alert('Successfully Updated');window.location='/worker_harvest'</script>")


# def planted_rep(request):
#     obj = plant.objects.filter(status='completed')
#     total_plants = obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(name__icontains=sname)
#             q |= Q(location_type__icontains=sname)
#             q |= Q(planting_fomate__icontains=sname)  # Correct field name assumed here
#             q |= Q(worker__first_name__icontains=sname)  # Correct field name assumed here
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(Plant_date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(Plant_date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(Plant_date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = plant.objects.filter(q,status='completed')
#         total_plants = obj.count()
        
#     paginator = Paginator(obj, 5)  # Assuming 10 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)
#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index
        
#     return render(request, 'planted_rep.html', {'obj': obj,'total_plants': total_plants})




def planted_rep(request):
    # Start with filtering by status 'completed'
    query = Q(status='completed')

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        search_conditions = Q()

        if sname:
            search_conditions |= (
                Q(name__icontains=sname) |
                Q(location_type__icontains=sname) |
                Q(planting_fomate__icontains=sname) |
                Q(worker__first_name__icontains=sname)
            )
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(Plant_date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(Plant_date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(Plant_date__lte=end_date)
            except ValueError:
                pass

        # Apply the search conditions to the queryset
        query &= search_conditions

    # Filter the queryset based on the constructed query
    obj = plant.objects.filter(query)
    total_plants = obj.count()

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    context = {
        'obj': obj,
        'total_plants': total_plants
    }
    return render(request, 'planted_rep.html', context)


# def planted_rep(request):
#     plants = plant.objects.filter(status='completed')
#     total_plants = plants.count()
#     context = {
#         'plants': plants,
#         'total_plants': total_plants
#     }
#     return render(request, 'planted_rep.html', context)




# def harvesting_rep(request):
#     obj = harvesting.objects.filter(status='completed')
#     total_plants = obj.count()

#     if request.method == "POST":
#         sname = request.POST.get('sname', '')
#         start_date_str = request.POST.get('start_date', '')
#         end_date_str = request.POST.get('end_date', '')

#         q = Q()
#         if sname:
#             q |= Q(name__icontains=sname)
#             q |= Q(variety__icontains=sname)
#             q |= Q(location_type__icontains=sname)
#             q |= Q(status__icontains=sname)
#             q |= Q(worker__first_name__icontains=sname)  # Correct field name assumed here
#             try:
#                 sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
#                 q |= Q(harvesting_date=sname_date)
#             except ValueError:
#                 pass

#         if start_date_str:
#             try:
#                 start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#                 q |= Q(harvesting_date=start_date)
#                 if end_date_str:
#                     try:
#                         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#                         q |= Q(harvesting_date__range=[start_date, end_date])
#                     except ValueError:
#                         pass
#             except ValueError:
#                 pass

#         obj = harvesting.objects.filter(q,status='completed')
#         total_plants = obj.count()

#     paginator = Paginator(obj, 5)  # Assuming 10 items per page
#     page_number = request.GET.get('page', 1)
#     obj = paginator.get_page(page_number)
#     # Calculate row numbers based on page_obj
#     for index, item in enumerate(obj.object_list, start=obj.start_index()):
#         item.row_number = index
#     return render(request, 'harvesting_rep.html', {'obj': obj,'total_plants': total_plants})


def harvesting_rep(request):
    # Start with filtering by status 'completed'
    query = Q(status='completed')

    if request.method == "POST":
        sname = request.POST.get('sname', '')
        start_date_str = request.POST.get('start_date', '')
        end_date_str = request.POST.get('end_date', '')

        search_conditions = Q()
        if sname:
            search_conditions |= (
                Q(name__icontains=sname) |
                Q(variety__icontains=sname) |
                Q(location_type__icontains=sname) |
                Q(status__icontains=sname) |
                Q(worker__first_name__icontains=sname)
            )
            try:
                sname_date = datetime.strptime(sname, '%Y-%m-%d').date()
                search_conditions |= Q(harvesting_date=sname_date)
            except ValueError:
                pass

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(harvesting_date__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                search_conditions &= Q(harvesting_date__lte=end_date)
            except ValueError:
                pass

        # Apply the search conditions to the queryset
        query &= search_conditions

    # Filter the queryset based on the constructed query
    obj = harvesting.objects.filter(query)
    total_plants = obj.count()

    # Pagination
    paginator = Paginator(obj, 5)  # Paginate with 5 items per page
    page_number = request.GET.get('page', 1)  # Default to page 1 if no page is specified
    obj = paginator.get_page(page_number)

    # Calculate row numbers based on page_obj
    for index, item in enumerate(obj.object_list, start=obj.start_index()):
        item.row_number = index  # Row numbers starting from 1

    context = {
        'obj': obj,
        'total_plants': total_plants
    }

    return render(request, 'harvesting_rep.html', context)



# def planted_rep(request):
#     q=plant.objects.filter(status='completed')
#     return render(request,'planted_rep.html',{'q':q})




def admin_task_reportsss(request):
    qa=Task.objects.all()
    paginator = Paginator(qa, 5)
    page_number = request.GET.get('page')
    qa= paginator.get_page(page_number)
    
    for index, item in enumerate(qa.object_list, start=qa.start_index()):
        item.row_number = index
    
    return render(request,'admin_task_reportsss.html',{'q':qa})


def fertilizer(request):
    data={}
    val=[]
    vals=[]
    out=""
    if request.method=="POST":
        temp=request.POST['Temperature']
        hum=request.POST['Humidity']
        moi=request.POST['Moisture']
        soil=request.POST['Soil_type']
        crop=request.POST['Crop_type']
        nit=request.POST['Nitrogen']
        pot=request.POST['Potassium']
        pho=request.POST['Phosphorus']

        val.append(temp)
        val.append(hum)
        val.append(moi)
        val.append(soil)
        val.append(crop)
        val.append(nit)
        val.append(pot)
        val.append(pho)

        vals.append(val)
        print("asssss",vals)
        out=predictfertilizerss(vals)
        q= Fertilizer(
            soil_type=soil,
            crop_type=crop,
            temperature=temp,
            humidity=hum,
            moisture=moi,
            nitrogen=nit,
            potassium=pot,
            phosphorus=pho,
            out=out,

        )
        q.save()

        # Output=request.args['Output']
        # print("ok.......................",Output)
        # q="insert into fertilizer_predict values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(logid,temp,hum,moi,soil,crop,nit,pot,pho,out)
        # print(q)
        # res=insert(q)
        if out==1:
            out='Urea'
        elif out==2:
            out='Dap'
        elif out==3:
            out='14-35-14'
        elif out==4:
            out='28-28'
        elif out==5:
            out='17-17-17'
        elif out==6:
            out='20-20'
        elif out==7:
            out='28-28'
        print("outsssssssssssssss" + out)
    return render(request,'customer_predict_fertilizer.html',{'out':out})


