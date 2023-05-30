from turtle import *

#we want to paint a house 


                                #step 1 : Draw a Quadrangle !
speed(1000) 
color("black")
width(4);
forward(200) # Bottom
left(90)
forward(400) # Right Side       
left(90)
forward(200) # Top
left(90)
forward(400) # Left Side
                                    # Quadrangle-End ! 


                            #Door !

left(90)
forward(55)
color("black")
width(2.5)
left(90)        
forward(100)
right(90)
forward(90)
right(90)
forward(100)
                           #Door - End ! 

                                                 #Draw - Windows !!!!!!!!!!!!!

                #Windows - Positions - Right !
penup()
goto(200,400)
pendown()
color("black")
forward(50)   
right(90)
                #windows - Start - Right - Side !

color("black")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)
                #Windows - On - Right - Side - 2 !  

right(90)
forward(100)
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)

                        #Windows - Position - Left !
penup()
goto(0,400)                        
pendown()
color("black")
forward(50)

                        #Windows - Start - Left - Side !

left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)

                        #Windows - On - Left - Side - 2 ! 

penup()
goto(0,220)
pendown()
color("black")

left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)

                                #Roof !

penup()
goto(0,400)
pendown()
left(150)
forward(120)
right(60)
forward(200)

penup()
goto(200,400)
pendown()
left(60)
forward(120)

                        # Right Side Of Apartament ! 


penup()
goto(200,0)
pendown()
forward(120)
left(30)
forward(400)


penup()
goto(200,350)
pendown()

right(60)
forward(40)
right(120)
forward(60)
right(60)
forward(40)
right(120)
forward(30)
right(60)
forward(40)
left(60)
forward(30)
left(120)
forward(20)
left(60)
forward(60)


penup()
goto(200,220)
pendown()
left(120)
forward(40)
right(120)
forward(60)
right(60)
forward(40)
right(120)
forward(30)
right(60)
forward(40)
left(60)
forward(30)
left(120)
forward(20)
left(60)
forward(60)
                                #LUKA -------------------------


               #L - Start !
penup()
goto(-50,-50)
pendown()

forward(60)
left(90)
forward(30)
                #L-End !


                #U - Start ! 


penup()
goto(30,-50)
pendown()


right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
                #U - End! 


                #K - Start ! 

penup()
goto(100,-50)
pendown()

right(180)
forward(60)
left(180)
forward(30)
right(140)
forward(40)
               

penup()
goto(100,-50)
pendown()

right(40)
forward(30)
left(140)
forward(40)
                #K - End !



penup()
goto(180,-50)
pendown()
left(200)
forward(65)
left(180)
forward(65)
left(220)
forward(65)

penup()
goto(180,-50)
pendown()

forward(50)
right(110)
forward(35)

exitonclick();