from userbot import bot, BOTLOG_CHATID, ALIVE_NAME, CMD_LIST
import asyncio
from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (PeerChat, PeerChannel,ChannelParticipantsAdmins, ChatAdminRights,ChatBannedRights, MessageEntityMentionName,MessageMediaPhoto, ChannelParticipantsBots)
from telethon.tl.types import Channel
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import rekcah05
client = javes = bot 
from telethon.tl.functions.messages import GetCommonChatsRequest
JAVES_NNAME = str(ALIVE_NAME) 
from telethon.events import ChatAction

#@bot.on(rekcah05(pattern=f"gban(?: |$)(.*)", allow_sudo=True))
@bot.on(outgoing=True, pattern="^!gban(?: |$)(.*)")
async def startgban(rk): 
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")      
   me = await rk.client.get_me() ; await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to gban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
   if rk.is_private:       
   	user = rk.chat ; reason = rk.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:      
        if user.id == 709723121:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**Error! This Is My Creator How Am i Supposed To Gban him.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import gmute            
        except:
   	     pass
        try:
          await rk.client(BlockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await rk.client.edit_permissions(i, user, view_messages=False)          
                 a += 1
                 await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to gban user!\nGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if gmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already gbanned.**")
   except:
    	pass
   return await rkp.edit(f"`{JAVES_NNAME}:` **Gbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) , Blocked user and added to Gban watch **") 
   
#@bot.on(rekcah05(pattern=f"ungban(?: |$)(.*)", allow_sudo=True))
@bot.on(outgoing=True, pattern="^!ungban(?: |$)(.*)")
async def regressgban(rk):
   lazy = rk ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()
   if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
   else:
    	rkp = await lazy.edit("`processing...`")   
   me = await rk.client.get_me() ; await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to ungban user!**") ; my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id) ; my_username = f"@{me.username}" if me.username else my_mention ; chat = await rk.get_chat() ; a = b = 0
   if rk.is_private:       
   	user = rk.chat ; reason = rk.pattern_match.group(1) ; chat_title = 'PM'  
   else:
   	chat_title = rk.chat.title  
   try:       
    user, reason = await get_user_from_event(rk)  
   except:
      pass
   try:
     if not reason:
       reason = 'Private'
   except:
   	return await rkp.edit(f"`{JAVES_NNAME}:`**Error! Unknown user.**")
   if user:      
        if user.id == 709723121:     
    	             return await rkp.edit(f"`{JAVES_NNAME}:`**Error! cant ungban this user.**")
        try:
          from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
   	     pass
        try:
          await rk.client(UnblockRequest(user))
          block = 'True'
        except:      
           pass
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel) ]                          
        for i in testrk:
            try:
                 await rk.client.edit_permissions(i, user, send_messages=True)          
                 a += 1
                 await rkp.edit(f"`{JAVES_NNAME}:` **Requesting  to ungban user!\nunGbanned {a} chats.....**")
            except:
                 b += 1                     
   else:
       await rkp.edit(f"`{JAVES_NNAME}:` **Reply to a user !! **")        
   try:
     if ungmute(user.id) is False:
            return await rkp.edit(f"`{JAVES_NNAME}:`**Error! User probably already ungbanned.**")
   except:
    	pass
   return await rkp.edit(f"`{JAVES_NNAME}:` **UnGbanned [{user.first_name}](tg://user?id={user.id}) in {a} chat(s) , UnBlocked and removed user from Gban watch **") 
        

   
   
CMD_HELP.update({
    "gban-gmute":
    "!gban <username> / <userid> / <reply to a user>\
\n**Usage**: Globel ban the person in all groups, channels , block in pm , add gban watch (use with solution) \
\n\n!ungban <username> / <userid> / <reply to a user>\
\n**Usage**: unban user from all groups, channels , remove user from gban watch.\
\n\n!gmute <username> / <userid> / <reply to a user>\
\n**Usage**: Globel mute the user  \
\n\n!ungmute <username> / <userid> / <reply to a user>\
\n**Usage**: Remove user form gmute list \
\n\n**All commands support sudo**\
"
})
