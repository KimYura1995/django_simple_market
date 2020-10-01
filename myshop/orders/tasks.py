from myshop.celery import app
from django.core.mail import send_mail

from .models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}'
    message = f'Уважаемый {order.first_name},\n\nВы успешно оформили заказ. Ваш заказ №{order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
