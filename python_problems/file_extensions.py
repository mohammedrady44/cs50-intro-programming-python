ex = input("File name: ").lower().strip()
size = len(ex)
for l in range(0,size):
    if ex[l] == ".":
        break

extenstions = {".gif":"image",".jpg":"image",".txt":"plain",".zip":"application",".jpeg":"image",".png":"image",".pdf":"application"}
for e in extenstions:
    if e == ex[l:size]:
        if e == ".txt":
            print(f"text/{extenstions[e]}")
        else:
            print(f"{extenstions[e]}/{ex[l+1:size]}")
        break
else:
    print("application/octet-stream") #if the loop wasn't breaked    