#maymay bot code

#importing directories

import discord
from discord.ext import commands
import os
import asyncpraw
import asyncio
import json
import datetime
from datetime import timedelta


#reddit login credentials

reddit = asyncpraw.Reddit(client_id=os.getenv("id"),
                          client_secret=os.getenv("ab"),
                          username="TheMayMayMakers",
                          password=os.getenv("pass"),
                          user_agent=os.getenv("ef"))

#setting default command

client = commands.Bot(command_prefix="-")

#client.event from here
client.remove_command('help')



@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))



#client.command from here










#omnithicc
@client.command(brief='boah he thicc', )
async def omnithicc(ctx, num=1):





  if int(num) >= 1:
    if ctx.author.id == 617021192011776000:
        for i in range(int(num)):
          await ctx.send(
          "https://cdn.discordapp.com/attachments/749884739703537746/876097954329559050/871698668917502003.png"
      )
    

    else:
      with open("omnithiccpass.txt", "r") as b:
        winningpostid =  b.read().replace('\n', '')
      
      winningpost = await reddit.submission(id = winningpostid)
      passwinner = winningpost.author

      with open("discordreddit.json", "r") as ab:
        checkdiscordid =json.load(ab)
        winnerdiscordid = checkdiscordid[passwinner.name.lower()] 

    
      if ctx.author.id == winnerdiscordid:
          if int(num) == 1:
           for i in range(int(num)):
            await ctx.send(
            "https://cdn.discordapp.com/attachments/749884739703537746/876097954329559050/871698668917502003.png")

          else:
            await ctx.send(f"sorry honey you arent cool enough to send omnithicc {num} times")
      
      else:
        await ctx.send("sorry honey you arent cool enough to use omnithicc :pleading_face:")















  
maymays = ["manwalkingdownreddit", "srgrafo", "100dicksinyourbum", "1blees", "adamwarlock707", "aj7123", "anorangebirb", "anotherformerlurker", "anurag2199", "aupifo", "averagesimpleton", "boredredditor101", "bravecrusader69", "capnchiknnugget", "chungus23", "dahooligan559", "dankbob_memepants_", "danny-devitotrashman", "dcxr", "deathstrokefsociety", "dollon_da_god", "doses_of_happiness", "efficaciousbean", "elch3w", "fantastic_ostrich", "george2110", "glipglopking28", "gravyxnips", "hardikupreti", "hin2u", "i_am_unique6435", "i_am_yugesh", "i_dont_eatbabies", "idea4granted", "idonthaveaname666", "inf1n1tymagic", "jommy69", "josvys", "kharooficus", "legend-l", "listerineafteroral", "litgrizzly", "macroc0sm", "milkychast", "mistermuesli", "morchel03", "nerdfighter_mohammad", "notkhaos", "organic_crystal_meth", "powerfuloperation8", "prestidigitator97", "qvistenn", "registered__", "regularnoodles", "shiteingann", "shrekkinghandsome", "shyguymemes", "skyeisland", "slummycancerweed", "somememeyboye42812", "srgrafo", "system32comics", "teekay_1994", "tropkis", "tutankhhamun", "ultranegaborel", "winkysocks21", "xdec0de", "yeetvegetabales", "yumyumpee", "zdark_knight21","imprettywhack", "prettycooltim", "nonuntitled", "irrbba"]



@client.command(brief='starts crossposting maymay posts to r/maymay_makers', aliases=["crp"])
@commands.is_owner()

