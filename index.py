from app.extraction.getFiles import get_all_files
from app.extraction.getInstagramData import get_insta_profile, get_insta_id, get_insta_media
from app.process.getText import get_text
import cgi

form = cgi.FieldStorage()




name = form.getvalue('name')
doc = form.getvalue('doc')
insta_auth_code = form.getvalue('insta_auth_code')
history = form.getvalue('history')

user_id, access_token = get_insta_id(insta_auth_code)
print(user_id)
print(access_token)

get_insta_profile(user_id, access_token)
get_insta_media(user_id, access_token)


