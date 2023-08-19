from pathlib import Path
import os
import django

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-2wf!^9tjx04nwo#2(5hb3sj$l2x^w(km*r44rqaxo)-%fh7(o='

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'social_django',

    'cart.apps.CartConfig',
    'shop.apps.ShopConfig',
    'orders.apps.OrdersConfig',
    'create_store.apps.CreateStoreConfig',
    'contact.apps.ContactConfig',
    'signup.apps.SignupConfig', 
    'getApiProducts.apps.GetapiproductsConfig', 
    'payments.apps.PaymentsConfig',

    'paypal.standard.ipn',
   

    'bootstrap4',
    'fontawesomefree',
]

ACCOUNT_ACTIVATION_DAYS = 7  # Number of days activation link is valid

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Use console backend for testing
# Configure email settings for production use

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',  

    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication backend

]

LOGIN_URL = '/accounts/login/' 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',  
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [               
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'social_django.context_processors.backends', 
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'reda0606705646',
        'HOST': 'localhost',
        'PORT': '3306',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
}#

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
] 


MEDIA_URL = 'media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CART_SESSION_ID = 'cart'



EMAIL_HOST = 'smtp.gmail.com'  # Replace with the hostname of your email server
EMAIL_HOST_USER = 'redaesskouni@gmail.com'  # Replace with your email address
EMAIL_HOST_PASSWORD = 'svytlnnjlsojpdqc'  # Replace with your email account password
EMAIL_PORT = 587  # Replace with the port number of your email server
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# PAYPAL settings to test
PAYPAL_RECEIVER_EMAIL = 'sb-gh7ge26227814@business.example.com'
PAYPAL_TEST = True


## for Facebook authontication
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'

SOCIAL_AUTH_FACEBOOK_KEY = '593567136277047'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '7aa09b2287e5c666d38eca596a51f5f9'  # App Secret


## for Linkedin authontication
# SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '78qdk6g7pcdrhh'
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET  = 'iHTYGBJGJBoe6muN'
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_liteprofile', 'r_emailaddress']
