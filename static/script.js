document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript is connected!");
    // Add event listeners or additional interactive features as needed.
});

// Features template js

document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');
    const toggleBtn = document.getElementById('toggleSidebar');
    
    // Toggle sidebar
    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');
        mainContent.classList.toggle('expanded');
    });

    // Responsive sidebar
    function handleResize() {
        if (window.innerWidth <= 768) {
            sidebar.classList.add('collapsed');
            mainContent.classList.add('expanded');
        } else {
            sidebar.classList.remove('collapsed');
            mainContent.classList.remove('expanded');
        }
    }

    // Initial check and event listener for resize
    handleResize();
    window.addEventListener('resize', handleResize);

    // Add hover effect to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Simulate user session
});

// login script

// Toggle mobile sidebar
const hamburger = document.getElementById('hamburger');
const sidebar = document.getElementById('sidebar');

hamburger.addEventListener('click', () => {
    sidebar.classList.toggle('active');
});

// Close sidebar when clicking outside on mobile
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
        if (!sidebar.contains(e.target) && !hamburger.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    }
});

// Toggle password visibility
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const toggleBtn = document.querySelector('.toggle-password i');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.classList.remove('fa-eye');
        toggleBtn.classList.add('fa-eye-slash');
    } else {
        passwordInput.type = 'password';
        toggleBtn.classList.remove('fa-eye-slash');
        toggleBtn.classList.add('fa-eye');
    }
}

// Form validation and submission
function handleLogin(event) {
    event.preventDefault();
    const form = event.target;
    const username = form.username;
    const password = form.password;
    let isValid = true;

    // Reset previous errors
    document.querySelectorAll('.input-group').forEach(group => {
        group.classList.remove('error');
    });

    // Validate username
    if (username.value.trim().length < 3) {
        username.parentElement.classList.add('error');
        isValid = false;
    }

    // Validate password
    if (password.value.length < 6) {
        password.parentElement.classList.add('error');
        isValid = false;
    }

    if (isValid) {
        const loginBtn = form.querySelector('.login-btn');
        loginBtn.classList.add('loading');

        // Simulate API call
        setTimeout(() => {
            // Replace this with your actual login logic
            console.log('Login successful!');
            loginBtn.classList.remove('loading');
            window.location.href = 'dashboard.html';
        }, 1500);
    }
}

// Input validation on change
document.querySelectorAll('.input-group input').forEach(input => {
    input.addEventListener('input', () => {
        if (input.value.trim().length > 0) {
            input.parentElement.classList.remove('error');
        }
    });
});

// Read js

function loadPatientDetails() {
    document.getElementById("patientId").textContent = patient.patientId;
    document.getElementById("name").textContent = patient.name;
    document.getElementById("age").textContent = patient.age;
    document.getElementById("gender").textContent = patient.gender;
    document.getElementById("phone").textContent = patient.phone;
    document.getElementById("email").textContent = patient.email;
    document.getElementById("diseaseCategory").textContent = patient.diseaseCategory;
    document.getElementById("nature").textContent = patient.nature;
    document.getElementById("address").textContent = patient.address;
}

