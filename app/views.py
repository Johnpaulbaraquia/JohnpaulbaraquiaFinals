from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Order
from .models import Customer, Categories, Product, Order, OrderDetail
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import FormView



# dito
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    products = order.products.all()  

    return render(request, 'order_detail.html', {'order': order, 'products': products})

class HomepageView(TemplateView):
    template_name = 'app/home.html'

class AboutpageView(TemplateView):
        template_name = 'app/about.html'

class ContactpageView(TemplateView):
    template_name = 'app/contact.html'
    
class OrderListView(ListView):
    model = Order
    template_name = 'app/order_list.html'
    context_object_name = 'orders'
    
    # dito
class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after signup
        return redirect('login')

    
class SignupPageView(TemplateView):
    template_name = 'app/signup.html'

class LoginPageView(TemplateView):
    template_name = 'app/login.html'
    
# class OrderDetailView(DetailView):
#     model = Order
#     template_name = 'app/order_detail.html'
#     context_object_name = 'order'
    
# class OrderCreateView(CreateView):
#     model = Order  
#     fields = ['customer','stage']
#     template_name = 'app/order_create.html'
#     # success_url = reverse_lazy('order_list')
    
      

# class OrderUpdateView(UpdateView):
#     model = Order
#     template_name = 'app/order_update.html'
#     fields = ['customer','stage']


# class OrderDeleteView(DeleteView):
#     model = Order
#     template_name = 'app/order_delete.html'
#     success_url = reverse_lazy('order_list')
# class SignupView(FormView):
#     template_name = 'registration/signup.html'
#     form_class = UserCreationForm

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)  # Log the user in after signup
#         return redirect('login') 

class LoginPageView(TemplateView):
    template_name = 'app/login.html'

class HomePageView(TemplateView):
    template_name = 'app/home.html'
    
class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class CustomerListView(ListView):
    model = Customer
    template_name = 'app/customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'app/order_detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        customer_orders = Order.objects.filter(customer=self.object)  
        context['order'] = customer_orders  
        return context
    

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
    template_name = 'app/customer_create.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
    template_name = 'app/customer_update.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_delete.html'
    success_url = reverse_lazy('customer_list')

class CategoryListView(ListView):
    model = Categories
    template_name = 'app/category_list.html'

class CategoryDetailView(DetailView):
    model = Categories
    template_name = 'app/category_detail.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['category'].pk)  # Check if pk is correct
        return context
    

class CategoryCreateView(CreateView):
    model = Categories
    fields = ['name', 'description', 'products']
    template_name = 'app/category_create.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Categories
    fields = ['name', 'description', 'products']
    template_name = 'app/category_update.html'
    success_url = reverse_lazy('category_list')
    
    

class CategoryDeleteView(DeleteView):
    model = Categories
    template_name = 'app/category_delete.html'
    success_url = reverse_lazy('category_list')

class ProductListView(ListView):
    model = Product
    template_name = 'app/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock']
    template_name = 'app/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock']
    template_name = 'app/product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_delete.html'
    success_url = reverse_lazy('product_list')

class OrderListView(ListView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_list.html'

class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        return context


class OrderCreateView(CreateView):
    model = Order
    fields = ['customer', 'status', 'products']
    template_name = 'app/order_create.html'

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer', 'status', 'products']
    template_name = 'app/order_update.html'

    def form_valid(self, form):
        if not form.instance.price:
            self.object = form.save()
            form.instance.price = 0.00
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'app/order_delete.html'
    success_url = reverse_lazy('order_list')

class OrderDetailListView(ListView):
    model = OrderDetail
    template_name = 'app/orderdetail_list.html'

class OrderDetailDetailView(DetailView):
    model = OrderDetail
    template_name = 'app/orderdetail_detail.html'

class OrderDetailCreateView(CreateView):
    model = OrderDetail
    fields = ['order', 'product', 'quantity', 'price']
    template_name = 'app/orderdetail_create.html'
    success_url = reverse_lazy('orderdetail_list')

class OrderDetailUpdateView(UpdateView):
    model = OrderDetail
    fields = ['order', 'product', 'quantity', 'price']
    template_name = 'app/orderdetail_update.html'
    success_url = reverse_lazy('orderdetail_list')

class OrderDetailDeleteView(DeleteView):
    model = OrderDetail
    template_name = 'app/orderdetail_delete.html'
    success_url = reverse_lazy('orderdetail_list')



    

    
    




