from app.database.instaTwinDB import create_table_instagramTwins
from app.database.personDBe import create_table_person, insert_person
from app.models.person import Person
from app.models.instagramTwin import InstagramTwin
from app.extraction.getInstagramData import get_insta_profile, get_insta_id, get_insta_media
import cgi

form = cgi.FieldStorage()

#create_table_instagramTwins()
#create_table_person()

if 'submit' in form:
    name = form.getvalue('name')
    doc = form.getvalue('doc')
    insta_auth_code = form.getvalue('insta_auth_code')
    history = form.getvalue('history')
    email = form.getvalue('email')

    person = Person(name,doc,email, history)
    insert_person(person)

    user_id, access_token = get_insta_id(insta_auth_code)

    print("<p>",user_id,"</p>")
    print("<p>",access_token,"</p>")

    insta_profile = get_insta_profile(user_id, access_token)
    print("<p>",insta_profile,"</p>")
    #instaTwin = InstagramTwin()


#get_insta_media(user_id, access_token)


