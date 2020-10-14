import time
import myserver.converttojson as tts
from random import randint, choice
import wikipedia
import pyowm
import urllib
import os
import myserver.StrToInt as strtoint
from youtubesearchpython import searchYoutube
import json


def MyMain(text):
    mymainr = text
    mymainr = mymainr.lower()
    print(mymainr)
    if mymainr=="how are you":
        print("I'm very good! How are you?")
        return "I'm very good! How are you?"
        My = False
    elif mymainr=="do you like me":
        print("Sure! Why not?")
        return "Sure! Why not?"
        My = False
    elif(mymainr=="do you like alexa" or mymainr=="do you like Alexa" or mymainr=="do you know alexa" or mymainr=="do you know Alexa" or
         mymainr=="do you like Siri" or mymainr=="do you like siri" or mymainr=="do you know siri" or mymainr=="do you know Siri" or
         mymainr=="do you like google assistant" or mymainr=="do you like Google assistant" or mymainr=="do you know google assistant" or mymainr=="do you know Google assistant"):
         
       return "I pay respect to all of voice assistants. Being an voice assistant is not an easy job."
    elif mymainr=="do you think I'm pretty":
        print("Sure you are!")
        return "Sure you are!"
        My = False
    elif mymainr=="who let the dogs out" or mymainr=="who Let The Dogs Out":
        print("who, who, who, who, who")
        return "who, who, who, who, who"
        My = False
    elif mymainr=="tell me a joke":
        joke = choice(jokelist)
        print(joke)
        return joke
        My = False
    elif mymainr=="am i funny":
        return "Sure you are!"
        My = False
    elif mymainr=="who created you" or mymainr=="who designeed you":
        return "I was designed by MyTja Team."
        My = False
    elif mymainr=="when were you published" or mymainr=="when were you created":
        return "My first software release came out on second of May 2020"
        My = False
    elif mymainr=="how to check for updates":
        return "Reboot me or say check for updates!"
        My = False
    elif mymainr=="what's your favorite drink":
        return "Electricity."
        My = False
    elif mymainr=="version":
        return version
        My = False
    elif mymainr=="what's your favorite food" or mymainr=="what is your favorite food":
        return "I like pizza."
        My = False
    elif mymainr=="what's the time" or mymainr=="what is the time":
       lt = time.localtime()
       lth = lt.tm_hour
       ltm = lt.tm_min
       return "It's " + str(lth) + "and" + str(ltm) + "minutes."
    elif mymainr=="what's the date":
       lt = time.localtime()
       lty = lt.tm_year
       ltmon = lt.tm_mon
       ltday = lt.tm_mday
       ltdayofweek = lt.tm_wday
       print(ltdayofweek)
       th = ""
       if (ltday=="21"):
          th = "twentyfirst"
       elif (ltday=="1"):
          th = "first"
       elif (ltday=="31"):
          th = "thirtyfirst"
       elif (ltday=="22"):
          th = "twentysecond"
       elif (ltday=="2"):
          th = "second"
       elif (ltday=="23"):
          th = "thirtythird"
       elif (ltday=="3"):
          th = "third"
       elif (ltday=="5"):
          th = "fifth"
       elif (ltday=="15"):
          th = "fifteenth"
       elif (ltday=="25"):
          th = "twentyfifth"
       elif (ltday=="30"):
          th = "thirtieth"
       elif (ltday=="20"):
          th = "twentieth"
       else:
          th = str(ltday) + "th"
          
       return ("It's " + daysOfTheWeek[ltdayofweek] + th + "Of" + monthsOfTheYear[ltmon-1] + str(lty))
##    elif mymainr=="set the stopwatch" or mymainr=="set a stopwatch" or mymainr=="stopwatch":
##       StopwatchStartup()
##    elif mymainr=="stop":
##       global playerOnline
##       global stopwatch
##       if (stopwatch==True):
##          stopwatch = False
##          tts.say("Time (in seconds): " + str(stopwatchTime))
##       if (playerOnline==True):
##          player.stop()
##          playerOnline = False
##    elif mymainr=="pause":
##       #global playerOnline
##       if (playerOnline==True):
##          player.pause()
##          playerOnline = False
##    elif mymainr=="continue":
##       #global playerOnline
##       if (playerOnline==False):
##          player.play()
##          playerOnline = True
##    elif mymainr == "pick a number":
##       PickANumberGame(randint(0, 10), 1)
##    elif mymainr=="countdown":
##       Countdown()
    else:
        query = mymainr
        stopwords = ['what','who','is','a','at','is','he', "who's", "what's", "the", "weather", "in", "like", "plus", "minus", "divided by", "times", "+", "-", "are", "play", "set the alarm at", "set alarm at", "set an alarm at", "set stopwatch", "set the timer for", "set", "timer", "for"]
        querywords = query.split() 
        resultwords  = [word for word in querywords if word.lower() in stopwords]
        result = ' '.join(resultwords)
        print(result)
        
        if (result=="what is the weather like in" or result=="what's the weather like in"):
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            print(result)
            observation = owm.weather_at_place(result)
            w = observation.get_weather()
            temperature = w.get_temperature('celsius')
            humidity = w.get_humidity()

            query = str(w)
            weatherstopwords = ["status=clouds,", "status=clear,"]
            weatherquerywords = query.split() 
            weatherresultwords  = [word for word in weatherquerywords if word.lower() in weatherstopwords]
            weather = ' '.join(weatherresultwords)
            finalweather = str(weather[7])+str(weather[8])+str(weather[9])+str(weather[10])+str(weather[11])+str(weather[12])
            print(weather)
            print(result)
            print(temperature)
            print(humidity)
            print(w)
            temp = temperature["temp"]
            print(temp)
            return ("Temperature in " + str(result) + "is" + str(temperature["temp"]) + "degrees celcius. There is a humidity of " + str(humidity) + "percent. It is" + str(finalweather))

