from django.shortcuts import render, redirect  # type:ignore
from .models import Contact, Product, OrderUpdate, Order
from django.contrib import messages  # type:ignore
from math import ceil
from datetime import datetime, timedelta

import hmac
import hashlib
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Merchant key for secure transactions
MID=""  #merchant id
MP=''   #merchant password
salt='' # integrity salty
return_url=''   #return url


# Home view
def home(request):
    products = []
    catproduct = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catproduct}

    for category in categories:
        prod = Product.objects.filter(category=category)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        products.append([prod, range(1, nSlides + 1), nSlides])

    params = {'products': products}
    return render(request, "index.html", params)


# Contact view
def contact(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("msg")
        query = Contact(name=Name, email=email, desc=msg)
        query.save()
        messages.success(request, "Your Query is Recorded. Thank you for your patience. We will respond ASAP.")
        return render(request, "contact.html")
    return render(request, "contact.html")


# About view
def about(request):
    return render(request, "about.html")



def cart(request):
    
    if request.method == "POST":
        # Collect form data
        json_data = request.POST.get("json", "")
        amt = request.POST.get("amt", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        add = request.POST.get("address", "")
        street = request.POST.get("street", "")
        city = request.POST.get("city", "")
        reg = request.POST.get("region", "")
        zip_code = request.POST.get("zip", "")
        country = request.POST.get("country", "")
        
        # Save order details to the database
        order = Orders(
            json=json_data,
            amt=amt,
            name=name,
            email=email,
            add=add,
            street=street,
            city=city,
            reg=reg,
            zip=zip_code,
            country=country,
        )
        order.save()

        # Save order update
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been placed.")
        update.save()

        # Generate transaction details
        thank = True
        time = datetime.now()
        txn_date = time.strftime("%Y%m%d%H%M%S")
        expiry = (time + timedelta(hours=24)).strftime("%Y%m%d%H%M%S")
        ref_no = f"T{txn_date}" if request.user.is_authenticated else f"T{txn_date}"
        
        # Prepare data for payment gateway
        post_data = {
            "pp_Version": "1.1",
            "pp_TxnType": "",
            "pp_Language": "EN",
            "pp_MerchantID": MID,
            "pp_SubMerchantID": "",
            "pp_Password": MP,
            "pp_BankID": "TBANK",
            "pp_ProductID": "RETL",
            "pp_TxnRefNo": ref_no,
            "pp_Amount": amt,
            "pp_TxnCurrency": "PKR",
            "pp_TxnDateTime": txn_date,
            "pp_BillReference": "billref",
            "pp_Description": "Description of transaction",
            "pp_TxnExpiryDateTime": expiry,
            "pp_ReturnURL": return_url,
            "pp_SecureHash": "",
            "ppmpf_1": "1",
            "ppmpf_2": "2",
            "ppmpf_3": "3",
            "ppmpf_4": "4",
            "ppmpf_5": "5",
        }

        # Generate secure hash
        sorted_data = "&".join(f"{key}={value}" for key, value in sorted(post_data.items()) if value)
        secure_hash = hmac.new(
            salt.encode(),
            sorted_data.encode(),
            hashlib.sha256
        ).hexdigest().upper()
        post_data['pp_SecureHash'] = secure_hash
        print("Sorted Data for Secure Hash:", sorted_data)
        print("Generated Secure Hash:", secure_hash)

        # Prepare context for the payment page
        param_dict = {
            "Customer Name": name,
            "Total Price": amt,
            "post_data": post_data,
        }

        return render(request, "payment.html", {"param_dict": param_dict})

    return render(request, "cart.html")

@csrf_exempt
def payment(request):
    # Handle the payment confirmation if needed (for example, after the payment is completed)
    return render(request, "payment.html")