async def crosspost(ctx):




  memes = await reddit.subreddit("memes")
  dankmemes = await reddit.subreddit("dankmemes")
  wholesomememes = await reddit.subreddit("wholesomememes")
  shitposting = await reddit.subreddit("shitposting")
  dogelore = await reddit.subreddit("dogelore")
  historymemes = await reddit.subreddit("historymemes")
  gaming = await reddit.subreddit("gaming")
  funny = await reddit.subreddit("funny")
  bikinibottom = await reddit.subreddit("bikinibottomtwitter")

  print("started scanning")
  while(1):
    print("scanning memes")

    async for submission in memes.new(limit = 70):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/memes")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007" ,icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)





    print("scanning wholesomememes")




      
    async for submission in wholesomememes.new(limit = 35):

      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))
                         
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/wholesomememes")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink))    

              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)




    print("scanning dankmemes")




    async for submission in dankmemes.new(limit = 35):

      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))
                           
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/dankmemes")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink))    

              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")
 
              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue
 
    await asyncio.sleep(30)


    print("scanning historymemes")



    async for submission in historymemes.new(limit = 30):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/historymemes")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)




    print("scanning dogelore")




    async for submission in dogelore.new(limit = 5):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/dogelore")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)




    print("scanning shitposting")




    async for submission in shitposting.new(limit = 40):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/shitposting")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)

    print("scanning gaming")

    async for submission in gaming.new(limit = 35):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/gaming")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)



    print("scanning funny")





    async for submission in funny.new(limit = 35):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/funny")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)



    print("scanning bikinibottomtwitter")




    async for submission in bikinibottom.new(limit = 10):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("crosspostlogs.json", "r") as h:
            logs = json.load(h)

            if (submission.id) in logs.values():
              print("post found in crosspost log, going to next post")
              continue
            
            else:

              crossposted = await submission.crosspost(subreddit="maymay_makers", title = (f"{submission.title}, (Post by u/{submission.author})"))            
              print("crossposted")


              crosspost = await reddit.submission(id = crossposted.id)


              em = discord.Embed(title = "crossposted post by {}".format(submission.author), color = discord.Color.blue())
              em.set_image(url = submission.url_overridden_by_dest)

              em.add_field(name = "Subreddit", value = "r/bikinibottomtwitter")

              
              em.add_field(name = f"Original Post ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

              em.add_field(name = f"Crosspost ({crosspost.id})", value = "[link](https://reddit.com{})".format(crosspost.permalink)) 
                 
              em.add_field(name = "Title", value = submission.title)
              em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

              await ctx.send(embed = em)
              await asyncio.sleep(10)

  

              with open("crosspostlogs.json", "r") as h:
                logs = json.load(h)
                logs[crossposted.id] = submission.id
              
              with open("crosspostlogs.json", "w") as h:
                json.dump(logs,h)

                print("written in crosspost log")
              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)


    print("clearing posts")





    with open("crosspostlogs.json", "r") as i:
      logdlt = json.load(i)
    
      for crpid in logdlt:
        originalpost = logdlt[crpid]
        op = await reddit.submission(id = originalpost)
        if op.removed_by_category == "deleted":
          crp = await reddit.submission(id = crpid)
          
          emb = discord.Embed(title = f"Deleted crosspost ({crp.id})")
          emb.add_field(name = "Name", value = crp.title)
          emb.add_field(name = "Reason", value = f"OP deleted post ({originalpost})")

          await ctx.send(embed = emb)
          await crp.delete()



          with open('crosspostlogs.json', 'r') as data_file:
              data = json.load(data_file)

              data.pop(crpid, None)

          with open('crosspostlogs.json', 'w') as data_file:
              data = json.dump(data, data_file)




    print('waiting 15mins to scan')
    await asyncio.sleep(900)
   



