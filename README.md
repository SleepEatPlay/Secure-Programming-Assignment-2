# Secure-Programming-Assignment-2
SECR4483-02 Secure Programming Assignment 2 

Name: Ricky Tang Siet Hong

Matric Number: A20EC3008

To initialize the startup:

1. Set up the virtual environment and install dependencies
   ![image](https://github.com/SleepEatPlay/Secure-Programming-Assignment-2/assets/103356958/d56607f7-717e-4252-8ad7-0592b1d14248)

2. Create the database
   ![image](https://github.com/SleepEatPlay/Secure-Programming-Assignment-2/assets/103356958/c92d6c94-cb6e-4e6c-aee1-7ab560dde344)

3. Run the Flask application
   ![image](https://github.com/SleepEatPlay/Secure-Programming-Assignment-2/assets/103356958/67bb761b-a7d8-4a59-9970-8dc0662ae336)

4. Access the application
   ![image](https://github.com/SleepEatPlay/Secure-Programming-Assignment-2/assets/103356958/60d90923-9aab-46b4-a097-6cc1c4a56786)


# Security Measures Implemented
Client-State Manipulation: Inputs are validated and sanitized.

Session Hijacking Attacks: HTTPS is used, and session cookies are marked as secure, HttpOnly, and SameSite.

Spoofing Authentication Cookies Attacks: Strong session IDs are used, and session information is securely stored server-side.

Session Fixation Attacks: Session IDs are regenerated upon login, and old sessions are invalidated upon logout.

# Future Security Considerations
Cross-Site Scripting (XSS): Further enhance input validation and output encoding.

Cross-Site Request Forgery (CSRF): Implement CSRF tokens to protect against CSRF attacks.

Database Security: Continue regular audits and use parameterized queries to prevent SQL injection.

User Authentication: Consider implementing two-factor authentication for added security.

Error Handling: Ensure error messages do not reveal sensitive information.


