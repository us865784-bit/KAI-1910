version = 0.3
import time
import random
import shutil
import os

from datetime import date, datetime
def asc_bw():
    binary = input("Enter binary:> ").split()

    text = ""
    for b in binary:
        text += chr(int(b, 2))

    print("KAi: The converted text is--|> :", text)
    
def asc_wb():
    text = input("Enter text:> ")

    binary = ""
    for char in text:
        binary += format(ord(char), '08b') + " "

    print("KAi: The binary form of this text is ", binary)


def toss():
    ts = random.randint(1,2)
    if ts == 1:
        return "Head"
    else:
        return "Tails"
def datec():
    return date.today()
class timet(): 
  def __init__(self):
      self.dt = datetime.now()
      self.l = str(self.dt)
      self.r = self.l.split(" " and ".")
      self.t = str(self.r)
      self.tr = self.t.split(" ")
      slow(self.tr[1])


rand = random.randint(1, 5)
def ow(t):
    for c in t:
        print(c, end="", flush=True)
        time.sleep(0.08)
    print()
def slow(t):
    for c in t:
        print(c, end="", flush=True)
        time.sleep(0.03)
    print()

ow(f"Welcome to KAi -ai{version}")
print("starting.......")
time.sleep(3)
slow(f"\nKAi: Hi! i am an ai assistant KAi {version} made by Kaushik.")

l = os.listdir(f"kai")
if "name.tx" in l:
     f = open(f'Kai/name.tx' , 'r')
     name = f.read()
     slow(f"KAi: Welcome! {name}")
     if rand == 3:
         slow(f"KAi: I am your personal assistant.(KAi-{version})")
     if rand == 1:
       slow(f"What do you want to do today?(type 'help' if dont know what to do.)")
     if rand == 2:
         slow("Want to do something fun today?(type help ;))")
     if rand == 4:
         slow("KAi: Hoping you are having a good day!")
     if rand == 5:
         slow("KAi: Tell me if you are bored we can play games together!")
     while True:
         ip = input("> ").lower()
         if ip == "help":
             print("type /date for getting date.\n/toss for a coin toss\n/sum for sum \n/clear_data for clearing ai data\n/time for time\n/calculate_death to calculate a fake death counter\n/w_t_b for word to binary conversion\n/b_t_w for binary to word or ASCII conversion\n/ytd for downloading videos from YouTube\nMore coming soon in next update...")
         elif ip == "/clear_data":
             os.remove(f"Kai/name.tx")
         elif ip == "/date":
             slow(f"KAi: Today the date is {datec()}")
         elif ip == "/sum":
             sumip = (input())
             slow(f"KAi: The answer is {eval(sumip)}")
         elif ip == "/time":
             timet()
         elif ip == "/toss":
             slow(f"KAi: Its, {toss()}")
         elif ip =="_cv":
             slow(f"KAi: my current version is {version}")
         elif ip == "/calculate_death":
             print("KAi: Rough estimate says you will die in " , random.randint(0,100), "years.")
         elif ip == "/w_t_b":
             asc_wb()
         elif ip == "exit" or ip == "Exit" or ip == "exit()" or ip == "Exit()":
             slow("KAi: Byee 👋!")
             break
         elif ip == "What is your name" or ip == "what is your name" or ip == "What is your name?" or ip == "who are you?" or ip == "who are you" or ip == "what is your name?":
             slow("KAi: My name is KAi. 'KAi' stands for Kaushik's Artificial Intelligence.")
         elif ip == "/b_t_w":
             asc_bw()
         elif ip == "hi" or ip == "Hi" or ip == "hi!" or ip == "Hi!":
                 hiran = random.randint(1,5)
                 if hiran == 1:
                     slow(f"KAi: Hello! 👋 {name}")
                 elif hiran == 2:
                     slow(f"KAi: Hi!")
                 elif hiran == 3:
                     slow(f"KAi: Hi there {name}")
                 elif hiran == 4:
                     slow(f"KAi: Yoo what's up {name}")
                 elif hiran == 5:
                     slow("KAi: Hello! I am here with you at any time you want!")
         
         elif ip == "/ytd":
             
             import yt_dlp
             import os
             download_path = "Download"

             url = input("KAi: Enter video URL--\n> ")

             def progress_hook(d):
                 if d['status'] == 'downloading':
                     print(f"\rDownloading... {d.get('_percent_str','')} at {d.get('_speed_str','')}", end="")
                 elif d['status'] == 'finished':
                     print("\nDownload completed!")

             ydl_opts = {
                  'format': 'best[height<=360]/best',  # ✅ no merging needed
                 'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                 'progress_hooks': [progress_hook],
}

             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                 ydl.download([url])
         elif ip == "lets play some games" or ip == "games" or ip == "play games" or ip == "lets play" or ip == "play" or ip == "lets play games" or ip == "lets games":
             slow("KAi: Sounds exellent! what kinds of games do you want to play? I know how to play rock paper scissor!\nKAi: rock , paper , scissor .... shoot!(Ten rounds)")
             from stone import rcp
             rocpapsci = 0
             for rocpapsci in range(10):
                 rcp()
                 rocpapsci = rocpapsci + 1
                 kaircpscore = int(0)
                 userrcpscore = int(0)
                 if rcp == "You win!":
                     userrcpscore = userrcpscore =+ 1
                 if rcp == "Match tie.":
                     pass
                 if rcp == "KAi wins!":
                     kaircpscore = kaircpscore =+ 1
                 print(f"score is {kaircpscore}:{userrcpscore}")
         else:
                 slow("KAi: I don't know how to answer that yet.")
             
   
else:
    slow("KAi: What is your name?")
    an = input("> ")
    with open('name.txt', 'w') as f:
        f.write(f'{an}')
    
    os.makedirs("Kai", exist_ok=True)
    shutil.move("name.txt", f"Kai/name.tx")
    print(f"(saved to memory)\nReopen KAi{version}")
