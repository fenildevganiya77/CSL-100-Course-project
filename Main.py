import pygame,math,random
pygame.init() #initialise pygame
scr=pygame.display.set_mode((800,600))  #screen creation
pygame.display.set_caption("Learn the Solar System")  #title
icon=pygame.image.load('icon.png')  #icon
pygame.display.set_icon(icon)
#Facts
facts={
    "Mercury":[
            "Closest to the Sun",
            "No moons",
            "Extreme temperature swings",
            "Orbits Sun in 88 days",
            "Surface full of craters"
    ],
    "Venus":[
        "Hottest planet",
        "Thick CO2 atmosphere",
        "Retrograde rotation",
        "Volcano-covered surface",
        "Same size as Earth"
    ],
    "Earth":[
        "Only planet with life",
        "70% water surface",
        "Has 1 Moon",
        "Ozone layer protects life",
        "Perfect oxygen mix"
    ],
    "Mars":[
        "Red planet",
        "Has 2 moons",
        "Home to Olympus Mons",
        "Thin atmosphere",
        "Ancient water traces"
    ],
    "Jupiter":[
        "Largest planet",
        "Has Great Red Spot",
        "Gas giant",
        "Strong magnetic field",
        "79+ moons"
    ],
    "Saturn":[
        "Beautiful rings",
        "Gas giant",
        "62+ moons",
        "Low density",
        "Mostly hydrogen & helium"
    ],
    "Uranus":[
        "Ice giant",
        "Rotates on its side",
        "13 rings",
        "Very cold",
        "Methane makes it blue"
    ],
    "Neptune":[
        "Farthest planet",
        "Strongest winds",
        "Ice giant",
        "Deep blue color",
        "14 moons incl. Triton"
    ]
}
# Planet images
planet_files =[
    ('planets/1.mercury.png', 16),
    ('planets/2.venus.png', 32),
    ('planets/3.earth.png', 32),
    ('planets/4.mars.png', 20),
    ('planets/5.jupiter.png', 50),
    ('planets/6.saturn.png', 40),
    ('planets/7.uranus.png', 32),
    ('planets/8.naptune.png', 32)
]
name={
    'planets/1.mercury.png':"Mercury",
    'planets/2.venus.png':"Venus",
    'planets/3.earth.png':"Earth",
    'planets/4.mars.png':"Mars",
    'planets/5.jupiter.png':"Jupiter",
    'planets/6.saturn.png':"Saturn",
    'planets/7.uranus.png':"Uranus",
    'planets/8.naptune.png':"Neptune"
}
planets=[]
paths=[]
for path,size in planet_files:
    img_o=pygame.image.load(path)
    img=pygame.transform.scale(img_o,(size,size))
    planets.append(img)
    paths.append(path)
sun=pygame.image.load('sun.png')  #sun
sun=pygame.transform.scale(sun,(62,62))
scr.fill((60,60,90))
font=pygame.font.SysFont("Arial",12,bold=True)
font2=pygame.font.SysFont("Arial",25,bold=True)
big=pygame.font.SysFont("Arial",46,bold=True)
def draw_text(surface,text,pos,font=font,color=(255,255,255)):
    surf=font.render(text,True,color)
    surface.blit(surf,pos)
def draw_centered_text(surface,text,center_pos,font=big,color=(255,255,255)):
    surf=font.render(text,True,color)
    r=surf.get_rect(center=center_pos)
    surface.blit(surf,r.topleft)
def main_menu():
    running=True
    while running:
        scr.fill((0,0,20))
        for e in pygame.event.get(): #takes all event
            if e.type==pygame.QUIT:
                running=False  #stops while loop if we click close
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                mx,my=pygame.mouse.get_pos()
                if 350<=mx<=650 and 220<=my<=280:
                    return "start"
                # Quiz button
                if 350<=mx<=650 and 320<=my<=380:
                    return "quiz"
        draw_centered_text(scr,"Learn the Solar System",(400,120),big,(255,240,255))
        #butons
        pygame.draw.rect(scr,(80,80,140),(240,220,300,60),border_radius=10)
        pygame.draw.rect(scr,(80,140,140),(240,320,300,60),border_radius=10)
        draw_centered_text(scr,"Start Learning",(400,250),big,(0,0,0))
        draw_centered_text(scr,"Take Quiz",(400,350),big,(0,0,0))
        mx,my=pygame.mouse.get_pos()
        if 200<=mx<=650 and 220<=my<=280:
            pygame.draw.rect(scr,(120,120,200),(240,220,300,60),width=4,border_radius=10)
        if 200 <=mx<=650 and 320<=my<=380:
            pygame.draw.rect(scr,(120,200,120),(240,320,300,60),width=4,border_radius=10)
        pygame.display.flip()
