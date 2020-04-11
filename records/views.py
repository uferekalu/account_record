from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import DeptForm
from django.db.models import Q
from django.db.models import Sum
from .models import (
    Mechanical_Dept,
    Electrical_Dept,
    Civil_Dept,
    Computer_Science_Dept,
    Comp_Engr_Dept,
    Pharmaceutical_Tech_Dept,
    Science_Lab_Tech_Dept,
    Food_Tech_Dept,
    Dispensary_and_Opticiary_Dept,
    Agric_Engr_Dept
)
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    form = DeptForm()
    return render(request, 'records/index.html', {
        'form': form
    })
    
def mech_details(request):
    mech_lists = Mechanical_Dept.objects.all().order_by('id')
    mech_total = Mechanical_Dept.objects.aggregate(Sum('total'))
    total = mech_total['total__sum']
    
    if mech_lists:
        return render(request, 'records/mech_engr.html', {
            'mech_lists': mech_lists,
            'total': total
        })
    else:
        department = 'Mechanical Engineering'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })    

def elect_details(request):
    elect_lists = Electrical_Dept.objects.all().order_by('id')
    elect_total = Electrical_Dept.objects.aggregate(Sum('total'))
    total = elect_total['total__sum']
    if elect_lists:
        return render(request, 'records/elect_engr.html', {
            'elect_lists': elect_lists,
            'total': total
        })
    else:
        department = 'Electrical Engineering'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        }) 

def civil_details(request):
    civil_lists = Civil_Dept.objects.all().order_by('id')
    civil_total = Civil_Dept.objects.aggregate(Sum('total'))
    total = civil_total['total__sum']
    if civil_lists:
        return render(request, 'records/civil_engr.html', {
            'civil_lists': civil_lists,
            'total': total
        })
    else:
        department = 'Civil Engineering'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })  

def comp_engr_details(request):
    comp_engr_lists = Comp_Engr_Dept.objects.all().order_by('id')
    comp_engr_total = Comp_Engr_Dept.objects.aggregate(Sum('total'))
    total = comp_engr_total['total__sum']
    if comp_engr_lists:
        return render(request, 'records/comp_engr.html', {
            'comp_engr_lists': comp_engr_lists,
            'total': total
        })
    else:
        department = 'Computer Engineering'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })  

def agric_engr_details(request):
    agric_engr_lists = Agric_Engr_Dept.objects.all().order_by('id')
    agric_engr_total = Agric_Engr_Dept.objects.aggregate(Sum('total'))
    total = agric_engr_total['total__sum']
    if agric_engr_lists:
        return render(request, 'records/agric_engr.html', {
            'agric_engr_lists': agric_engr_lists,
            'total': total
        })
    else:
        department = 'Agricultural Engineering'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })  

def computer_science_details(request):
    science_lists = Computer_Science_Dept.objects.all().order_by('id')
    science_total = Computer_Science_Dept.objects.aggregate(Sum('total'))
    total = science_total['total__sum']
    if science_lists:
        return render(request, 'records/comp_sci.html', {
            'science_lists': science_lists,
            'total': total
        })
    else:
        department = 'Computer Science'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })  

def science_lab_details(request):
    science_lab_lists = Science_Lab_Tech_Dept.objects.all().order_by('id')
    sci_lab_total = Science_Lab_Tech_Dept.objects.aggregate(Sum('total'))
    total = sci_lab_total['total__sum']
    if science_lab_lists:
        return render(request, 'records/sci_lab_tech.html', {
            'science_lab_lists': science_lab_lists,
            'total': total
        })
    else:
        department = 'Science Laboratory Technology'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })  

def food_tech_details(request):
    food_lists = Food_Tech_Dept.objects.all().order_by('id')
    food_total = Food_Tech_Dept.objects.aggregate(Sum('total'))
    total = food_total['total__sum']
    if food_lists:
        return render(request, 'records/food_tech.html', {
            'food_lists': food_lists,
            'total': total
        })
    else:
        department = 'Food Science Technology'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        }) 

def pharm_tech_details(request):
    pharm_lists = Pharmaceutical_Tech_Dept.objects.all().order_by('id')
    pharm_total = Pharmaceutical_Tech_Dept.objects.aggregate(Sum('total'))
    total = pharm_total['total__sum']
    if pharm_lists:
        return render(request, 'records/pharm_tech.html', {
            'pharm_lists': pharm_lists,
            'total':total
        })
    else:
        department = 'Pharmaceutical Technology'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        }) 

def dispense_details(request):
    dispensary_lists = Dispensary_and_Opticiary_Dept.objects.all().order_by('id')
    dispense_total = Dispensary_and_Opticiary_Dept.objects.aggregate(Sum('total'))
    total = dispense_total['total__sum']
    if dispensary_lists:
        return render(request, 'records/opticiary.html', {
            'dispensary_lists': dispensary_lists,
            'total': total
        })
    else:
        department = 'Dispensary and Opticiary'
        none = 'No records found..'
        return render(request, 'records/none.html', {
            'department': department,
            'none': none
        })  


