import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import wiki

TOKEN="vk1.a.ff5fSV84JjEbnCvsRWgnS-cRvLqZER8J9H40DusGWANNwBH0FkW0vtc_XQm9GeaI_aZxk3V3y_tdKDiEYeu84R5Rkpj-pWc-7Db8ZppeJUQR3NgDY_j5wqVcW8HpET9Cbq30FPNR3x1omM1WHE9glVoE7lQz3Kur0ms11kHcrmMmJVQgk-k7qjPXU-v03HR6Gk2VFSPzjk3rGoCs05MdMg"

vk_session = vk_api.VkApi(token = TOKEN)

vk=vk_session.get_api()


# vk.message.send(params="params", id=id, message=text)


longpoll=VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg= event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1,10**10)

        if msg == "привет":
            response = "Ну здравствуй"

        elif msg.startswith('узнай'):
            ask = msg[6:]
            response = wiki.get_info_wiki(ask)[:4000]

        # elif
        

        # else:
        #     response = "За базаром следи, такого понятия не знаем, поприветствуй как полагается. Напиши Поморгите, и узнаешь о чем можешь поинтересоваться."

        vk.messages.send(user_id = user_id, random_id=random_id, message=response)
