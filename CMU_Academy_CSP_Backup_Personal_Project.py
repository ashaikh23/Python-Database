###Aymaan Shaikh
###AP CSP

### As a kid growing up I used to watch Pingu: a claymation children's tv show
### Since the snow season is coming soon I decided to bring back the old classic show

###Body
Oval(200, 250, 140, 200, fill='black')
Oval(200, 250, 100, 160, fill='white')

###Left Arm
Oval(105, 230, 50, 100, fill='black', rotateAngle=50, border=None)

###Left Arm Nails
Polygon(50,260,55,290,60,260,65,290,70,260,75,290,80,260,fill="orange", rotateAngle=32)

###Right Arm
Oval(275, 230, 50, 100, fill='black', rotateAngle=-20, border=None)

###Right Arm Snowcone 
Polygon(290, 240, 310, 280, 330,240,fill='blue',rotateAngle=33)

###Right Arm Icecream
Circle(328, 226, 20, fill=gradient('paleturquoise', 'skyBlue','lightSkyBlue', start='top-left'))

###Right Feet
Polygon(170, 345, 180, 372, 190, 343,rotateAngle=20)

###Left Feet
Polygon(210, 345, 220, 372, 230, 340,rotateAngle=-20)

###Head
Oval(200, 115, 100, 70, fill='black')

###Mouth
Oval(200, 130, 40, 20, fill='tomato')

###Left Eye scelra
Oval(177, 105, 25, 25, fill='white')

###Left Eye pupil
Oval(177, 105, 10, 10, fill='black')

###Right Eye scelra
Oval(223, 105, 25, 25, fill='white')

###Right Eye pupil
Oval(223, 105, 10, 10, fill='black')

###The Sun
Circle(400, 0, 40, fill=gradient('orange','yellow', 'red','yellow', start='top-left'))

###Pingu's Name
Label('Pingu', 200, 250, size=36, fill=gradient('lightCyan','lightSkyBlue','aqua','paleturquoise', start='bottom'), font='arial', bold=True, border='black')

###Bottom Rectangle: The icy ground
Rect(0, 370, 400, 30, fill=gradient('lightCyan','lightSkyBlue','blue', start='top'))

###My Name
Label('Aymaan Shaikh',350,363,bold=True,font='sans')
