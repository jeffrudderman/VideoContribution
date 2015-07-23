import os
import time
import urlparse
import tornado.options

os.environ['COOKIE_SECRET'] = os.environ.get("SECRET_TOKEN", "placeholder")
os.environ['MONGODB_URL'] = os.environ.get("MONGOLAB_URI", "mongodb://localhost:27017/apptrack")
os.environ['DB_NAME'] = urlparse.urlsplit(os.environ['MONGODB_URL']).path.replace("/","")
os.environ['ZIGGEO_TOKEN'] = urlparse.urlsplit(os.environ.get("ZIGGEO_URL", "https://token:privatekey@srvapi.ziggeo.com")).username
os.environ['FILE_PICKER_KEY'] = os.environ.get("FILEPICKER_API_KEY", "placeholder")
os.environ["ADMINS"] = "adminname:adminpassword"



os.environ['BASE_URL'] = "localhost"
os.environ['PATH'] = "/app/bin:/app/vendor/nginx/sbin:/app/vendor/php/bin:/app/vendor/php/sbin:/usr/local/bin:/usr/bin:/bin"
os.environ['TZ'] = "US/Eastern"
os.environ['PROJECT_ROOT'] = os.path.abspath(os.path.join(os.path.dirname(__file__)))

os.environ['SITE_TITLE'] = "The Gift"
os.environ['APPLY_TITLE'] = "Contribute"   
os.environ['STRING_BOTTOM'] = "© 2015 Jeff Rudderman.  All rights reserved."
os.environ['STRING_CONFIRMATION'] = "We will begin reviewing contributions shortly, and we will be in touch if we need anything else."
os.environ["STRING_WELCOME"] = "Thanks for taking the time to contribute!"
os.environ["STRING_INTRO"] = "As a surprise gift for Katie and Jason at their wedding, we are collecting a photo and brief (1 min or less) video from their friends and family to commemorate their marriage. We encourage everyone to participate, even if you are not able to attend the wedding."

global_data = {
    "VIDEOS": [{
        "question": "Why are you interested in the position?",
        "limit": 90,
        "required": True
    }, {
        "question": "What inspires you the most, and why?",
        "limit": 120,
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
        "label": "Who is your video from?",
        "name": "projects",
        "type": "textarea",
        "placeholder": "ex: The Smiths; or Ralph and Susan Smith; or Ralph, Susan, Mark, Kathy and Jessica Smith",
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
