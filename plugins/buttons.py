# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Button(object):

      BUTTONS01 = InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="📁 YTS", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜ", switch_inline_query_current_chat="1 ") ],
                                          [ InlineKeyboardButton(text="📁 Anime", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜ", switch_inline_query_current_chat="2 ") ],
                                          [ InlineKeyboardButton(text="📁 1337x", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜ", switch_inline_query_current_chat="3 " ) ],
                                          [ InlineKeyboardButton(text="📁 ThePirateBay", callback_data='00'),
                                            InlineKeyboardButton(text="🔍 ꜱᴇᴀʀᴄʜ", switch_inline_query_current_chat="4 ") ],
                                          [ InlineKeyboardButton(text="❌", callback_data="X0") ] ] )
