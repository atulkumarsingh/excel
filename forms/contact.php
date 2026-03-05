<?php
/**
 * Quote Form Email Handler
 * Sends form submission to resv@excelhotelandresort.com
 */

// Receiving email address
$receiving_email_address = 'resv@excelhotelandresort.com';

// Validate required fields
$first_name = filter_var(trim($_POST['fname'] ?? ''), FILTER_SANITIZE_STRING);
$last_name  = filter_var(trim($_POST['lname'] ?? ''), FILTER_SANITIZE_STRING);
$hotel      = filter_var(trim($_POST['hotel'] ?? ''), FILTER_SANITIZE_STRING);
$start_date = filter_var(trim($_POST['sdate'] ?? ''), FILTER_SANITIZE_STRING);
$end_date   = filter_var(trim($_POST['edate'] ?? ''), FILTER_SANITIZE_STRING);
$email      = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$phone      = filter_var(trim($_POST['mob'] ?? ''), FILTER_SANITIZE_STRING);
$message    = filter_var(trim($_POST['qdetail'] ?? ''), FILTER_SANITIZE_STRING);

// Basic validation
if (empty($first_name) || empty($last_name) || empty($email) || empty($message)) {
    echo 'Please fill in all required fields.';
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo 'Please enter a valid email address.';
    exit;
}

// Build email subject and body
$subject = "New Quote Request - $hotel";

$email_body  = "New Quote / Booking Request\n";
$email_body .= "============================\n\n";
$email_body .= "Name       : $first_name $last_name\n";
$email_body .= "Email      : $email\n";
$email_body .= "Phone      : $phone\n";
$email_body .= "Hotel      : $hotel\n";
$email_body .= "Check-In   : $start_date\n";
$email_body .= "Check-Out  : $end_date\n\n";
$email_body .= "Message / Occasion Details:\n";
$email_body .= "----------------------------\n";
$email_body .= "$message\n";

// Email headers
$headers  = "From: Website Form <noreply@excelhotelandresort.com>\r\n";
$headers .= "Reply-To: $first_name $last_name <$email>\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// Send email
if (mail($receiving_email_address, $subject, $email_body, $headers)) {
    echo 'OK';
} else {
    echo 'There was an error sending your message. Please try again or contact us directly.';
}
