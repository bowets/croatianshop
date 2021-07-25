from django.http import HttpResponse
from django.http.response import HttpResponseServerError
from .models import Order


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """Handle a generic / unknonw / unexpected webhook event"""

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
            """Handle the payment_intent.succeeded webhook event from Stripe"""
            intent = event.data.object
            pid = intent.id
            cart = intent.metadata.cart
            save_info = intent.metadata.save_info

            billing_details = intent.charges.data[0].billing_details
            shipping_details = intent.shipping
            grand_total = round(intent.data.charges[0].amount / 100, 2)

            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None

            order_exists = False
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.country,
                    eircode__iexact=shipping_details.postal_code,
                    town_or_city__iexact=shipping_details.city,
                    street_address1__iexact=shipping_details.line1,
                    street_address2__iexact=shipping_details.line2,
                    county__iexact=shipping_details.state,
                    grand_total__iexact=grand_total,
                )
                order_exists = True
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200
                )
            except Order.DoesNotExist:
                try:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=shipping_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.country,
                        eircode=shipping_details.postal_code,
                        town_or_city=shipping_details.city,
                        street_address1=shipping_details.line1,
                        street_address2=shipping_details.line2,
                        county=shipping_details.state,
                        grand_total=grand_total,
                    )
                    for item_id, item_data in json.loads(cart).items():
                        product = Product.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order = order,
                            product = product,
                            quantity = item_data,
                        )
                        order_line_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR {E}',
                    staus=500)
            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200
            )


    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.failed webhook event from Stripe"""

        return HttpResponse(
            content=f'Payment Failed Webhook received: {event["type"]}',
            status=200
        )
