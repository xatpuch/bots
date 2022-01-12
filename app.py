from aiogram import Dispatcher, executor
import logging
from handlers import dp
from filters import is_admin, is_phone_number, is_vk_link, not_subscribed, is_instagram_link, is_tiktok_profile

logging.basicConfig(level=logging.INFO)

def get_handled_updates_list(dp: Dispatcher) -> list:
    available_updates = (
        "callback_query_handlers", "chat_member_handlers",
        "edited_channel_post_handlers", "edited_message_handlers",
        "message_handlers"
        )
    return [item.replace("_handlers", "") for item in available_updates
            if len(dp.__getattribute__(item).handlers) > 0]

if __name__ == "__main__":
    dp.bind_filter(is_admin.Is_Admin)
    dp.bind_filter(is_phone_number.Is_Phone_Number)
    dp.bind_filter(is_vk_link.Is_Vk_Link)
    dp.bind_filter(not_subscribed.Not_Subscribed)
    dp.bind_filter(is_instagram_link.Is_Instagram_Link)
    dp.bind_filter(is_tiktok_profile.Is_Tiktok_Profile)
    executor.start_polling(dp, skip_updates=True, allowed_updates=get_handled_updates_list(dp))