##        elif (result=="play" or result=="Play"):
##            query = mymainr
##            swords = ["play"]
##            querywords = query.split()
##            resultwords  = [word for word in querywords if word.lower() not in swords]
##            result = ' '.join(resultwords)
##            print(result)
##            ytlinks = []
##            textToSearch = result
##            search = searchYoutube(textToSearch, offset = 1, mode = "dict", max_results = 1)
##            result = search.result()["search_result"]
##            for video in result:
##               vid = video["link"]
##            video = pafy.new(vid)
##            best = video.getbest()
##            playurl = best.url
##
##            Instance = vlc.Instance()
##            player = Instance.media_player_new()
##            Media = Instance.media_new(playurl)
##            Media.get_mrl()
##            player.set_media(Media)
##            playerOnline = True
##            player.play()
            
               #tts.say("Please be more specific. Maybe tell me an author or something more.")
               
##        elif (result=="set the alarm at" or result=="set alarm at" or result=="set an alarm at"):
##           stopwords = ["o'clock", "oclock", "sharp", "set the alarm at", "set alarm at", "set an alarm at"]
##           resultwords  = [word for word in querywords if word.lower() not in stopwords]
##           result = ' '.join(resultwords)
##           hoursstr = result[0:2]
##           hoursalmostfinal = hoursstr.replace(":", "")
##           minstr = result[2:4]
##           finalresultm = strtoint.StrToInt(minstr)
##           finalresulth = strtoint.StrToInt(hoursalmostfinal)
##           
##           if (len(alarm1) == 0):
##              alarm1.append(finalresulth)
##              alarm1.append(finalresultm)
##           else:
##              if (len(alarm2) == 0):
##                 alarm2.append(finalresulth)
##                 alarm2.append(finalresultm)
##              else:
##                 if (len(alarm3) == 0):
##                    alarm3.append(finalresulth)
##                    alarm3.append(finalresultm)
##                 else:
##                    tts.say("All my alarm capabilities are full.")
##           
##        elif result=="set the timer for" or result=="set a timer for":   # Timer
##           stopwords = ["set the timer for", "set a timer for"]
##           resultwords  = [word for word in querywords if word.lower() not in stopwords]
##           result = ' '.join(resultwords)
##           timestr = result[0:2]
##           timesetstr = result[2:]
##           if timesetstr=="hour" or timesetstr=="hours":
##              if timestr[1] == " ":
##                 timeint = strtoint.StrToInt(timestr[1])
##                 timefinal = timeint * 60 * 60
##                 TimerSetup(timefinal)
##              else:
##                 timeint = strtoint.StrToInt(timestr)
##                 timefinal = timeint * 60 * 60
##                 TimerSetup(timefinal)
##           elif timesetstr=="minute" or timesetstr=="minutes":
##              if timestr[1] == " ":
##                 timeint = strtoint.StrToInt(timestr[1])
##                 timefinal = timeint * 60
##                 TimerSetup(timefinal)
##              else:
##                 timeint = strtoint.StrToInt(timestr)
##                 timefinal = timeint * 60
##                 TimerSetup(timefinal)
##           elif timesetstr=="second" or timesetstr=="seconds":
##              if timestr[1] == " ":
##                 timeint = strtoint.StrToInt(timestr[1])
##                 timefinal = timeint
##                 TimerSetup(timefinal)
##              else:
##                 timeint = strtoint.StrToInt(timestr)
##                 timefinal = timeint
##                 TimerSetup(timefinal)
##           elif timesetstr=="day" or timesetstr=="days":
##              if timestr[1] == " ":
##                 timeint = strtoint.StrToInt(timestr[1])
##                 timefinal = timeint * 24 * 60 * 60
##                 TimerSetup(timefinal)
##              else:
##                 timeint = strtoint.StrToInt(timestr)
##                 timefinal = timeint * 24 * 60 * 60
##                 TimerSetup(timefinal)

        else:
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            print(result)
            
            try:
               summary = wikipedia.summary(result, sentences=1)
               filteredtext = wpfilter1.removeunwanted(summary)
               print(filteredtext)
               final = filteredtext.encode("utf8")
               print(summary)
               return str(final)
            except:
               return "Sorry, but I cannot tell you that, because a bug in my code."
