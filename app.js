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

// ===========================================================

var createOrderButton = document.querySelector("#createOrderButton");
createOrderButton.onclick = function () {
    var newOrderAirport = document.querySelector("#airportBox").value
    var newOrderPickUp = document.querySelector("#pickUpBox").value
    var newOrderDropOff = document.querySelector("#dropOffBox").value
    var newOrderBagAmount = document.querySelector("#bagAmountBox").value
    var newOrderComment = document.querySelector("#commentBox").value

    var bodyStr = "airport=" + encodeURIComponent(newOrderAirport);
    bodyStr += "&bagAmount=" + encodeURIComponent(newOrderBagAmount);
    bodyStr += "&pickUpDate=" + encodeURIComponent(newOrderPickUp);
    bodyStr += "&dropOffDate=" + encodeURIComponent(newOrderDropOff);
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
        displayData();
    })
}
displayData();


// ===========================================================


function displayData() {
	fetch("http://localhost:8080/orders").then(function (response){
		response.json().then(function(data){
			console.log("data received from the server: ", data);

			var ordersList = document.querySelector("#displayOrders");
			ordersList.innerHTML = " ";
			data.forEach(function (order) {

                var newListItem = document.createElement("li");

				var airportName = document.createElement("div");
				airportName.innerHTML = order.airport;
				newListItem.appendChild(airportName);

				var bagAmountDiv = document.createElement("div");
				bagAmountDiv.innerHTML = order.date;
				newListItem.appendChild(bagAmountDiv);

				var pickUpDiv = document.createElement("div");
				pickUpDiv.innerHTML = order.comment;
                newListItem.appendChild(pickUpDiv);
                
                var dropOffDiv = document.createElement("div");
				pickUpDiv.innerHTML = order.comment;
                newListItem.appendChild(dropOffDiv);
                
                var commentDiv = document.createElement("div");
                commentDiv.innerHTML = order.comment;
                
            var deleteButton = document.createElement("button");
			deleteButton.setAttribute("id", "deleteButton");
			deleteButton.innerHTML = "Delete";
			deleteButton.onclick = function () {
				console.log("delete clicked:", job.id);
				if (confirm("Are you sure you want to delete? "+ order.id + "?" )){
					deleteOneOrder(order.id);
				}
			}

			var editButton = document.createElement("button");
			editButton.setAttribute("id", "editButton");
			editButton.innerHTML = "Modify";
			editButton.onclick = function () {

				var newNameLabel = document.createElement("input");
				var newDateLabel = document.createElement("input");
				var newCommentLabel = document.createElement("input");
				var newStatusLabel = document.createElement("input");

				newNameLabel.setAttribute("id", "editBox1");
				newDateLabel.setAttribute("id", "editBox2");
				newCommentLabel.setAttribute("id", "editBox3");
				newStatusLabel.setAttribute("id", "editBox4");

				newNameLabel.setAttribute("class", "box");
				newDateLabel.setAttribute("class", "box");
				newCommentLabel.setAttribute("class", "box");
				newStatusLabel.setAttribute("class", "box");

				newNameLabel.value = job.name;
				newDateLabel.value = job.date;
				newCommentLabel.value = job.comment;
				newStatusLabel.value = job.status;

				newListItem.appendChild(newNameLabel);
				newListItem.appendChild(newDateLabel);
				newListItem.appendChild(newCommentLabel);
				newListItem.appendChild(newStatusLabel);

				deleteButton.style.display = "none";
				// document.getElementById("mainList").style.display = "none";
				editButton.style.display = "none"
				newListItem.appendChild(saveButton2);
				console.log("edit clicked:", job.id);

				titleHeading.style.display = "none";
				dateDiv.style.display = "none";
				commentDiv.style.display = "none";
				statusDiv.style.display = "none";

			}

			var saveButton2 = document.createElement("button");
			saveButton2.setAttribute("id", "saveButton2");
			saveButton2.innerHTML = "Save";
			saveButton2.onclick = function () {

				var newJobName = document.querySelector("#editBox1").value
				var newJobDate = document.querySelector("#editBox2").value
				var newJobComment = document.querySelector("#editBox3").value
				var newJobStatus = document.querySelector("#editBox4").value
			
				if (newJobName && newJobDate && newJobComment && newJobStatus != "") {
					var bodyStr = "name=" + encodeURIComponent(newJobName);
					bodyStr += "&date=" + encodeURIComponent(newJobDate);
					bodyStr += "&comment=" + encodeURIComponent(newJobComment);
					bodyStr += "&status=" + encodeURIComponent(newJobStatus);
					
					fetch("http://localhost:8080/jobs/" + job.id,{
						// requests parameters:
						method: "PUT", 
						body: bodyStr,
						headers: {
							"Content-Type": "application/x-www-form-urlencoded"
							// make sure to memorize for the test. 
						}
					}).then(function (response) {
						// reload the page
						displayData();
					})
			
				} else {
					window.alert("Please, fill the form completely!");
				}
			}
            
            var deleteButton = document.createElement("button");
			deleteButton.setAttribute("id", "deleteButton");
			deleteButton.innerHTML = "Delete";
			deleteButton.onclick = function () {
				console.log("delete clicked:", order.id);
				if (confirm("Are you sure you want to delete? "+ order.name + "?" )){
					deleteOrder(order.id);
				}
			}

			var editButton = document.createElement("button");
			editButton.setAttribute("id", "editButton");
			editButton.innerHTML = "Edit";
			editButton.onclick = function () {

				var newAirportLabel = document.createElement("input");
				var newDateLabel = document.createElement("input");
				var newCommentLabel = document.createElement("input");
				var newStatusLabel = document.createElement("input");

				newNameLabel.setAttribute("id", "editBox1");
				newDateLabel.setAttribute("id", "editBox2");
				newCommentLabel.setAttribute("id", "editBox3");
				newStatusLabel.setAttribute("id", "editBox4");

				newNameLabel.setAttribute("class", "box");
				newDateLabel.setAttribute("class", "box");
				newCommentLabel.setAttribute("class", "box");
				newStatusLabel.setAttribute("class", "box");

				newNameLabel.value = job.name;
				newDateLabel.value = job.date;
				newCommentLabel.value = job.comment;
				newStatusLabel.value = job.status;

				newListItem.appendChild(newNameLabel);
				newListItem.appendChild(newDateLabel);
				newListItem.appendChild(newCommentLabel);
				newListItem.appendChild(newStatusLabel);

				deleteButton.style.display = "none";
				// document.getElementById("mainList").style.display = "none";
				editButton.style.display = "none"
				newListItem.appendChild(saveButton2);
				console.log("edit clicked:", job.id);

				titleHeading.style.display = "none";
				dateDiv.style.display = "none";
				commentDiv.style.display = "none";
				statusDiv.style.display = "none";

			}

			var saveButton2 = document.createElement("button");
			saveButton2.setAttribute("id", "saveButton2");
			saveButton2.innerHTML = "Save";
			saveButton2.onclick = function () {

				var newJobName = document.querySelector("#editBox1").value
				var newJobDate = document.querySelector("#editBox2").value
				var newJobComment = document.querySelector("#editBox3").value
				var newJobStatus = document.querySelector("#editBox4").value
			
				if (newJobName && newJobDate && newJobComment && newJobStatus != "") {
					var bodyStr = "name=" + encodeURIComponent(newJobName);
					bodyStr += "&date=" + encodeURIComponent(newJobDate);
					bodyStr += "&comment=" + encodeURIComponent(newJobComment);
					bodyStr += "&status=" + encodeURIComponent(newJobStatus);
					
					fetch("http://localhost:8080/jobs/" + job.id,{
						// requests parameters:
						method: "PUT", 
						body: bodyStr,
						headers: {
							"Content-Type": "application/x-www-form-urlencoded"
							// make sure to memorize for the test. 
						}
					}).then(function (response) {
						// reload the page
						displayData();
					})
			
				} else {
					window.alert("Please, fill the form completely!");
				}
			}
            
            newListItem.appendChild(commentDiv);
            newListItem.appendChild(deleteButton);
			newListItem.appendChild(editButton);
            ordersList.appendChild(newListItem);

			});
		});
	});
};



var deleteOrder = function (orderId){
	fetch("http://localhost:8080/orders/" + orderId, {
		method: "DELETE"
	}).then(function(response){
		// reload the page
		displayData();			
	})
	}

// var clearInputs = function () {
// 	document.getElementById('box1').value = '';
// 	document.getElementById('box2').value = '';
// 	document.getElementById('box3').value = '';
// 	document.getElementById('box4').value = '';
// }