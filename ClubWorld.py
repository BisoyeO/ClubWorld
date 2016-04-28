'''
Project  
Jourdan Kerl & Bisoye Olaleye
Performer plays music as the crowd dances
'''
import viz
import vizshape
import vizact
from random import randint

viz.setMultiSample(4)#Enable full screen anti-aliasing (FSAA) to smooth edges
viz.go() #starts an empty world 
viz.MainWindow.fov(60)#Increase the Field of View
#viz.MainView.move([0,0,7]) #X,Z,Y
viz.MainView.setPosition([-0,0,-15])
#viz.MainView.setEuler([0,30,0])
piazza = viz.addChild('piazza.osgb') #adds the plazza

sound = viz.addAudio('Panda.mp3') 
sound.loop(viz.ON)
sound.play() 

platform = viz.addChild('platform.osg')
platform.setPosition([0, .2, -11])
micStand = viz.addChild('pole.wrl',parent=platform)
micStand.setPosition([0, 0, .5])
micStand.setScale([0.5,0.36,0.5])
micStand.color(1,1,1)

mic = viz.addChild('pole.wrl')
mic.setPosition([0, 1.6, -10.5])
mic.setScale([0.1,0.04,0.15])
mic.setEuler([0,-45,0])
mic.color(1,0,0)

hat = viz.addChild('tophat.3ds')
performer = viz.addAvatar('vcc_male2.cfg')
performer.setPosition([0, .2, -11])
performer.blend(4,0.5)
performer.blend(5,0.5)

head = performer.getBone('Bip01 Head')
HatLink = viz.link(head,hat)
#Tweek the hat link so it fits snuggly on the head
HatLink.preTrans( [0,0.15,-0.0] )
HatLink.preEuler( [0,-10,0] )

	
for x in [-1,0,1]:
	backupDancer = viz.addAvatar('vcc_female.cfg')
	backupDancer.setPosition([x, .2, -13])
	backupDancer.state(5)
	jump = vizact.move(0,0,1,1)
	turn = vizact.spin(0,1,0,180,1)
	danceMove = vizact.sequence(jump,turn,-1)
	backupDancer.addAction(danceMove)



armBone = performer.getBone('Bip01 R Hand') 
#armBone.lock()
#armBone.setEuler(0, 45, 0)
#viz.link(armBone,mic)



for x in [-3, -1, 1, 3]:
	for z in [4, 2, 0, -2, -4]:
		male = viz.addAvatar('vcc_male.cfg')
		female = viz.addAvatar('vcc_female.cfg')
		male.setPosition([x,0,z])
		female.setPosition([x+1,0,z])
		male.setEuler([180,0,0])
		female.setEuler([180,0,0])
		male.state(randint(3,5))
		female.state(randint(3,5))
		male.setEuler(randint(0,360),0,0)
		female.setEuler(randint(0,360),0,0)



vizshape.addAxes()
viz.collision(viz.ON) #cant navigate off the map