#------------
#solar system
#------------
def sol_sys():
    selected_plan=None
    running=True
    while running:
        for e in pygame.event.get(): #takes all event
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                mx,my=pygame.mouse.get_pos()
                for i,(x,y,size) in enumerate(planet_pos):
                    if math.hypot(mx-x,my-y)<=size:
                        selected_plan=i
            if e.type==pygame.QUIT:
                running=False  #stops while loop if we click close
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:
                running=False
        zoomed=False
        scr.fill((0,0,20))
        center=(400,300)
        t=pygame.time.get_ticks()/1000  #get current time
        planet_pos=[]
        draw_text(scr,"Press ESC to go back or click on planet to view",(10,570),font)
        for i,planet in enumerate(planets,start=1):  #movement of planets
            mx,my=pygame.mouse.get_pos()
            orb_rad=i*50
            orb_speed=1/i  #speed of planet(slower for outer)
            angle=t*orb_speed
            pygame.draw.circle(scr,(60,60,90),center,orb_rad,1)
            #(x,y) by sine and cosine
            x=center[0]+math.cos(angle)*orb_rad
            y=center[1]+math.sin(angle)*orb_rad

            size=planet_files[i-1][1]
            dist=math.hypot(mx-x,my-y)
            if dist<=size+6:
                index=i-1
                size=int(size*1.4)
                zoomed=True
            planet_pos.append((x,y,size))
            scaled=pygame.transform.scale(planet,(size,size))
            planet_rect=scaled.get_rect(center=(x,y))
            scr.blit(scaled,planet_rect)
        if zoomed==True:
            x,y,_=planet_pos[index]   
            plan_name=name[paths[index]]
            draw_text(scr,plan_name,(x-20,y-28),font)
        scr.blit(sun,(370,270))
        if selected_plan is not None:
            pname=name[paths[selected_plan]]
            #Big planet
            big_img=pygame.transform.scale(planets[selected_plan],(150,150))
            scr.blit(big_img,(80,200))
            #PLANET NAME
            draw_text(scr,pname,(100,160),big)
            #Facts
            fx=facts[pname]
            y_pos=160
            for f in fx:
                draw_text(scr,"- "+f,(450, y_pos),font2)
                y_pos+=25
        pygame.display.flip()
def quiz():
    running=True
    scr.fill((0,0,20))
    que=[]
    for planet,flist in facts.items():
        for f in flist:
            q=f"Which planet: {f}?"
            que.append((q,planet))
    random.shuffle(que)
    que=que[:10]
    q_index=0
    score=0
    fontQ=pygame.font.SysFont("Arial",26,bold=True)
    fontA=pygame.font.SysFont("Arial",22,bold=True)
    def generate_que(index):
        q_text,answer=que[index]
        all_plan=list(facts.keys())
        wrong=[p for p in all_plan if p!=answer]
        random.shuffle(wrong)
        opts=[answer]+wrong[:3]
        random.shuffle(opts)
        rects=[]
        return q_text,answer,opts,rects
    q_text,answer,options,option_rects=generate_que(q_index)
    while running:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                running=False
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:
                running=False
            if e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
                mx,my=pygame.mouse.get_pos()
                # Check button clicks
                for i,rect in enumerate(option_rects):
                    if rect.collidepoint(mx,my):
                        if options[i]==answer:
                            score+=1
                        q_index+=1
                        if q_index>=len(que):
                            return score,len(que)
                        q_text,answer,options,option_rects=generate_que(q_index)
        scr.fill((10,10,30))
        draw_text(scr,f"Q {q_index+1}:{q_text}",(50,80),fontQ)
        option_rects.clear()
        y=200
        for o in options:
            rect=pygame.Rect(100,y,600,50)
            option_rects.append(rect)
            pygame.draw.rect(scr,(80,80,140),rect,border_radius=8)
            draw_text(scr,o,(120,y+10),fontA)
            y+=80
        draw_text(scr,f"Score: {score}",(650,20),fontQ)
        pygame.display.flip()
def show_result(score,total):
    running=True
    while running:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                running=False
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_ESCAPE or e.key==pygame.K_RETURN:
                    running=False
        scr.fill((20,0,40))
        # Big title
        draw_centered_text(scr,"QUIZ COMPLETE!",(400,150),big,(255,230,0))
        # Score text
        text=f"Your Score: {score} / {total}"
        draw_centered_text(scr,text,(400,260),font2,(255,255,255))
        # Message
        if score==total:
            msg="PERFECT! You're a Solar Champion"
        elif score>=total*0.7:
            msg="Great Job! You know your planets!"
        elif score>=total*0.4:
            msg="Not bad, keep learning"
        else:
            msg="Try again! You'll get better!"
        draw_centered_text(scr,msg,(400,330),font2,(200,200,255))
        draw_centered_text(scr,"Press ENTER or ESC to return",(400,430),font,(180,180,180))
        pygame.display.flip()
#main loop
def main():
    while True:
        choice=main_menu()
        if choice=="start":
            sol_sys()
        elif choice=="quiz":
            score,total=quiz()
            show_result(score,total)
        else:
            break
main()