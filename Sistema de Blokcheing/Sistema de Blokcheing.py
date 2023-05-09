import os
import webbrowser as wb

reg=open("base.txt", "r",encoding='utf-8')
r=reg.readlines()
reg.close()

def Agli(x):
    y=9
    while y>0:
        links[y]=links[y-1]
        y-=1
    links[0]=x
    sa="";x=0
    while x < 10:
        sa+=str(links[x])+"\n"
        x+=1
    reg=open("base.txt", "w")
    reg.write(sa)
    reg.close()
def chek():
  rcu=list(range(10))
  res=list(range(10));lf=-1;rch=0;cdlk=0
  print("INCONINCIDEBCUA!");x=0
  while x < 10:
    if 0<links[x].count("\\"):
      oj=open(links[x]+"\\dat.txt", "r",encoding='utf-8')
      olis=oj.readlines()
      oj.close()
      res[x]="::".join(olis)
      cdlk+=1
    x+=1
  x=0
  while x < 10:
    rcu[x]=0;y=0
    while y < 10:
      if res[x]==res[y] and x!=y:rcu[x]+=1
      y+=1
    x+=1
  #print("kr:",rcu)
  if rcu[0]+1>cdlk/2 or rcu[1]+1>cdlk/2 or rcu[2]+1>cdlk/2:
    x=0
    while x < 10:
      for y in rcu:
        if rcu[x]>rch:rch=rcu[x];lf=x
      x+=1
  #print("kl:",lf)
  if lf!=-1:
    oj=open(links[lf]+"\\dat.txt", "r",encoding='utf-8')
    olis=oj.readlines()
    oj.close()
    sa="";x=0
    while x < len(olis):
        sa+=str(olis[x])
        x+=1
    reg=open("dat.txt", "w")
    reg.write(sa)
    print(sa)
    reg.close()

links=list(range(10))
ap=list(range(10))
x=0;y=len(r)

mlis=list(range(10))
olis=list(range(10))
x=0;cloop=0
while x < 10:
    links[x]=""
    ap[x]="-0-"
    if x<y:
      links[x]=r[x].replace("\n", "")
    x+=1
com=""
while com!="x":
    print("\n+---------------------------------------+")
    rem=open("dat.txt", "r",encoding='utf-8')
    mlis=rem.readlines()
    for x in mlis:print(x)
    rem.close()
    print("--[(c)Check]--[(l)Link up]--[(x)Exit]")
    if cloop<=0:com=input("Comant>: ")
    if com=="c":
        if cloop<=0:
          print("--[(l)loop]--[(n)no loop]")
          com=input("Comant>: ")
        if com=="l":
          cloop=int(input("Amount >: "))
        i=0
        while i<10:
            ap[i]="-0-"
            if 0<links[i].count("\\"):
              oj=open(links[i]+"\\dat.txt", "r",encoding='utf-8')
              olis=oj.readlines()
              oj.close()
              x=0;print(len(mlis),"><",len(olis))
              if len(mlis)<=len(olis):
                ap[i]="-T-"
                while x < len(mlis):
                    if mlis[x].replace("\n", "")!=olis[x].replace("\n", ""):ap[i]="-F-"
                    else:
                      if len(mlis)<len(olis):
                        oj=open(links[i]+"\\dat.txt", "r",encoding='utf-8')
                        olis=oj.readlines()
                        oj.close()
                        sa="";x=0
                        while x < len(olis):
                            sa+=str(olis[x])
                            x+=1
                        reg=open("dat.txt", "w")
                        reg.write(sa)
                        print(sa)
                        reg.close()
                    #print(mlis[x].replace("\n", ""),"><",olis[x].replace("\n", ""))
                    x+=1
            i+=1
        print(ap);x=0
        while x<10:
          if ap[x]=="-F-":chek()
          x+=1
    if cloop>0:
       com="c"
       cloop-=1
    if com=="l":
        for x in links:print("[.]"+x)
        print("[(a)add new link]--[(n)next]")
        com=input("Comant>: ")
        if com=="a":
          com=input("New link>: ")
          Agli(com)
###



