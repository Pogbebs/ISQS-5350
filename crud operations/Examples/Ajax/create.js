function createUser() {
    var username = document.getElementById("createUsername").value;
    var password = document.getElementById("createPassword").value;
    var resultDiv = document.getElementById("createResult");

    // Construct the POST request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "create.py", true);  // Make sure this URL is correct!
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Define what happens on successful data submission
    xhr.onload = function () {
        if (xhr.status === 200) {
            // Parse and handle response from your Python script here
            // Assuming your Python script returns a JSON response
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                resultDiv.innerHTML = "Account created successfully!";
                resultDiv.style.color = "green";
                // Optionally redirect the user or clear the form here
            } else {
                resultDiv.innerHTML = response.error || "An error occurred.";
                resultDiv.style.color = "red";
            }
        } else {
            resultDiv.innerHTML = "An error occurred while trying to send the request.";
            resultDiv.style.color = "red";
        }
    };

    // Define what happens in case of an error
    xhr.onerror = function () {
        resultDiv.innerHTML = "An error occurred while trying to send the request.";
        resultDiv.style.color = "red";
    };

    // Set up and send the request
    xhr.send("username=" + encodeURIComponent(username) + "&password=" + encodeURIComponent(password));
}

// Ensure you link this JS script in your HTML file
