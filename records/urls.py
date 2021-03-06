from django.urls import path
from .import views

app_name = 'records'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_details/', views.add_details, name='add_details'),
    path('mech_details/', views.mech_details, name='mech_details'),
    path('elect_details/', views.elect_details, name='elect_details'),
    path('civil_details/', views.civil_details, name='civil_details'),
    path('comp_engr_details/', views.comp_engr_details, name='comp_engr_details'),
    path('agric_engr_details/', views.agric_engr_details, name='agric_engr_details'),
    path('computer_science_details/', views.computer_science_details, name='computer_science_details'),
    path('science_lab_details/', views.science_lab_details, name='science_lab_details'),
    path('food_tech_details/', views.food_tech_details, name='food_tech_details'),
    path('pharm_tech_details/', views.pharm_tech_details, name='pharm_tech_details'),
    path('dispense_details/', views.dispense_details, name='dispense_details'),
    path('delete_mech/<int:mech_id>/', views.delete_mech, name='delete_mech'),
    path('delete_elect/<int:elect_id>/', views.delete_elect, name='delete_elect'),
    path('delete_civil/<int:civil_id>/', views.delete_civil, name='delete_civil'),
    path('delete_comp_engr/<int:comp_engr_id>/', views.delete_comp_engr, name='delete_comp_engr'),
    path('delete_comp_sci/<int:comp_sci_id>/', views.delete_comp_sci, name='delete_comp_sci'),
    path('delete_agric/<int:agric_id>/', views.delete_agric, name='delete_agric'),
    path('delete_sci_lab/<int:sci_lab_id>/', views.delete_sci_lab, name='delete_sci_lab'),
    path('delete_food/<int:food_id>/', views.delete_food, name='delete_food'),
    path('delete_pharm/<int:pharm_id>/', views.delete_pharm, name='delete_pharm'),
    path('delete_dispense/<int:dispense_id>/', views.delete_dispense, name='delete_dispense'),
    path('mech_update/<int:id>/', views.mech_update, name='mech_update'),
    path('elect_update/<int:id>/', views.elect_update, name='elect_update'),
    path('civil_update/<int:id>/', views.civil_update, name='civil_update'),
    path('comp_sci_update/<int:id>/', views.comp_sci_update, name='comp_sci_update'),
    path('comp_engr_update/<int:id>/', views.comp_engr_update, name='comp_engr_update'),
    path('pharm_update/<int:id>/', views.pharm_update, name='pharm_update'),
    path('sci_lab_update/<int:id>/', views.sci_lab_update, name='sci_lab_update'),
    path('food_update/<int:id>/', views.food_update, name='food_update'),
    path('dispense_update/<int:id>/', views.dispense_update, name='dispense_update'),
    path('agric_update/<int:id>/', views.agric_update, name='agric_update'),
    path('search/', views.search, name='search'),
]