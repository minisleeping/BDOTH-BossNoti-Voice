import discord
import asyncio
from discord import Game
from discord.ext.commands import Bot
import datetime
import os

datename = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
kttime = [[10,18],[14],[18],[0,14],[10,18],[14],[14]]
kztime = [[14],[18],[0,14],[10,18],[14],[18],[0,10,18]]
time = [[2,40],[6,40],[10,40],[14,40],[18,40],[22,40]]
ktplayer = ''
kzplayer =''
Nightplayer =''
voice = ''
voice_channel = ''

worldbossmsg = ''
client = discord.Client()

@client.event
async def on_ready():
    global counter
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)

@client.event
async def on_message(message):
	global ktplayer
	global kzplayer
	global Nightplayer
	global voice
	global kznext
	global kznextdate
	global ktnext
	global ktnextdate
	global worldbossmsg
	global voice_channel
	now1 = datetime.datetime.now()
	datenow = now1.strftime("%A")
	if message.content == '!playnoti':
		voice_channel = message.author.voice.voice_channel
		aa=await client.send_message(message.channel, 'Set voice_channel = ' + str(voice_channel))
		await asyncio.sleep(3)
		await client.delete_message(aa)
		await client.delete_message(message)
	elif message.content == '!แตกแน่นอน':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('brake.m4a')
		ktplayer.start()
		await asyncio.sleep(10)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!fail':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('fail.mp3')
		ktplayer.start()
		await asyncio.sleep(15)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!nani':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('nani.m4a')
		ktplayer.start()
		await asyncio.sleep(4)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!omea':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('omea.m4a')
		ktplayer.start()
		await asyncio.sleep(5)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!isas':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('isas.m4a')
		ktplayer.start()
		await asyncio.sleep(5)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!999':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('191.m4a')
		ktplayer.start()
		await asyncio.sleep(5)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!555':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('555.m4a')
		ktplayer.start()
		await asyncio.sleep(15)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!tuna90fs':
		await client.delete_message(message)
		voice = await client.join_voice_channel(voice_channel)
		ktplayer = voice.create_ffmpeg_player('TunaBreak.mp3')
		ktplayer.start()
		await asyncio.sleep(23)
		ktplayer.stop()
		await voice.disconnect()
	elif message.content == '!bw':
		embed = discord.Embed()
		embed.set_image(url='https://cdn.discordapp.com/attachments/394466092845760512/454548640279560192/unknown.png')
		if ktnextdate == datenow:
			ktdd = 'Today'
			if int(now1.minute) > 0:
				ktm = 60 - int(now1.minute)
				kth = ktnext - int(now1.hour) - 1
			else:
				kth = ktnext - int(now1.hour)
				ktm = 0
		else:
			ktdd = 'Tomorrow'
			if int(now1.minute) > 0:
				ktm = 60 - int(now1.minute)
				kth = 24 - int(now1.hour) - 1 + ktnext
			else:
				kth = 24 - int(now1.hour) + ktnext
				ktm = 0

		if kznextdate == datenow:
			kzdd = 'Today'
			if int(now1.minute) > 0:
				kzm = 60 - int(now1.minute)
				kzh = kznext - int(now1.hour) - 1
			else:
				kzh = kznext - int(now1.hour)
				kzm = 0
		else:
			kzdd = 'Tomorrow'
			if int(now1.minute) > 0:
				kzm = 60 - int(now1.minute)
				kzh = 24 - int(now1.hour) - 1 + kznext
			else:
				kzh = 24 - int(now1.hour) + kznext
				kzm = 0


		worldbossmsg = await client.send_message(message.channel, 'Kzarka  next ' + str(kznext) + ':01 ' + kzdd + ' (' +str(kzh)+'h'+str(kzm)+'m)'+'\n'+ 'Kutum  next ' + str(ktnext) + ':01 ' + ktdd + ' (' +str(kth)+'h'+str(ktm)+'m)', embed=embed)
		await client.delete_message(message)
	elif message.content == '!dmsg':
		await client.delete_message(worldbossmsg)
		await client.delete_message(message)
	elif message.content == '!chelp':
		await client.delete_message(message)
		await client.send_message(message.channel, '!bw = ดูเวลาบอสเกิด\n!บอสกิล [บอสอะไรบ้าง] [กี่ใบ] [กี่โมง] [เพิ่มเติมจะใส่ไม่ใส่ก็ได้]\n!แตกแน่นอน\n!fail\n!nani\n!omea\n!isas\n!999\n!555')
	st = message.content.split()
	if len(st) == 4:
		com = st[0]
		bs = st[1]
		x = st[2]
		tm = st[3]
		if com == '!บอสกิล':
			await client.delete_message(message)
			await client.send_message(message.channel, '@everyone !วันนี้มีบอสกิล'+bs+' '+x+'ใบ เวลา'+tm+' แนลบาเลนอส-2 ใครว่างก็มาได้น้า')
	elif len(st) == 5:
		com = st[0]
		bs = st[1]
		x = st[2]
		tm = st[3]
		cc = st[4]
		if com == '!บอสกิล':
			await client.delete_message(message)
			await client.send_message(message.channel, '@everyone !วันนี้มีบอสกิล'+bs+' '+x+'ใบ เวลา'+tm+' แนลบาเลนอส-2 '+cc+' ใครว่างก็มาได้น้า')
		

