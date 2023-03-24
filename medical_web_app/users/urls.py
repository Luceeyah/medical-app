from django.urls import path
from .views import appointment_approval, FirstPage, appointment, show_doc, search_doc, HomePage,RegisterDoc, Register, Login, add_profile, chart, table


urlpatterns = [
    path('', FirstPage, name="first-page"),
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('registerDoc/', RegisterDoc, name="registerdoc-page"),

    path('login/', Login, name="login-page"),
    path('profile/', add_profile, name="add-profile"),
    path('table/', table, name="table-page"),
    path('search_doc/', search_doc, name="search-doc"),
    path('show_doc/<doc_id>', show_doc, name="show-doc"),
    path('appointment/', appointment, name="appointment"),
    path('appointment_approval/', appointment_approval, name="appointment-approval"),
    path('chart/', chart, name='chart-data'),
]
