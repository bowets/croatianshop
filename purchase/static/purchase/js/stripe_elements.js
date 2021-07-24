let stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
let client_secret = $('#id_client_secret').text().slice(1,-1);
console.log(stripe_public_key);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
console.log(elements);

let card = elements.create('card', {
    style: {
      base: {
        iconColor: '#c4f0ff',
        color: '#000',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#DC3545',
        color: '#DC3545',
      },
    },
  });

card.mount('#card-element');