import os
import time
import urlparse
import tornado.options

os.environ['COOKIE_SECRET'] = os.environ.get("SECRET_TOKEN", "placeholder")
os.environ['MONGODB_URL'] = os.environ.get("MONGOLAB_URI", "mongodb://localhost:27017/apptrack")
os.environ['DB_NAME'] = urlparse.urlsplit(os.environ['MONGODB_URL']).path.replace("/","")
os.environ['ZIGGEO_TOKEN'] = urlparse.urlsplit(os.environ.get("ZIGGEO_URL", "https://token:privatekey@srvapi.ziggeo.com")).username
os.environ['FILE_PICKER_KEY'] = os.environ.get("FILEPICKER_API_KEY", "placeholder")
os.environ["ADMINS"] = "jrudderman:admin"



os.environ['BASE_URL'] = "localhost"
os.environ['PATH'] = "/app/bin:/app/vendor/nginx/sbin:/app/vendor/php/bin:/app/vendor/php/sbin:/usr/local/bin:/usr/bin:/bin"
os.environ['TZ'] = "US/Eastern"
os.environ['PROJECT_ROOT'] = os.path.abspath(os.path.join(os.path.dirname(__file__)))

os.environ['SITE_TITLE'] = "Video Contribution"
os.environ['APPLY_TITLE'] = "Wedding Wizdom"
os.environ['STRING_BOTTOM'] = "Developed with love by Jeff Rudderman."
os.environ['STRING_CONFIRMATION'] = "You're all set!  Thank you so much for taking the time."
os.environ["STRING_WELCOME"] = " - You are invited to share your thoughts with Jason and Katie on the secrets to having a long and happy marriage."
os.environ["STRING_INTRO"] = "Let's get started with the basics."

global_data = {
    "VIDEOS": [{
        "question": "The secret to a long, happy marriage. \n Advice for a groom, bride or both. \n General congratulations and best wishes. \n  Words of wisdom on life and/or marriage.",
        "limit": 90,
        "required": True
    }],
    "FIELDS": [{
        "label": "Your Name",
        "name": "name",
        "type": "text",
        "placeholder": "",
        "required": True
    }, {
        "label": "Email",
        "name": "email",
        "type": "text",
        "placeholder": "",
        "required": True
    }, {
        "label": "Contact phone number",
        "name": "location",
        "type": "text",
        "placeholder": "(###) ###-####",
        "required": True
    }, {
        "label": "Relation to Katie or Jason",
        "name": "web",
        "type": "textarea",
        "placeholder": "ex: Friends, Colleagues, Sister, Cousin, Long Lost Buddy, BFF, etc.",
        "required": True
    }, {
        "label": "How would you like to sign your message?",
        "name": "projects",
        "type": "textarea",
        "placeholder": "ex: Ralph and Susan Smith; or Uncle Ralph and Aunt Susan",
        "required": False
    }, {
        "label": "Cover picture, if you'd like to provide one.",
        "name": "cv",
        "type": "file",
        "placeholder": "Your nice photo (JPG, PNG)",
        "required": False
    }]
}


try:
  import settings_local_environ
  if settings_local_environ.global_data :
      global_data = settings_local_environ.global_data
except:
  pass

  
time.tzset()

def get(key):
  return os.environ.get(key.upper())
