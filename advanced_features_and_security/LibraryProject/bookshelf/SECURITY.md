HTTPS & Security Headers:
- SECURE_SSL_REDIRECT: Forces HTTPS.
- HSTS: 1 year, includes subdomains, preload enabled.
- SESSION_COOKIE_SECURE & CSRF_COOKIE_SECURE: Cookies only over HTTPS.
- X_FRAME_OPTIONS='DENY': Prevent clickjacking.
- SECURE_CONTENT_TYPE_NOSNIFF & SECURE_BROWSER_XSS_FILTER: Prevent XSS/MIME attacks.
