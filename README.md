# E-Store (Django) — E-Commerce with JazzCash Payments

A Django e-commerce store with product catalogue, cart, checkout and **JazzCash** payment integration, plus email-verified user accounts. Preserved for years as a RAR archive inside a projects collection — now extracted into its own repository.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)

## Overview

E-Store is a complete small-shop build: customers browse products by category, manage a cart, and check out; orders and their status updates are stored as models. Payments go through JazzCash (credentials are read from environment variables). A separate `security` app handles signup with email activation tokens, login and logout.

## Key Features

- **Product catalogue** — products with category/subcategory, price and images (`Product` model)
- **Cart & checkout** — session cart, order placement, `Order` / `OrderUpdate` tracking models
- **JazzCash payment flow** — payment view builds the provider request from env-configured credentials in `store/keys.py`
- **Verified accounts** — signup with email activation token (`security` app: TokenGenerator + email link), login/logout
- Contact form messages stored via the `Contact` model

## Tech Stack

Python · Django · SQLite · JazzCash payment gateway · SMTP email activation · Pillow

## Project Structure

```
├── estore/     # Project settings, URLs, WSGI/ASGI
├── store/      # Shop: Product / Order / Contact models, cart, payment (keys.py)
├── security/   # Auth: signup + email activation, login, logout
├── templates/  # Storefront pages
├── static/     # CSS/JS assets
└── manage.py
```

## Getting Started

```bash
git clone https://github.com/datascientist970/estore-django.git
cd estore-django
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

For payments, set `JAZZCASH_MID`, `JAZZCASH_MK`, `JAZZCASH_MP`, `JAZZCASH_SALT` and `JAZZCASH_RETURN_URL` in your environment (see `store/keys.py`). Configure SMTP settings in `estore/settings.py` for account-activation emails.

## Notes

- This project was recovered from the `estore.rar` archive inside the `Web-Development-Django-` collection. Media/product images and the development database are not included in this repository copy.
- **Security note:** earlier archive copies contained hard-coded payment credentials in `store/keys.py`. They have been removed from this repository and replaced with environment variables — if you ever shared that archive, rotate the credentials with JazzCash.

## Author

**Muhammad Dawood** — AI & Data Science Engineer | Full-Stack Developer
GitHub: https://github.com/datascientist970 · LinkedIn: https://www.linkedin.com/in/dawood406/
Mardan, Khyber Pakhtunkhwa, Pakistan
