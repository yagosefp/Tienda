
var stripe = Stripe('pk_test_51MC0gKBbI7O9XQcTrVxaBFuN6TtCQZL41HYhN2XBugqznJfunv9yVSgvfLzfwxE5x4zVcuHygXfVl2JBeGeJrXqm00bRQ5cteX');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');


var elements = stripe.elements();
var style = {
base: {
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};


var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on('change', function(event) {
var displayError = document.getElementById('card-errors')
if (event.error) {
  displayError.textContent = event.error.message;
  $('#card-errors').addClass('alert alert-info');
} else {
  displayError.textContent = '';
  $('#card-errors').removeClass('alert alert-info');
}
});

var form = document.getElementById('pago-form');

form.addEventListener('submit', function(ev) {
ev.preventDefault();

var custName = document.getElementById("custName").value;
var direc = document.getElementById("direc").value;
var direc2 = document.getElementById("direc2").value;
var postal = document.getElementById("postal").value;


  $.ajax({
    type: "POST",
    url: 'http://127.0.0.1:8000/orders/add/',
    data: {
      order_key: clientsecret,
      csrfmiddlewaretoken: CSRF_TOKEN,
      action: "post",
    },
    success: function (json) {
      console.log(json.success)

      stripe.confirmCardPayment(clientsecret, {
        payment_method: {
          card: card,
          billing_details: {
            address:{
                line1:direc,
                line2:direc2
            },
            name: custName
          },
        }
      }).then(function(result) {
        if (result.error) {
          console.log('error')
          console.log(result.error.message);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            console.log('Pago admitido')
            // Puede romper si se cierra la ventana muy pronto
            
            window.location.replace("http://127.0.0.1:8000/pago/orderplaced/");
          }
        }
      });

    },
    error: function (xhr, errmsg, err) {},
  });



});