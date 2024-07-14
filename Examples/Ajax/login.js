// Function to handle user login
function loginUser() {
    var username = document.getElementById("loginUsername").value;
    var password = document.getElementById("loginPassword").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "login.py", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function() {
        var loginResult = document.getElementById('loginResult');
        if (xhr.status === 200) {
            try {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    localStorage.setItem('loggedInUser', username);
                    loginResult.innerHTML = 'Logged in successfully';
                    loginResult.style.backgroundColor = '#4CAF50'; // Green for success
                    updateLoginStatus(); // Update login status across the site
                } else {
                    loginResult.innerHTML = response.message || 'Login failed';
                    loginResult.style.backgroundColor = '#f44336'; // Red for error
                }
            } catch(e) {
                loginResult.innerHTML = 'Error parsing server response.';
                loginResult.style.backgroundColor = '#f44336';
            }
        } else {
            loginResult.innerHTML = 'Server error or response not understood';
            loginResult.style.backgroundColor = '#f44336'; // Red for server error
        }
    };
    xhr.send(`username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`);
}

// Function to handle user logout

function logoutUser() {
    localStorage.removeItem('loggedInUser');
    updateLoginStatus(); // Update login status across the site
    window.location.href = 'index.html'; // Redirect to home page
}

// Function to update user display and logout button visibility

function updateLoginStatus() {
    const userDisplaySection = document.getElementById('userDisplay');
    const logoutBtn = document.getElementById('logoutButton');
    const loggedInUser = localStorage.getItem('loggedInUser');
    if (loggedInUser) {
        userDisplaySection.innerHTML = `Welcome, ${loggedInUser}`;
        logoutBtn.style.display = 'block'; // Show logout button
    } else {
        userDisplaySection.innerHTML = '';
        logoutBtn.style.display = 'none'; // Hide logout button
    }
}

// Event listener for DOM content loaded to update user display and logout button

document.addEventListener('DOMContentLoaded', (event) => {
    updateLoginStatus();
    const logoutBtn = document.getElementById('logoutButton');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(event) {
            event.preventDefault();
            logoutUser();
        });
    }
});

function updateUserDisplay() {
    const loggedInUser = localStorage.getItem('loggedInUser');
    const userDisplayElements = document.querySelectorAll('.userDisplay');
    userDisplayElements.forEach(el => {
        if (loggedInUser) {
            el.textContent = `Welcome, ${loggedInUser}`;
        } else {
            el.textContent = '';
        }
    });
}

// Call updateUserDisplay on page load:

document.addEventListener('DOMContentLoaded', () => {
    updateUserDisplay();

});

