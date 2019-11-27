from django.http import HttpResponse
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import ListView, TemplateView, CreateView
from dj_pizzas.models import *
from dj_pizzas.forms import *
from django.template import Context, Template


class Home(TemplateView):
	template_name = 'index.html'


class CreateBasket(FormView):
	template_name = 'pizza_constructor.html'
	form_class = BasketForm
	success_url = '/basket/'

	def form_valid(self, form):
		pizza = Pizza.objects.get(id=form.cleaned_data.get('pizza_id'))
		count = form.cleaned_data.get('count')
		instance_pizza = pizza.make_order(count)
		order, created = Order.objects.get_or_create(user=self.request.user)
		order.pizzas.add(instance_pizza)
		order.price = order.get_price()
		order.save()
		return super().form_valid(form)


class UpdateOrder(UpdateView):
	model = Order
	form_class = UpdateOrderForm
	template_name = 'update_order.html'
	success_url = '/basket/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		curent_order = Order.objects.filter(user=self.request.user)
		user = 0
		context['instances_pizzas'] = InstancePizza.objects.all().filter(order_template__user=self.request.user)
		return context

	def form_valid(self, form):
		curent_order = Order.objects.get(user=self.request.user)
		print('PRICE1', curent_order.price, curent_order.id)
		curent_order.change_order_price()
		Order.objects.filter(user=self.request.user).update(price=Order.objects.get(user=self.request.user).get_price())
		curent_order.change_order_price()
		print('PRICE3', curent_order.price, curent_order.pizzas, curent_order.id)
		order = Order.objects.get(id=1)
		order.price = 200
		order.save()
		print('EXAMPLE: ', order.order_template.all())
		print('PRICE 4', curent_order.price, curent_order.pizzas, curent_order.id)
		return super().form_valid(form)


class ListOrders(ListView):
	model = Order
	template_name = 'list_objects.html'

	def get_queryset(self):
		order = Order.objects.all()
		return order

	def get_context_data(self, **kwargs):
		context = {'object_name1': 'заказов', 'object_name2': 'заказа'}
		return super().get_context_data(**context)


class UpdateInstancePizza(UpdateView):
	model = InstancePizza
	form_class = EditInstancePizzaForm
	template_name = 'update.html'
	success_url = '/'


class CreateDough(CreateView):
	model = Dough
	form_class = CreateDoughForm
	template_name = 'create_object.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = {'object_name': 'коржа'}
		return super().get_context_data(**context)


class ListDough(ListView):
	model = Dough
	template_name = 'list_objects.html'

	def get_queryset(self):
		order = Dough.objects.all()
		return order

	def get_context_data(self, **kwargs):
		context = {'object_name1': 'коржей', 'object_name2': 'коржа'}
		return super().get_context_data(**context)


class UpdateDough(UpdateView):
	model = Dough
	form_class = EditDoughForm
	template_name = 'update.html'
	success_url = '/'


class CreateSnacks(CreateView):
	model = Snacks
	form_class = CreateSnacksForm
	template_name = 'create_object.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = {'object_name': 'закусок'}
		return super().get_context_data(**context)


class ListSnacks(ListView):
	model = Snacks
	template_name = 'list_objects.html'

	def get_queryset(self):
		order = Snacks.objects.all()
		return order

	def get_context_data(self, **kwargs):
		context = {'object_name1': 'закусок', 'object_name2': 'закуски'}
		return super().get_context_data(**context)


class UpdateSnack(UpdateView):
	model = Snacks
	form_class = EditSnackForm
	template_name = 'update.html'
	success_url = '/'


class CreateTopping(CreateView):
	model = Topping
	form_class = CreateToppingForm
	template_name = 'create_object.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = {'object_name': 'топпинга'}
		return super().get_context_data(**context)


class UpdateTopping(UpdateView):
	model = Topping
	form_class = EditToppingForm
	template_name = 'update.html'
	success_url = '/'


class CommonToppingUpdate(FormView):
	model = Topping
	form_class = UpdateObject
	template_name = 'common_update.html'
	success_url = '/sorter/'

	def form_valid(self, form):
		price_change = form.cleaned_data.get('price_change')
		all_toppings = Topping.objects.all()
		for topping in all_toppings:
			topping.price = topping.price + price_change
			topping.save()
		return super().form_valid(form)


class ToppingSorter(TemplateView):
	template_name = 'list_toppings.html'
	sortering_fields = ['description', 'price', '-price']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		ordering = self.request.GET.get('ordering')
		if ordering not in self.sortering_fields:
			ordering = 'id'
		context['toppings'] = Topping.objects.all().order_by(ordering)
		return context