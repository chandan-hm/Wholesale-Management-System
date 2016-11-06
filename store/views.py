from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from store.models import Producer, Payment, Phoneprod, Phonecus, Pays, Product, Receipt, Customer, Cart, Sells, Buys


def login(request):

    return render(request, 'store/login.html')


def index(request):
    return render(request, 'store/index.html')


def producer(request):
    all_producers = Producer.objects.all()
    return render(request, 'store/producer.html', {'all_producers': all_producers})


def detail_producer(request, producer_id):
    prod = Producer.objects.get(pk=producer_id)
    return render(request, 'store/detail_producer.html', {'prod': prod})


class UserFormView(View):
    form_class = UserForm
    template_name = 'store/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('store:index')

            return render(request, self.template_name, {'form': form})


def customer(request):
    all_customers = Customer.objects.all()
    return render(request, 'store/customer.html', {'all_customers': all_customers})


def detail_customer(request, customer_id):
    cus = Customer.objects.get(pk=customer_id)
    return render(request, 'store/detail_customer.html', {'cus': cus})


def product(request):
    all_products = Product.objects.all()
    return render(request, 'store/product.html', {'all_products': all_products})


def detail_product(request, product_id):
    pro = Product.objects.get(pk=product_id)
    return render(request, 'store/detail_product.html', {'pro': pro})


def payment(request):
    all_payment = Payment.objects.all()
    return render(request, 'store/payment.html', {'all_payment': all_payment})