async def my_background_task():
	global ktplayer
	global kzplayer
	global Nightplayer
	global voice
	global kznext
	global kznextdate
	global ktnext
	global ktnextdate
	global voice_channel
	await client.wait_until_ready()
	while not client.is_closed:
		now = datetime.datetime.now()
		date = now.strftime("%A")
		hour = (now.hour)
		mine = (now.minute)
		day = datename.index(date)
		ktalltime = kttime[day]
		kzalltime = kztime[day]
		ktnext = 99
		kznext = 99
		ktnextdate = date
		kznextdate = date
		x = 0
		while x < len(ktalltime):
			if int(hour) < ktalltime[x]:
				ktnext = ktalltime[x]
				x = len(ktalltime)
			else:
				x += 1
		x = 0
		while x < len(kzalltime):
			if int(hour) < kzalltime[x]:
				kznext = kzalltime[x]
				x = len(kzalltime)
			else:
				x += 1


		if ktnext == 99:
			if day+1 < 7:
				ktnextdate = datename[day+1]
				ktnext = kttime[day+1][0]
			else:
				ktnextdate = datename[0]
				ktnext = kttime[0][0]

		if kznext == 99:
			if day+1 < 7:
				kznextdate = datename[day+1]
				kznext = kztime[day+1][0]
			else:
				kznextdate = datename[0]
				kznext = kztime[0][0]


		x = 0
		while x < len(time):
			if int(hour) < time[x][0]:
				nexth = time[x][0]
				nextm = time[x][1]
				x = len(time)
			elif int(hour) == time[x][0] and int(mine) < time[x][1]:
				nexth = time[x][0]
				nextm = time[x][1]
				x = len(time)
			elif x == len(time) - 1:
				nexth = time[0][0]
				nextm = time[0][1]
				x = len(time)
			else:
				x += 1
		startlp = 0
		print('------------------Set New Time----------------------')
		print('Kz next ' + str(kznext) + ' ' + kznextdate)
		print('Kt next ' + str(ktnext) + ' ' + ktnextdate)
		print('market next ' + str(nexth) + ':' + str(nextm))
		print('----------------------------------------------------')
		print('')
		print('')


		if ktnextdate == date:
			ckktm = (ktnext - int(hour))*60 + int(mine)
		else:
			ckktm = (24 - int(hour) + ktnext)*60 +int(mine)
		if kznextdate == date:
			ckkzm = (kznext - int(hour))*60 + int(mine)
		else:
			ckkzm = (24 - int(hour) + kznext)*60 +int(mine)

		if ckkzm < ckktm:
			nextboss = 'kz'
		else:
			nextboss = 'kt'


		while  startlp == 0:
			now = datetime.datetime.now()
			date = now.strftime("%A")
			hour = (now.hour)
			mine = (now.minute)
			day = datename.index(date)
			ktalltime = kttime[day]
			kzalltime = kztime[day]
			await asyncio.sleep(1)

			if nextboss == 'kt':
				if ktnextdate == date:
					if int(mine) > 0:
						showm = 60 - int(mine)
						showh = ktnext - int(hour) - 1
					else:
						showh = ktnext - int(hour)
						showm = 0
				else:
					if int(mine) > 0:
						showm = 60 - int(mine)
						showh = 24 - int(hour) - 1 + ktnext
					else:
						showh = 24 - int(hour) + ktnext
						showm = 0
				if int(showh/24) == 0:
					await client.change_presence(game=discord.Game(name='Kutum at ' + str(ktnext) + ':01(' + str(showh) +'h' + str(showm) +'m)'))
				else:
					await client.change_presence(game=discord.Game(name='Kutum at ' + str(ktnext) + ':01('+str(int(showh/24))+'d' + str(showh - int(showh/24) * 24) +'h' + str(showm) +'m)'))
			else:
				if kznextdate == date:
					if int(mine) > 0:
						showm = 60 - int(mine)
						showh = kznext - int(hour) - 1
					else:
						showh = kznext - int(hour)
						showm = 0
				else:
					if int(mine) > 0:
						showm = 60 - int(mine)
						showh = 24 - int(hour) - 1 + kznext
					else:
						showh = 24 - int(hour) + kznext
						showm = 0
				if int(showh/24) == 0:
					await client.change_presence(game=discord.Game(name='Kzarka at ' + str(kznext) + ':01(' + str(showh) +'h' + str(showm) +'m)'))
				else:
					await client.change_presence(game=discord.Game(name='Kzarka at ' + str(kznext) + ':01('+str(int(showh/24))+'d' + str(showh - int(showh/24) * 24) +'h' + str(showm) +'m)'))


			if datename.index(date)+1 < 7:
				checkmidnight = datename[datename.index(date)+1]
			else:
				checkmidnight = datename[0]
			if ktnextdate == date or (ktnext == 0 and checkmidnight == ktnextdate):
				if (int(hour) == ktnext-1 or int(hour)-24 == ktnext-1) and int(mine) == 30:
					print('Kt next ' + str(ktnext) + ' ' + ktnextdate + ' 30min Noti')
					voice = await client.join_voice_channel(voice_channel)
					ktplayer = voice.create_ffmpeg_player('kt30.m4a')
					ktplayer.start()
					await asyncio.sleep(60)
					ktplayer.stop()
					await voice.disconnect()
					startlp = 1
				elif (int(hour) == ktnext-1 or int(hour)-24 == ktnext-1) and int(mine) == 45:
					print('Kt next ' + str(ktnext) + ' ' + ktnextdate + ' 15min Noti')
					voice = await client.join_voice_channel(voice_channel)
					ktplayer = voice.create_ffmpeg_player('kt15.m4a')
					ktplayer.start()
					await asyncio.sleep(60)
					ktplayer.stop()
					await voice.disconnect()
					startlp = 1
				elif int(hour) == ktnext and int(mine) == 0:
					print('Kt next ' + str(ktnext) + ' ' + ktnextdate + ' Spawn')
					voice = await client.join_voice_channel(voice_channel)
					kzplayer = voice.create_ffmpeg_player('ktb.m4a')
					kzplayer.start()
					await asyncio.sleep(60)
					kzplayer.stop()
					await voice.disconnect()
					startlp = 1
			if kznextdate == date or (kznext == 0 and checkmidnight == kznextdate):
				if (int(hour) == kznext-1 or int(hour)-24 == kznext-1) and int(mine) == 30:
					print('Kz next ' + str(kznext) + ' ' + kznextdate + ' 30min Noti')
					voice = await client.join_voice_channel(voice_channel)
					kzplayer = voice.create_ffmpeg_player('kz30.m4a')
					kzplayer.start()
					await asyncio.sleep(60)
					kzplayer.stop()
					await voice.disconnect()
					startlp = 1
				elif (int(hour) == kznext-1 or int(hour)-24 == kznext-1) and int(mine) == 45:
					print('Kz next ' + str(kznext) + ' ' + kznextdate + ' 15min Noti')
					voice = await client.join_voice_channel(voice_channel)
					kzplayer = voice.create_ffmpeg_player('kz15.m4a')
					kzplayer.start()
					await asyncio.sleep(60)
					kzplayer.stop()
					await voice.disconnect()
					startlp = 1
				elif int(hour) == kznext and int(mine) == 0:
					print('Kz next ' + str(kznext) + ' ' + kznextdate + ' Spawn')
					voice = await client.join_voice_channel(voice_channel)
					kzplayer = voice.create_ffmpeg_player('kzb.m4a')
					kzplayer.start()
					await asyncio.sleep(60)
					kzplayer.stop()
					await voice.disconnect()
					startlp = 1
			if int(hour) == nexth and int(mine) == nextm:
				print('Market Noti' + str(nexth) +':'+str(nextm))
				voice = await client.join_voice_channel(voice_channel)
				Nightplayer = voice.create_ffmpeg_player('market.m4a')
				Nightplayer.start()
				await asyncio.sleep(60)
				Nightplayer.stop()
				await voice.disconnect()
				startlp = 1



client.loop.create_task(my_background_task())
client.run(os.getenv('TOKEN'))
