import os

# JazzCash payment credentials — set these in your environment.
# Never commit real credentials. (Previous hard-coded values were removed
# when this project was split into its own repository; rotate them with
# your payment provider if they were ever shared publicly.)
MID = os.environ.get("JAZZCASH_MID", "")
MK = os.environ.get("JAZZCASH_MK", "")
MP = os.environ.get("JAZZCASH_MP", "")
salt = os.environ.get("JAZZCASH_SALT", "")
return_url = os.environ.get("JAZZCASH_RETURN_URL", "http://127.0.0.1:8000/payment")
