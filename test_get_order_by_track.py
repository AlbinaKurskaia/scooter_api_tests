#Альбина Курская 40 когорта — Финальный проект. Инженер по тестированию плюс#
import sender_stand_request

def test_get_order_info_success_response():
    response = sender_stand_request.post_new_order()
    track_number = response.json()["track"]
    order_response = sender_stand_request.get_order_info(track_number)
    assert order_response.status_code == 200