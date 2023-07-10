from app.extraction.getFiles import get_all_files
from app.extraction.getInstagramData import get_insta_profile, get_insta_id, get_insta_media
from app.database.database import clean_table, insert_audio, get_all_audio
from app.process.getText import get_text

#Url para conseguir um código atualizado
#https://api.instagram.com/oauth/authorize?client_id=1310982763154267&redirect_uri=https://alexfoppa.github.io/SocintMH/&scope=user_profile,user_media,instagram_graph_user_profile,instagram_graph_user_media&response_type=code

auth_code = 'AQAv8MP0-HJwX7nNU0k3MxqPYEWtX0LKas_DylSA2Vn4rL7tdnLQtE0mNrDrkUgrPQF8dE4N01Tp0H6EC4IEm4JdtM14dYJAJNQLr663nRqiOYK-ycJI2G4QaZJzxYJRgCpMqkPDg6vE8DVRelwST1ZKjPfQfWnzSJmd0iXYLDutFxRl_8w7gr6Yby95z363TXFWzGXYgjPBIL5x6XAPOHpXhcz2R5nWZr9Y4PMHueSJSw'


user_id, access_token = get_insta_id(auth_code)
get_insta_profile(user_id, access_token)
get_insta_media(user_id, access_token)




'''
Teste de extração de informação de áudios

clean_table()

path = "./audios/"

files = get_all_files(path)

for file in files:
    get_text(file)
    insert_audio(file)

allAudios = get_all_audio()
    
print(allAudios)


'''

