var registerButton = document.querySelector("#registerButton");
// console.log(registerButton);
registerButton.onclick = function() {
    // window.alert("Good");
    var newUserName = document.querySelector("#registerName").value
    var newUserEmail = document.querySelector("#registerEmail").value
    var newUserPhoneNumber = document.querySelector("#registerNumber").value
    var newUserPassword = document.querySelector("#registerPassword").value

    var bodyStr = "name=" + encodeURIComponent(newUserName);
    bodyStr += "&email=" + encodeURIComponent(newUserEmail);
    bodyStr += "&phoneNumber=" + encodeURIComponent(newUserPhoneNumber);
    bodyStr += "&password=" + encodeURIComponent(newUserPassword);

    fetch("http://localhost:8080/users",{
        // requests parameters:
        method: "POST", 
        body: bodyStr,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        }
    }).then(function (response) {
        // reload the page
        // displayData();
    })
}



var createOrderButton = document.querySelector("#createOrderButton");
createOrderButton.onclick = function () {
    var newOrderAirport = document.querySelector("#airportBox").value
    var newOrderPickUp = document.querySelector("#pickUpBox").value
    var newOrderDropOff = document.querySelector("#dropOffBox").value
    var newOrderBagAmount = document.querySelector("#bagAmountBox").value
    var newOrderComment = document.querySelector("#commentBox").value

    var bodyStr = "airport=" + encodeURIComponent(newOrderAirport);
    bodyStr += "&pickUpDate" + encodeURIComponent(newOrderPickUp);
    bodyStr += "&dropOffDate=" + encodeURIComponent(newOrderDropOff);
    bodyStr += "&bagAmount=" + encodeURIComponent(newOrderBagAmount);
    bodyStr += "&comment=" + encodeURIComponent(newOrderComment);

    fetch("http://localhost:8080/orders",{
        // requests parameters:
        method: "POST", 
        body: bodyStr,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        }
    }).then(function (response) {
        // reload the page
        // displayData();
    })
}


