from . import stripe
from users.models import User

def create_charge(order, user, card):
    return stripe.Charge.create(
        amount=int(order.total), #En centavos
        currency='USD',
        description=order.description,
        customer=user.customer_id,
        source=card.card_id, #Método de pago
        metadata={
            'order_id': order.id
        }
    )


user = User.objects.get(pk=1)

customer = create_customer(user)

user.customer_id = customer.id
user.save()