@client.command(brief='sends a post url from its id (usable by everyone)', aliases=["gp"])
async def getpost(ctx, url):
  try:
    submission = await reddit.submission(id = url)
    await ctx.send(f"https://reddit.com{submission.permalink}")
    await ctx.send(f"- {submission.url_overridden_by_dest}")

  except:
    em = discord.Embed(title = f"{url} is not a valid post id", color = discord.Color.red())

    em.set_footer(text = "Examples of valid post ids are paq851, pd4ord etc ", icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")
    await ctx.send(embed = em)




@client.command(brief='finds posts suitable to post on instagram', aliases=["hp"])
@commands.is_owner()

async def hotposts(ctx):




  memes = await reddit.subreddit("memes")
  dankmemes = await reddit.subreddit("dankmemes")
  wholesomememes = await reddit.subreddit("wholesomememes")
  shitposting = await reddit.subreddit("shitposting")
  dogelore = await reddit.subreddit("dogelore")
  historymemes = await reddit.subreddit("historymemes")
  gaming = await reddit.subreddit("gaming")
  funny = await reddit.subreddit("funny")
  bikinibottom = await reddit.subreddit("bikinibottomtwitter")



  print("started hot posts scanning")
  while(1):
    print("scanning memes hot")

    async for submission in memes.hot(limit = 20):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/memes")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)

    print("scanning wholesomememes")

      
    async for submission in wholesomememes.hot(limit = 10):

      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/wholesomememes")

                em.add_field(name = "Score", value = submission.score)
                                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              else:
                continue
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)

    print("scanning dankmemes")

    async for submission in dankmemes.hot(limit = 15):

      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/dankmemes")

                em.add_field(name = "Score", value = submission.score)
                                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")
                

                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
             
              else:
                continue
            


        else:
          continue
       
      except:
        continue

    print("scanning historymemes hot")

    async for submission in historymemes.hot(limit = 20):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/historymemes")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)


    print("scanning dogelore hot")

    async for submission in dogelore.hot(limit = 7):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 5000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/dogelore")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)


    print("scanning shitposting hot")

    async for submission in shitposting.hot(limit = 10):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 5000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/shitposting")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)


    print("scanning funny hot")

    async for submission in funny.hot(limit = 15):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/funny")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)



    print("scanning gaming hot")

    async for submission in gaming.hot(limit = 20):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/gaming")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)

    async for submission in bikinibottom.hot(limit = 10):
  
      
      try:
              
        if submission.author.name.lower() in maymays:
          with open("hotpostssent.txt", "r") as h:
        

            if (submission.id) in h.read():
              print("post found in hotposts log, going to next post")
              continue
            
            else:
              if submission.score > 10000:





                em = discord.Embed(title = "Post matching requirements by {}".format(submission.author), color = discord.Color.blue())
                em.set_image(url = submission.url_overridden_by_dest)

                em.add_field(name = "Subreddit", value = "r/bikinibottomtwitter")

                
                em.add_field(name = f"Post link ({submission.id})", value = "[link](https://reddit.com{})".format(submission.permalink))

                em.add_field(name = "Score", value = submission.score)

                  
                em.add_field(name = "Title", value = submission.title)
                em.set_footer(text = "developed by Sept1c#0007",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")


                await ctx.send(embed = em)
                await asyncio.sleep(10)

    

                with open("hotpostssent.txt", "a") as h:
                  h.write(submission.id)
                  h.write(",")
                  print("written id in hot posts log")
              
              
              else:
               continue
              

              
            


        else:
          continue
      
      except:
        continue

    await asyncio.sleep(30)


    print('waiting 1h to scan')
    await asyncio.sleep(3600)
    

@client.command(brief='sends a leaderboard of top voted posts of the day (usable by everyone)', aliases=['hom', 'plb'])

async def postlb(ctx):
  userwait = await ctx.send("<a:omniloading:882163610875469824>")
  with open ("crosspostlogs.json", "r") as k:
    hofpost = json.load(k)
    for postid in hofpost.values():
      submission = await reddit.submission(id = postid)

      date = datetime.datetime.fromtimestamp(submission.created_utc)
      dif = datetime.datetime.utcnow() - date

      if  dif < timedelta(hours = 24):
        with open ("hof.json", "r") as l:
          hofuser = json.load(l)
          hofuser[postid] = submission.score

        with open("hof.json", "w") as l:
          json.dump(hofuser,l)


      else:
        continue

    with open ("hof.json", "r") as m:
      hofwinner = json.load(m)

      with open ("omnithiccpass.txt", "w") as a:
        a.write(max(zip(hofwinner.values(), hofwinner.keys()))[1])


      em = discord.Embed(title = "Top posts of today", color = discord.Color.blue())
      em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/876323153876508702/881781364091932702/maymayicon.png")
      em.set_footer(text = "Note: bot only looks through r/dankmemes, r/memes, r/wholesomememes, r/dogelore, r/gaming, r/funny, r/shitposting, r/historymemes and r/bikinibottomtwitter. If you get a hot post in some other sub, ping memey with your post before he announces.",icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

      for i in range(len(hofwinner)):

        keymax = max(zip(hofwinner.values(), hofwinner.keys()))[1]
        submission = await reddit.submission(id = keymax)

        date = datetime.datetime.fromtimestamp(submission.created_utc)
        dif = datetime.datetime.utcnow() - date
      
        hours, remainder = divmod(dif.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        

        em.add_field(name = "{}) {} with {} upvotes ({})".format(i + 1, submission.author, submission.score, submission.id), value = "[{}](https://reddit.com{}) ({}h {}m old)".format(submission.title, submission.permalink,hours,minutes), inline = False)

        
        hofwinner.pop(keymax, None)


      await ctx.send(embed = em)
      await userwait.delete()

      hofwinner = {}

    with open ("hof.json", "w") as m:
      json.dump(hofwinner, m)



@client.command(brief='lists the servers the bot is in')
@commands.is_owner()

async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in client.guilds))




@client.command(brief = "gives stats of a redditor", aliases=["r"])
async def redditor(ctx, username):


  emb = discord.Embed(title = "Choose stats to show", description = "<:monthly:882273461274284032>: Monthly stats\n<:alltime:882273485303447602>: All time stats", color = discord.Color.blue())
  choose = await ctx.send(embed = emb)
  await choose.add_reaction("<:monthly:882273461274284032>")
  await choose.add_reaction("<:alltime:882273485303447602>")

  monthly = '<:monthly:882273461274284032>'
  alltime = '<:alltime:882273485303447602>'

  valid_reactions = ['<:alltime:882273485303447602>', '<:monthly:882273461274284032>']

  def check(reaction, user):
      return user == ctx.author and str(reaction.emoji) in valid_reactions and reaction.message == choose 
  try:
    reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=check)

   
    if str(reaction.emoji) == alltime:




      try:
        await choose.delete()

        totalsc = 0
        totalsub = 0
        name = await reddit.redditor(username)
        userwait = await ctx.send("<a:omniloading:882163610875469824>")

        async for submission in name.submissions.top(limit = None):
          totalsc = submission.score + totalsc
          totalsub = totalsub + 1
        

        em = discord.Embed(title = "Redditor stats", color = discord.Color.blue(), description = "Here's all time stats for [u/{}](https://reddit.com/u/{})".format(username, username))
        score_with_commas = "{:,}".format(totalsc)
        subs_with_commas = "{:,}".format(totalsub)

        avgvotes = int(float(totalsc/totalsub))
        
        avg_with_commas = "{:,}".format(avgvotes)

        await name.load()
        em.set_thumbnail(url = name.icon_img)

        tempdic = {}

        async for submission in name.submissions.top(limit = 10):
          tempdic[submission.id] = submission.score

        maxscore = max(zip(tempdic.values(), tempdic.keys()))[1]




        em.add_field(name = "Total votes past all time:", value = "`{}`".format(score_with_commas), inline = False )

        em.add_field(name = "Total submissions past all time:",value = "`{}`".format(subs_with_commas), inline = False)

        em.add_field(name = "Average votes", value = " `{}`".format((avg_with_commas)))
        
        em.set_footer(text = "Note: Cant fetch more than 1000 posts due to reddit api, if user has more posts, stats will be not be completely accurate (they will still be mostly accurate though)", icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")
      
        toppost = await reddit.submission(id = maxscore)
        toppost_with_commas = "{:,}".format(toppost.score)

        em.add_field(name = "Top voted submission of all time:", value = "[{}](https://reddit.com{}) which got `{}` upvotes".format(toppost.title, toppost.permalink, toppost_with_commas), inline = False)




        await ctx.send(embed = em)
        await userwait.delete()
      

      except:
        await userwait.delete()
        em = discord.Embed(title = f"u/{name} is either suspended or does not exist", color = discord.Color.red())
        await ctx.send(embed = em)


    elif str(reaction.emoji) == monthly:

      
     
      try:
        await choose.delete()


        totalsc = 0
        totalsub = 0
        name = await reddit.redditor(username)
        userwait = await ctx.send("<a:omniloading:882163610875469824>")
        tempdic = {}


        async for submission in name.submissions.new(limit = None):
          date = datetime.datetime.fromtimestamp(submission.created_utc)
          
          dif = datetime.datetime.utcnow() - date

          tempsubcount = 0

          if dif < timedelta(days = 30):
            totalsc = totalsc + submission.score
            totalsub = totalsub + 1
            tempdic[submission.id] = submission.score
            tempsubcount = tempsubcount + 1


          elif totalsub <5:
            continue
          
          elif totalsub >=5:
            break




        em = discord.Embed(title = "Redditor stats", color = discord.Color.blue(), description = "Here's monthly stats for [u/{}](https://reddit.com/u/{})".format(username, username))
        score_with_commas = "{:,}".format(totalsc)
        subs_with_commas = "{:,}".format(totalsub)
        await name.load()
        em.set_thumbnail(url = name.icon_img)
        em.set_footer(text = "Note: Cant fetch more than 1000 posts due to reddit api, if user has more posts, stats will be inaccurate", icon_url = "https://cdn.discordapp.com/emojis/882157424990122015.gif?v=1")

        avgvotes = int(float(totalsc/totalsub))
        
        avg_with_commas = "{:,}".format(avgvotes)



          


        maxscore = max(zip(tempdic.values(), tempdic.keys()))[1]




        em.add_field(name = "Total votes this month:", value = "`{}`".format(score_with_commas), inline = False )

        em.add_field(name = "Total submissions this month:",value = "`{}`".format(subs_with_commas), inline = False)

        toppost = await reddit.submission(id = maxscore)
        toppost_with_commas = "{:,}".format(toppost.score)

        em.add_field(name = "Average votes", value = " `{}`".format((avg_with_commas)))


        em.add_field(name = "Top voted submission this month:", value = "[{}](https://reddit.com{}) which got `{}` upvotes".format(toppost.title, toppost.permalink, toppost_with_commas), inline = False)




        await ctx.send(embed = em)
        await userwait.delete()
    
   
      except:
        await userwait.delete()
        em = discord.Embed(title = f"u/{name} is either suspended or does not exist", color = discord.Color.red())
        await ctx.send(embed = em)


  except asyncio.TimeoutError:
    await ctx.send("Message timed out")
    await choose.clear_reaction(monthly)
    await choose.clear_reaction(alltime)






@client.command()
async def help(ctx):
  
  em = discord.Embed(title = "omnithicc commands", color = discord.Color.red())

  em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/749884739703537746/876097954329559050/871698668917502003.png")

  em.add_field(name = "-omnithicc", value = "Sends thicc omni :weary:, hall of memes winner automatically gets perms to use this", inline = False)

  em.add_field(name = "-adv, -advertise", value = "Starts advertising maymayaid on reddit (owner only) [runs 24/7]", inline = False )

  em.add_field(name = "-crp, -crosspost", value = "Stars crossposting maymay posts to r/maymay_makers (owner only) [runs 24/7]", inline = False)

  em.add_field(name = "-hp, -hotposts", value = "Finds posts suitable to be posted on instagram (owner only) [runs 24/7]", inline = False)

  em.add_field(name = "-gp, -getpost", value = "Gets post link and post file from id", inline = False)

  em.add_field(name = "-r, -redditor", value = "Shows the upvote stats of specified redditor", inline = False)

  em.add_field(name = "-servers", value = "Shows the servers the bot is in (owner only)", inline = False)

  em.add_field(name = "-hom, -plb, -postlb", value  = "Shows the top posts of the day by maymaymakers", inline = False)

  em.add_field(name = "-help", value = "Shows this embed", inline = False)


  await ctx.send(embed = em)






#errors:
@crosspost.error
async def crosspost_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        em = discord.Embed(title = "This is a dev-only command", color = discord.Color.red())

        await ctx.send(embed = em)



@servers.error
async def servers_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        em = discord.Embed(title = "This is a dev-only command", color = discord.Color.red())

        await ctx.send(embed = em)




@hotposts.error
async def hotposts_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        em = discord.Embed(title = "This is a dev-only command", color = discord.Color.red())

        await ctx.send(embed = em)





#to know all the attributes of a command, do print(vars(<command>))

#running bot with token

client.run(os.getenv("token"))
