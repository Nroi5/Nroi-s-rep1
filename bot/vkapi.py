import vk_api

TOKEN="vk1.a.ff5fSV84JjEbnCvsRWgnS-cRvLqZER8J9H40DusGWANNwBH0FkW0vtc_XQm9GeaI_aZxk3V3y_tdKDiEYeu84R5Rkpj-pWc-7Db8ZppeJUQR3NgDY_j5wqVcW8HpET9Cbq30FPNR3x1omM1WHE9glVoE7lQz3Kur0ms11kHcrmMmJVQgk-k7qjPXU-v03HR6Gk2VFSPzjk3rGoCs05MdMg"


#создали экз класса VKApi
vk= vk_api.VkApi(token = TOKEN)

while True:

    #обработка ошибок
    try:

        message = vk.method(
            "messages.getConversations",
                {   
                    "count"  :  20,
                    'filter' : "unanswered"
                }
            )

        if  message['count'] >= 1:
            user_id= message ['items'][0]['last_message']['from_id'] #id пользователя
            message_id= message ['items'][0]['last_message']['id'] #id сообщения от пользователя
            text_msg =message ['items'][0]['last_message']['text'] # сообщение от пользователя





            print(user_id, message_id, text_msg)

            #приводим строку к нижнему регистру
            if text_msg.lower() == 'арбуз':
                message = vk.method(
                    "messages.send",
                        {
                            "peer_id"  :  user_id,
                            "random_id" : message_id,
                            'message'   : "Сам ты, Наташа"
                        }
                    )
    except vk_api.exceptions.ApiError as e:
        print(e)
        e.try_method()



