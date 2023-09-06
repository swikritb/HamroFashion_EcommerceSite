const bars = document.getElementById("bars");
const svg = document.getElementById("svgsearch");
const information = document.getElementsByClassName("information")[0];
const nav = document.getElementsByTagName("nav")[0];

function showcart() {
  window.location.href = "/cart/";
}

function fillnav(User = "not AnonymousUser") {
  if (User == "AnonymousUser") {
    return null;
  }
  document.getElementById("loader");

  var table = document.getElementById("cart");
  table.childNodes[1].innerHTML = "";
  fetch(curl + "?HTTP_X_REQUESTED_WITH=XMLHttpRequest", {
    method: "GET",
    headers: {
      Accpet: "application/json",
    },
    credentials: "same-origin",
  })
    .then((data) => data.json())
    .then((resp) => {
      [...resp.res].forEach((resObj, index) => {
        var row = table.insertRow(index);
        var cell1 = row.insertCell(0);
        var div = document.createElement("div");
        div.innerHTML = `<a href="${resObj.url}"><img height="100" width="100" src="${resObj.pic}" class="float-l"></a><div class="mx-2"><a href="${resObj.url}"><h6 style="text-decoration: none; color:white">${resObj.name}</h6></a><div>NRS ${resObj.price} /- <br>${resObj.detail}  <br>Qty  <span class="mx-2">${resObj.quantity}</span></div>`;
        var div1 = document.createElement("div");
        div.classList.add("d-flex");
        cell1.appendChild(div);
        var cell2 = row.insertCell(1);
        div1.innerHTML = `<br> NRS ${resObj.price}`;
        cell2.appendChild(div1);
        if (index === 0) {
          var tot = document.getElementById("write-total");
          tot.innerHTML = `
                <h5 style="color:white">
                  TOTAL : NRS ${resp.totalprice} /-
                </h5>`;
        }
      });

      updatecounting(resp);
    });
}

function updatecounting(resp = []) {
  var total = 0;

  resp.res.map((data) => {
    total = total + data.quantity;
  });
  [...document.getElementsByTagName("sup")].forEach((sup) => {
    sup.innerText = total || 0;
  });
}
