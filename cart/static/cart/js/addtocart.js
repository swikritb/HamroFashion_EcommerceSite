// Add to cart animation
// Open the cart and display a loader and make a sweet
//animation when someone adds an item to the cart

document.getElementById("addtocart").addEventListener("submit", (event) => {
  event.preventDefault();

  var q = document.getElementById("quantity");
  let quantity = q.innerText;
  let itemId = q.dataset.prodid;

  fetch(addToCartUrl, {
    method: "post",
    body: JSON.stringify({ itemId: itemId, quantity: quantity }),
    headers: {
      "X-CSRFToken": csrfToken,
      "Content-Type": "application/json",
    },
  })
    .then((data) => {
      var u = new URL(data.url);
      if (data.url && u.pathname !== addToCartUrl) {
        var url = new URL(data.url);
        url.search = `?next=${new URL(window.location).pathname}`;
        window.location = url;
      }
      return data.json();
    })
    .then((resp) => {
      step1(resp);
      window.location.href = "/cart/";
    })
    .catch((e) => {
      console.log(e);
    });
});

function step1(resp) {
  document.getElementById("cartcount").innerText = resp["count"];
  document.getElementById("cartcount-mobile").innerText = resp["count"];
}
