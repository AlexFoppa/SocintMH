
from app.database.instaTwinDB import clean_tables_instagram, create_table_instagramTwins, get_all_pubs, get_all_twins, insert_publication, insert_twin
from app.database.personDBe import clean_table_person, create_table_person, get_all_persons, insert_person
from app.models.person import Person
from app.models.instagramTwin import InstagramFeedPublication, InstagramTwin
from app.extraction.getInstagramData import get_insta_profile, get_insta_id, get_insta_media
import cgi

form = cgi.FieldStorage()

clean_table_person()
clean_tables_instagram()

if 'submit' in form:
    name = form.getvalue('name')
    doc = form.getvalue('doc')
    insta_auth_code = form.getvalue('insta_auth_code')
    history = form.getvalue('history')
    email = form.getvalue('email')

else:
    name = 'Alexandre'
    doc = '123456'
    insta_auth_code = 'AQBBPMcbZ2I0Jd-ryiC_6NTvblXWJiYd99_TYMymKdxuIXBQp9EwIJeDM_bR5SRa8Fi_EsVy4yFIeXYUiaIo89Hw274IifjAfhuMJAa62qu8_ifwbAt2kQN73FA5FRi1xq5tbexDsuEkbce2JCpsogMi_bAk301Cpy6YQ7624X_VRxVUvaQib6sBEOOuDuGvMyF86--Iq7ZsIB81y5Jq6FIBYaFkQqP75lCbMOMPyKr8cg'
    history = 'sintoma 1 e 2'
    email = 'oi@gmail.com'


    person = Person(name=name,doc=doc,email=email,history=history)
    personId=insert_person(person)

    print('---------------------------------------------')
    print(get_all_persons())
    print('---------------------------------------------')

    #user_id, access_token = get_insta_id(insta_auth_code)

    user_id = 7225088037518267
    access_token = "IGQVJWQzkxWDYzMVp2c0wzci1tOWlYTzZAja0RSWjgtVUt2ajBkVFVDbVhYR3BxWEdoUENOQWFIdVFkOHBYZADdfa3otSndGLS1xbjlGTHRXdmozUUgwU3Q2WEVXZAUV5QXZAUR3NaMUluLUNZAZAHBMbThiRVVEeFkzblRSV29z"
  
    print('---------------------------------------------')
    print('Person ID:',personId)
    print('User ID:',user_id)
    print('Access Token:',access_token)
    print('---------------------------------------------')

    insta_profile = get_insta_profile(user_id, access_token)   
    instaTwin = InstagramTwin(
        personId=personId, 
        instagramId=insta_profile['id'], 
        account_type=insta_profile['account_type'], 
        media_count=insta_profile['media_count'],
        username=insta_profile['username'])
    insert_twin(instaTwin)

    print('---------------------------------------------')
    print(get_all_twins())
    print('---------------------------------------------')

    insta_media = get_insta_media(access_token)

    for pub in insta_media["data"]:
        feed_publication = InstagramFeedPublication(
            personId=personId,
            instagramId = pub["id"],
            caption = pub["caption"],
            media_type = pub["media_type"],
            media_url = pub["media_url"],
            permalink = pub["permalink"],
            timestamp = pub["timestamp"],
            username = pub["username"]
            )
        insert_publication(feed_publication)

    print('---------------------------------------------')     
    print(get_all_pubs())
    print('---------------------------------------------')