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
os.environ["STRING_WELCOME"] = """We are creating a SURPRISE wedding gift for Katie and Jason from their friends and family and request your participation.
                                \n It will only take a few minutes to provide a memory that will last a lifetime.  Deadline for your participation: November 8th, 2015."""
os.environ["STRING_INTRO"] = "Let's get started with the basics."

global_data = {
    "VIDEOS": [{
        "question": """ What is the secret to a long, happy marriage?
                       \n Words of Wizdom on marriage and/or life.
                       \n Offer your congratulations and best wishes.""",
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
        "label": "Your Email",
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
        "label": "Upload your photo.",
        "name": "cv",
        "type": "file",
        "placeholder": "Click button to upload photo (JPG, PNG)",
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
