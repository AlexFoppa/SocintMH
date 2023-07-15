
from app.database.instaTwinDB import clean_tables_instagram, get_all_pubs, get_all_twins, insert_publication, insert_twin
from app.database.personDB import clean_table_person, get_all_persons, get_person_by_name, insert_person
from app.models.person import Person
from app.models.instagramTwin import InstagramFeedPublication, InstagramTwin
from app.extraction.getInstagramData import get_insta_profile, get_insta_id, get_insta_media
from app.process.getSentiment import get_sentiment_polarity
import cgi

form = cgi.FieldStorage()

clean_table_person()
clean_tables_instagram()

#Este método foi mantido no index para facilitar a demonstração nesta versão
#Futuramente, a ideia é criar um arquivo na camada processos. Não sei se manterei o form - se sim, creio que dividiria entre presentation and process (necessário avaliar) 

if 'submit' in form:
    name = form.getvalue('name')
    doc = form.getvalue('doc')
    insta_auth_code = form.getvalue('insta_auth_code')
    history = form.getvalue('history')
    email = form.getvalue('email')

else:
    name = 'Alexandre'
    doc = '123456'
    insta_auth_code = ''
    history = 'sintoma 1 e 2'
    email = 'oi@gmail.com'

person = Person(name=name,doc=doc,email=email,history=history)
personId=insert_person(person)
user_id, access_token = get_insta_id(insta_auth_code)

insta_profile = get_insta_profile(user_id, access_token)   
instaTwin = InstagramTwin(
    personId=personId, 
    instagramId=insta_profile['id'], 
    account_type=insta_profile['account_type'], 
    media_count=insta_profile['media_count'],
    username=insta_profile['username'])
insert_twin(instaTwin)

insta_publication= get_insta_media(access_token)

for pub in insta_publication["data"]:
    feed_publication = InstagramFeedPublication(
        personId=personId,
        instagramId = pub["id"],
        caption = pub["caption"],
        captionSentimentPolarity = get_sentiment_polarity(pub["caption"]),
        media_type = pub["media_type"],
        media_url = pub["media_url"],
        permalink = pub["permalink"],
        timestamp = pub["timestamp"],
        username = pub["username"]
        )
    insert_publication(feed_publication)
   