from django.shortcuts import render,redirect


from .models import My_Details

# Create your views here.

def my_form_view(request):

    if request.method == 'POST':
        name_ = request.POST['name']
        email_ = request.POST['email']
        city_ = request.POST['city']
        number_ = request.POST['mobile']

        image_ = request.FILES.get('image')

        new_detals = My_Details.objects.create(
            name = name_,
            email = email_,
            city = city_,
            number = number_,
            image=image_
        )
        new_detals.save()
        return redirect(My_read_view)


    return render(request,'myform.html')

def My_read_view(request):
    query = request.GET.get('search')
    if query:
        mydata = My_Details.objects.filter(name__icontains=query)
        
    else:
        mydata = My_Details.objects.all()

    context = {
        'mydata' : mydata
    }
    return render(request,'read.html',context)

def edit_get_data(request,pk):
    get_value = My_Details.objects.get(id=pk)
    context = {
        'mydata' : get_value
    }
    return render(request,'edit.html',context)

def update_my_data(request,pk):
    get_value = My_Details.objects.get(id=pk)

    get_value.name = request.POST['name']
    get_value.email = request.POST['email']
    get_value.city = request.POST['city']
    get_value.number = request.POST['mobile']
    get_value.image = request.FILES['image']
    if not get_value.image:
        get_value.save()

    

    get_value.save()
    print(get_value.name)
    return redirect('My_read_view')


def delete_view(request,pk):
    get_data = My_Details.objects.get(id=pk)
    get_data.delete()
    return redirect('My_read_view')


