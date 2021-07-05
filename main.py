import os
import discord
from keep_alive import keep_alive
client = discord.Client()

letter = {
  'A': '858313597591617536',
  'B': '858313611335565353',
  'C': '858313623054057503',
  'D': '860515821365624892',
  'E': '860517375963168798',
  'F': '860518983476183050',
  'G': '860520607057051698',
  'H': '860522822123388978',
  'I': '860524636487286875',
  'J': '860534925739950089',
  'K': '860532353281032264',
  'L': '860527525854969896',
  'M': '860537043594772490',
  'N': '860528976404545536',
  'O': '860539511243407401',
  'P': '860900822707732540',
  'Q': '860900852457144320',
  'R': '860926910866522112',
  'S': '860909128330903572',
  'T': '860926776473026570',
  'U': '861215490470314035',
  'V': '861215506500157461',
  'W': '861215519830966272',
  'X': '861220514475016202',
  'Y': '860919200913817610',
  'Z': '861233642041769984',
  'Ö': '860912493425459220'
}

navy = 'What the fuck did you just fucking say about me you little bitch Ill have you know I graduated top of my class in the Navy Seals and Ive been involved in numerous secret raids on AlQuaeda and I have over threehundred confirmed kills I am trained in gorilla warfare and Im the top sniper in the entire US armed forces You are nothing to me but just another target I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth mark my fucking words You think you can get away with saying that shit to me over the Internet Think again fucker As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm maggot The storm that wipes out the pathetic little thing you call your life Youre fucking dead kid I can be anywhere anytime and I can kill you in over seven hundred ways and thats just with my bare hands Not only am I extensively trained in unarmed combat but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent you little shit If only you could have known what unholy retribution your little clever comment was about to bring down upon you maybe you would have held your fucking tongue But you couldnt you didnt and now youre paying the price you goddamn idiot I will shit fury all over you and you will drown in it Youre fucking dead kiddo'

shrek = 'Somebody once told me the world is gonna roll me\nI aint the sharpest tool in the shed\nShe was looking kind of dumb with her finger and her thumb\nIn the shape of an L on her forehead\nWell the years start coming and they dont stop coming\nFed to the rules and I hit the ground running\nDidnt make sense not to live for fun\nYour brain gets smart but your head gets dumb\nSo much to do so much to see\nSo whats wrong with taking the back streets\nYoull never know if you dont go\nYoull never shine if you dont glow\nHey now youre an allstar get your game on go play\nHey now youre a rock star get the show on get paid\nAnd all that glitters is gold\nOnly shooting stars break the mold\nIts a cool place and they say it gets colder\nYoure bundled up now wait\n'

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return;
  if message.content.startswith('.sf'):
    if message.content.startswith('.sf-navy'):
      msg = navy
    elif message.content.startswith('.sf-shrek'):
      msg = shrek
    elif message.content.startswith('.sf-fred'):
      msg = "Big time dumb"
    else:
      msg = message.content[4:]
    output = ''
    count = 1
    subcount = 1
    for char in msg:
      key = char.upper()
      if char == " ":
        output += "    "
      elif key == '\n':
        output += '\n'
        await message.channel.send(output)
        output = ''
        subcount = 1
        continue
      elif key not in letter:
        await message.channel.send('You can only use letters you dumbass')
        return;
      elif key == 'Ö':
        output += f'<:__:' + letter[key] + '>'
      else:
        output += f'<:{char}_:' + letter[key] + '>'
      subcount += 1
      count += 1
      if subcount % 83 == 0:
        await message.channel.send(output)
        output = ''
      if count == len(msg) + 1:
        await message.channel.send(output)

keep_alive()
Token = os.environ['Token']
client.run(Token)
