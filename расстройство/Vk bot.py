import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from re import *

from vk_api import VkUpload
import requests

vk_session = vk_api.VkApi(token='9e9910d7a8894b217dc280d865a71902e5d344ed93fa49a8f079bdec78a1fc1bd675c963dc0455f3a462f')
vk = vk_session.get_api()
from bs4 import BeautifulSoup


def main():
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            #vk.messages.send(user_id=event.user_id, random_id = get_random_id(), message='Привет, ' + vk.users.get(user_id=event.user_id)[0]['first_name'])
            request = event.text
            group_number = 0
            request=request.lower()
            if request=="начать":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                 message='Привет, ' + vk.users.get(user_id=event.user_id)[0]['first_name'])
                pics(event.user_id,'Drizzle')
def pics(user_id,weather):
    upload = VkUpload(vk_session)
    attachments = []
    image = requests.get("https://openweathermap.org/weather-conditions", stream=True)
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find('a',id="Weather-Condition-Codes-2").\
    findAll()  # получить ссылки
    for x in result:
        print(x)
    # photo = upload.photo_messages(photos=image.raw)[0]
    # attachments.append("photo{}_{}".format(photo["owner_id"], photo["id"]))
    # vk.messages.send(
    #     user_id = user_id,
    #     attachment=','.join(attachments),
    #     random_id=get_random_id(),
    #     message = "jdskf")

if __name__ == '__main__':
    main()