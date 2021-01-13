import random, string
import webbrowser

print(">>> DISCORD NITRO CODE GENERATOR       <<< ")
print(">>> DM Gvth#3340 on Discord for help!! <<< ")
print(">>> I hope you enjoy!                  <<< \n\n\n")

webbrowser.open('https://discord.gg/2VJfFgdwDt')

num=input('Input How Many Codes to Generate: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Generating...")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()
input("\n\nFinished, Press enter to exit. Codes saved in Nitro Codes")