def add_details(request):
    current_date = timezone.now()
    if request.method == 'POST':
        form = DeptForm(request.POST)
        if form.is_valid():
            dept = form.cleaned_data['dept']
            name = form.cleaned_data['name']
            amount = form.cleaned_data['amount']
            balance = form.cleaned_data['balance']
            total = form.cleaned_data['total']
            if dept == 'ME':
                Mechanical_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/mech_details')
            if dept =='EE':
                Electrical_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/elect_details')
            if dept =='CE':
                Civil_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/civil_details')
            if dept =='CTE':
                Comp_Engr_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/comp_engr_details')
            if dept =='AE':
                Agric_Engr_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/agric_engr_details')
            if dept =='CS':
                Computer_Science_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/computer_science_details')
            if dept =='SLT':
                Science_Lab_Tech_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/science_lab_details')
            if dept =='FST':
                Food_Tech_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/food_tech_details')
            if dept =='PT':
                Pharmaceutical_Tech_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/pharm_tech_details')
            if dept =='DOP':
                Dispensary_and_Opticiary_Dept.objects.create(added_date=current_date, name_of_students=name, amount=amount, balance=balance, total=total)
                return HttpResponseRedirect('/dispense_details')

    else:
        form = DeptForm()
        return render(request, 'records/index.html', {
            'form': form
        })

def delete_mech(request, mech_id):
    Mechanical_Dept.objects.get(id=mech_id).delete()
    return HttpResponseRedirect("/mech_details")

def delete_elect(request, elect_id):
    Electrical_Dept.objects.get(id=elect_id).delete()
    return HttpResponseRedirect("/elect_details")

def delete_civil(request, civil_id):
    Civil_Dept.objects.get(id=civil_id).delete()
    return HttpResponseRedirect("/civil_details")

def delete_comp_engr(request, comp_engr_id):
    Comp_Engr_Dept.objects.get(id=comp_engr_id).delete()
    return HttpResponseRedirect("/comp_engr_details")

def delete_comp_sci(request, comp_sci_id):
    Computer_Science_Dept.objects.get(id=comp_sci_id).delete()
    return HttpResponseRedirect("/computer_science_details")

def delete_agric(request, agric_id):
    Agric_Engr_Dept.objects.get(id=agric_id).delete()
    return HttpResponseRedirect("/agric_engr_details")

def delete_sci_lab(request, sci_lab_id):
    Science_Lab_Tech_Dept.objects.get(id=sci_lab_id).delete()
    return HttpResponseRedirect("/science_lab_details")

def delete_food(request, food_id):
    Food_Tech_Dept.objects.get(id=food_id).delete()
    return HttpResponseRedirect("/food_tech_details")

def delete_pharm(request, pharm_id):
    Pharmaceutical_Tech_Dept.objects.get(id=pharm_id).delete()
    return HttpResponseRedirect("/pharm_tech_details")

def delete_dispense(request, dispense_id):
    Dispensary_and_Opticiary_Dept.objects.get(id=dispense_id).delete()
    return HttpResponseRedirect("/dispense_details")

def mech_update(request, id):
    dept = get_object_or_404(Mechanical_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('mech_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def elect_update(request, id):
    dept = get_object_or_404(Electrical_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('elect_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def civil_update(request, id):
    dept = get_object_or_404(Civil_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('civil_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def comp_sci_update(request, id):
    dept = get_object_or_404(Computer_Science_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('computer_science_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def comp_engr_update(request, id):
    dept = get_object_or_404(Comp_Engr_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('comp_engr_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def pharm_update(request, id):
    dept = get_object_or_404(Pharmaceutical_Tech_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('pharm_tech_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def sci_lab_update(request, id):
    dept = get_object_or_404(Science_Lab_Tech_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('science_lab_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def food_update(request, id):
    dept = get_object_or_404(Food_Tech_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('food_tech_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def dispense_update(request, id):
    dept = get_object_or_404(Dispensary_and_Opticiary_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('dispense_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def agric_update(request, id):
    dept = get_object_or_404(Agric_Engr_Dept, id=id)
    form = DeptForm(request.POST, dept)
    if form.is_valid():
        form.save()
        return redirect('agric_engr_details')
    return render(request, 'records/index.html', {
        'form': form
    })

def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(name_of_students__icontains=query) | Q(amount__icontains=query) |Q(balance__icontains=query)
            results = Mechanical_Dept.objects.filter(lookups)
            elect_results = Electrical_Dept.objects.filter(lookups)
            civil_results = Civil_Dept.objects.filter(lookups)
            comp_sci_results = Computer_Science_Dept.objects.filter(lookups)
            comp_engr_results = Comp_Engr_Dept.objects.filter(lookups)
            pharm_results = Pharmaceutical_Tech_Dept.objects.filter(lookups)
            sci_results = Science_Lab_Tech_Dept.objects.filter(lookups)
            food_results = Food_Tech_Dept.objects.filter(lookups)
            dispense_results = Dispensary_and_Opticiary_Dept.objects.filter(lookups)
            agric_results = Agric_Engr_Dept.objects.filter(lookups)
            context = {
                'results': results,
                'elect_results': elect_results,
                'civil_results': civil_results,
                'comp_sci_results': comp_sci_results,
                'comp_engr_results': comp_engr_results,
                'pharm_results': pharm_results,
                'sci_results': sci_results,
                'food_results': food_results,
                'dispense_results': dispense_results,
                'agric_results': agric_results,
                'submitbutton': submitbutton
            }
            return render(request, 'records/search.html', context)
        else:
            return render(request, 'records/search.html')
    else:
        return render(request, 'records/index.html')
