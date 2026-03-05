/**
 * EmailJS Form Handler for Excel Hotels & Resorts
 * Works on ALL hosting including GitHub Pages (no backend needed)
 * 
 * SETUP INSTRUCTIONS:
 * 1. Go to https://www.emailjs.com/ and sign up for free
 * 2. Add an Email Service (Gmail, Outlook, etc.) → get your SERVICE_ID
 * 3. Create an Email Template → get your TEMPLATE_ID
 *    Template variables to use: {{fname}}, {{lname}}, {{hotel}},
 *    {{sdate}}, {{edate}}, {{email}}, {{mob}}, {{qdetail}}
 * 4. Go to Account → API Keys → get your PUBLIC_KEY
 * 5. Replace the three values below with your actual IDs
 */

// ─── CONFIG: Replace these with your EmailJS values ──────────────────────────
const EMAILJS_SERVICE_ID = 'YOUR_SERVICE_ID';   // e.g. 'service_abc123'
const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';  // e.g. 'template_xyz456'
const EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY';   // e.g. 'abcDEF123456'
// ─────────────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', function () {
    // Initialize EmailJS
    emailjs.init(EMAILJS_PUBLIC_KEY);

    const form = document.querySelector('.php-email-form');
    if (!form) return;

    const loadingEl = form.querySelector('.loading');
    const errorEl = form.querySelector('.error-message');
    const successEl = form.querySelector('.sent-message');
    const submitBtn = form.querySelector('button[type="submit"]');

    function showLoading() {
        loadingEl.classList.add('d-block');
        errorEl.classList.remove('d-block');
        successEl.classList.remove('d-block');
        if (submitBtn) submitBtn.disabled = true;
    }

    function showSuccess() {
        loadingEl.classList.remove('d-block');
        successEl.classList.add('d-block');
        if (submitBtn) submitBtn.disabled = false;
    }

    function showError(msg) {
        loadingEl.classList.remove('d-block');
        errorEl.textContent = msg;
        errorEl.classList.add('d-block');
        if (submitBtn) submitBtn.disabled = false;
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Basic validation
        const firstName = form.querySelector('#fname').value.trim();
        const lastName = form.querySelector('#lname').value.trim();
        const email = form.querySelector('#email').value.trim();
        const phone = form.querySelector('#mob').value.trim();
        const hotel = form.querySelector('#sel1').value;
        const startDate = form.querySelector('#sdate').value;
        const endDate = form.querySelector('#edate').value;
        const message = form.querySelector('#qdetail').value.trim();

        if (!firstName || !lastName) {
            return showError('Please enter your first and last name.');
        }
        if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            return showError('Please enter a valid email address.');
        }
        if (!phone) {
            return showError('Please enter your contact number.');
        }
        if (!startDate || !endDate) {
            return showError('Please select both start and end dates.');
        }
        if (!message) {
            return showError('Please enter details about your occasion.');
        }

        showLoading();

        // Collect template parameters (match your EmailJS template variable names)
        const templateParams = {
            fname: firstName,
            lname: lastName,
            hotel: hotel,
            sdate: startDate,
            edate: endDate,
            email: email,
            mob: phone,
            qdetail: message,
            to_email: 'resv@excelhotelandresort.com'
        };

        emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, templateParams)
            .then(function () {
                showSuccess();
                form.reset();
            })
            .catch(function (error) {
                console.error('EmailJS error:', error);
                showError('Something went wrong. Please try again or call us at +91 9211301999.');
            });
    });
});
