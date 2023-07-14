
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
#Futuramente, a ideia é criar um arquivo getInstagramData.py na camada processos. Não sei se manterei o form - se sim, creio que dividiria entre presentation and process (necessário avaliar) 

if 'submit' in form:
    name = form.getvalue('name')
    doc = form.getvalue('doc')
    insta_auth_code = form.getvalue('insta_auth_code')
    history = form.getvalue('history')
    email = form.getvalue('email')

else:
    name = 'Alexandre'
    doc = '123456'
    insta_auth_code = 'AQDUpCKLc9YCzTZ8tTZg30OYWJAjhy9Yc78ioRcnHd5lCRTlIy26-cccUFA7G0xOXpSaP60n_KsCkBy3CUhqElqPEHLkpn7L67QKaOBgfE4RuvW8fsEHH7tHsEdOoMc1yAUy_DAaSPs3h-2YP_Hf0JfmuVPVSurYuLToN8-c2KFmg5s9t5lO4WCpr-RPx9yp08StCxHMs_TJq57aL0Ko55CidwIrpiM6Vo3zfymR1Zo6-A'
    history = 'sintoma 1 e 2'
    email = 'oi@gmail.com'

person = Person(name=name,doc=doc,email=email,history=history)
personId=insert_person(person)

print('-----------------1 - Pessoa cadastrada no BD ----------------------------')
print(get_all_persons())

user_id, access_token = get_insta_id(insta_auth_code)

print('------------------2 - Retorno da API do Instagram ---------------------------')
print('Person ID:',personId)
print('User ID:',user_id)
print('Access Token:',access_token)

insta_profile = get_insta_profile(user_id, access_token)   
instaTwin = InstagramTwin(
    personId=personId, 
    instagramId=insta_profile['id'], 
    account_type=insta_profile['account_type'], 
    media_count=insta_profile['media_count'],
    username=insta_profile['username'])
insert_twin(instaTwin)

print('----------------3 - Digital Twin: Perfil do Instagram no BD -----------------------------')
print(get_all_twins())

insta_publication= get_insta_media(access_token)
print('----------------------4 - Análise de Sentimento das Postagens ----------------------')
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
    print(get_sentiment_polarity(pub["caption"]),": ",pub["caption"])
    insert_publication(feed_publication)

print('--------------------5 - Digital Twin: Publicações do Feed no BD -------------------------')     
print(get_all_pubs())
print('--------------------6 - Consulta aos dados da pessoa -------------------------')     

person = get_person_by_name('Alexandre')[0]
person = Person(id=person[0],name=person[1],doc=person[2],email=person[3],history=person[4])

print('Pede os dados da pessoa sem argumento:', person.get_person_data())
print('Pede os dados da pessoa pedindo pelo Instagram', person.get_person_data('Instagram'))
print('Pede os dados da pessoa pedindo pelo Facebook', person.get_person_data('Facebook'))
print('Pede todos os dados da pessoa',person.get_person_and_twins_data())