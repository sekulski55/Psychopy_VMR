#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 25, 2022, at 17:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

#IMPORTANT!!!
#This section is CODE type: BOTH meaning that it doesnt 
#instantly convert to JS
#This is because these functions do not convert the right way
#and need to be manually inputted
#*BE careful when touching these functions*


#TO run the code through entire target file:
#set 1st REACH trials to "1:16"
#set Reach_VMR trials to "17:96"
#set 2dn REACH trials to "97:105"
#set 3rd REACH trials to "106:128"

def cart2pol(x, y):
    '''
    Converts cartesian coordinates to polar coordinates

    Parameters:
    x - x coord 
    y - y coord 

    Returns:
    rho (distance), phi(angle)
    '''
    rho = sqrt(x**2 + y**2)
    phi = np.arctan2(y, x) #becomes Math.atan2(y,x) on JS side
    return(rho, phi)
    
def JustPhi(x,y):
    '''
    Finds just the phi component from cartesian coords
    Parameters:
    x - x coord 
    y - y coord 

    Returns:
    phi(angle)
    '''
    phi = np.arctan2(y, x)
    return(phi)
    

def pol2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    x,y coordinates
    '''
    x = rho * cos(phi)
    y = rho * sin(phi)
    return(x, y)
    
def xcoord2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    only x coordinate
    '''
    x = rho * cos(phi)
    return x
    
def ycoord2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    Only y coordinate
    '''
    y = rho * sin(phi)
    return y


def radians(deg):
    '''
    Converts degrees to radians

    Parameters:
    deg - degree

    Returns:
    result in radians
    '''
    Degree = (deg/180)*3.1415
    return Degree
    
def degree(rad):
    '''
    Converts radians to degrees

    Parameters:
    rad - radians

    Returns:
    result in degrees
    '''
    Rad = (rad/3.1415)*180
    if Rad < 0:
        Rad = 360 + Rad
    return Rad
    


def pol2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    x,y coordinates
    '''
    x = rho * cos(phi)
    y = rho * sin(phi)
    return(x, y)
    
def xcoord2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    only x coordinate
    '''
    x = rho * cos(phi)
    return x
    
def ycoord2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    Only y coordinate
    '''
    y = rho * sin(phi)
    return y


def radians(deg):
    '''
    Converts degrees to radians

    Parameters:
    deg - degree

    Returns:
    result in radians
    '''
    Degree = (deg/180)*3.1415
    return Degree
    
def degree(rad):
    '''
    Converts radians to degrees

    Parameters:
    rad - radians

    Returns:
    result in degrees
    '''
    Rad = (rad/3.1415)*180
    if Rad < 0:
        Rad = 360 + Rad
    return Rad
    


def pol2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    x,y coordinates
    '''
    x = rho * cos(phi)
    y = rho * sin(phi)
    return(x, y)
    
def xcoord2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    only x coordinate
    '''
    x = rho * cos(phi)
    return x
    
def ycoord2cart(rho, phi):
    '''
    Converts polar coordinates to cartesian coordinates

    Parameters:
    rho - length from origin
    phi - angle from unit circle 0

    Returns:
    Only y coordinate
    '''
    y = rho * sin(phi)
    return y


def radians(deg):
    '''
    Converts degrees to radians

    Parameters:
    deg - degree

    Returns:
    result in radians
    '''
    Degree = (deg/180)*3.1415
    return Degree
    
def degree(rad):
    '''
    Converts radians to degrees

    Parameters:
    rad - radians

    Returns:
    result in degrees
    '''
    Rad = (rad/3.1415)*180
    if Rad < 0:
        Rad = 360 + Rad
    return Rad
    




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'VMR_demo_copy1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\sport\\Desktop\\Psychopy_VMR\\Psychopy_VMR\\VMR_Builder_Code_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
Instruct_text = visual.TextStim(win=win, name='Instruct_text',
    text='Move the cursor from the home position to the target that appears\nin a quick fluid movement. Reach directly for the target\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "code_starter"
code_starterClock = core.Clock()
#document.documentElement.style.cursor = 'none';


# Initialize components for Routine "Reach"
ReachClock = core.Clock()
target = visual.ShapeStim(
    win=win, name='target', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=1.0, depth=0.0, interpolate=True)
#Initilize all varibles in begin experiment
Tx = 0; #Varible for phi component of endpoint


Targetxx = 0.250315801; #Positions of targets, need to be initilized here
Targetyy = -0.250315801;

EndPointCursorx = 5; #Final endpoint positions, intilized outside of visible range
EndPointCursory = 5;




Invis_Home = visual.ShapeStim(
    win=win, name='Invis_Home', vertices=180,
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='green',
    opacity=1.0, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Cursor_2 = visual.ShapeStim(
    win=win, name='Cursor_2',
    size=(0.025, 0.025), vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='gray', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
EndpointMarker = visual.ShapeStim(
    win=win, name='EndpointMarker', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "Instr_rotate"
Instr_rotateClock = core.Clock()
Instruct_text_2 = visual.TextStim(win=win, name='Instruct_text_2',
    text='Please continue reaching for the target\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Reach_VMR"
Reach_VMRClock = core.Clock()
target_2 = visual.ShapeStim(
    win=win, name='target_2', vertices=180,
    size=(0.025, 0.025),
    ori=90.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=1.0, depth=0.0, interpolate=True)
#Initilize Global varibles

#Makes mouse invisble
win.mouse_2Visible = False

#Initilize rotated cursor ouside screen bounds
Rx=5
Ry=5

#Rotated cursor's rho and phi
rho2 = 0
phi2 = 0

#Endpoint intilized ouside screen bounds
EndPointCursorxx = 5;
EndPointCursoryy = 5;


Invis_Home_2 = visual.ShapeStim(
    win=win, name='Invis_Home_2', vertices=180,
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=0.5, depth=-2.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
Cursor_mouse = visual.ShapeStim(
    win=win, name='Cursor_mouse', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Cursor_VMR = visual.ShapeStim(
    win=win, name='Cursor_VMR', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
EndpointMarker_2 = visual.ShapeStim(
    win=win, name='EndpointMarker_2', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=0.0, depth=-6.0, interpolate=True)

# Initialize components for Routine "Instr_wash"
Instr_washClock = core.Clock()
Instruct_text_3 = visual.TextStim(win=win, name='Instruct_text_3',
    text='The cursor will now go away, please continue reaching for the target\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Reach"
ReachClock = core.Clock()
target = visual.ShapeStim(
    win=win, name='target', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=1.0, depth=0.0, interpolate=True)
#Initilize all varibles in begin experiment
Tx = 0; #Varible for phi component of endpoint


Targetxx = 0.250315801; #Positions of targets, need to be initilized here
Targetyy = -0.250315801;

EndPointCursorx = 5; #Final endpoint positions, intilized outside of visible range
EndPointCursory = 5;




Invis_Home = visual.ShapeStim(
    win=win, name='Invis_Home', vertices=180,
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='green',
    opacity=1.0, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Cursor_2 = visual.ShapeStim(
    win=win, name='Cursor_2',
    size=(0.025, 0.025), vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='gray', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
EndpointMarker = visual.ShapeStim(
    win=win, name='EndpointMarker', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "Instr_wash_fb"
Instr_wash_fbClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='The cursor will now reappear, please continue reaching for the target\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Reach"
ReachClock = core.Clock()
target = visual.ShapeStim(
    win=win, name='target', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='red',
    opacity=1.0, depth=0.0, interpolate=True)
#Initilize all varibles in begin experiment
Tx = 0; #Varible for phi component of endpoint


Targetxx = 0.250315801; #Positions of targets, need to be initilized here
Targetyy = -0.250315801;

EndPointCursorx = 5; #Final endpoint positions, intilized outside of visible range
EndPointCursory = 5;




Invis_Home = visual.ShapeStim(
    win=win, name='Invis_Home', vertices=180,
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='green',
    opacity=1.0, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
Cursor_2 = visual.ShapeStim(
    win=win, name='Cursor_2',
    size=(0.025, 0.025), vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='gray', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
EndpointMarker = visual.ShapeStim(
    win=win, name='EndpointMarker', vertices=180,
    size=(0.025, 0.025),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='This is the end\n\nThank you for participating! \n\nPress space to end',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstrComponents = [Instruct_text, key_resp]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr"-------
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct_text* updates
    if Instruct_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct_text.frameNStart = frameN  # exact frame index
        Instruct_text.tStart = t  # local t and not account for scr refresh
        Instruct_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct_text, 'tStartRefresh')  # time at next scr refresh
        Instruct_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct_text.started', Instruct_text.tStartRefresh)
thisExp.addData('Instruct_text.stopped', Instruct_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "code_starter"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
code_starterComponents = []
for thisComponent in code_starterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
code_starterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "code_starter"-------
while continueRoutine:
    # get current time
    t = code_starterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=code_starterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in code_starterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "code_starter"-------
for thisComponent in code_starterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "code_starter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Target_file_real.xlsx', selection='1:16'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Reach"-------
    continueRoutine = True
    # update component parameters for each repeat
    target.setPos((Targetxx,Targetyy))
    #Initilize local varibles 
    mouse_2.setVisible(False)
    wait_time = 0 
    wait_time2 = 0
    counter = 0
    Cursor_2.setColor('white')
    
    
    ###########################
    
    #Make sure target, endpint invisible to start
    target.opacity = 0;
    EndpointMarker.opacity =0;
    
    
    #Convert target file to radians
    rad1 = radians(tgt_angle)
    
    #Set the target's x,y position
    Targetxx = xcoord2cart(tgt_distance,rad1)
    Targetyy = ycoord2cart(tgt_distance,rad1)
    
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ReachComponents = [target, Invis_Home, mouse_2, Cursor_2, EndpointMarker]
    for thisComponent in ReachComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ReachClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reach"-------
    while continueRoutine:
        # get current time
        t = ReachClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ReachClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        #Find distance from origin to cursor at every frame
        Dist_from_Home = sqrt(((Cursor_2.pos[0]-Invis_Home.pos[0])**2)+(Cursor_2.pos[1]-Invis_Home.pos[1])**2)
        
        #####################################################
        #Phase 0, using 'counter' to change phases
        #Finding Home phase
        #When cursor within certain distance of home, becomes visible
        #When its within home radius, waits 20 frames then goes to next phase
        
        
        if counter ==0:
            Invis_Home.opacity = 1;
            target.opacity = 0;
            
            if Dist_from_Home > 0.15:
                continueRoutine = True;
                Cursor_2.opacity =0
            if (Dist_from_Home <= 0.15) & (Dist_from_Home > 0.0125):
                continueRoutine = True;
                
                Cursor_2.opacity =1
            if Dist_from_Home < 0.0125:
                wait_time = wait_time+1
            if wait_time > 20: 
                counter=1;
        ##################################################
        #Phase 1
        #REACH Phase
        #Checks target file for online feedback y/n
        #Once cursor crosses 'target ring', goes to next phase
        
        if counter ==1:
            if online_fb == 1:
                Cursor_2.opacity =1;
            if online_fb == 0:
                Cursor_2.opacity=0;
            Invis_Home.opacity = 0.0;
            target.opacity = 1;
        
        
            if Dist_from_Home > 0.354:
                Cursor_2.fillColor = 'gray';
                Cursor_2.opacity=0;
                counter=2
        
        #Phase 2
        #Endpoint phase
        #Checks target file for endpoint y/n
        #Tx calculates the phi of the cursor
        #Tx plugged into the endpointmarker
        #endpoint stays for 20 frames, then routine ends
        
        
        if counter == 2:
            if endpoint_feedback == 1:
                EndpointMarker.opacity =1;
            if endpoint_feedback == 0:
                EndppointMarker.opacity=0;
            #Cursor_2.opacity=1;
                    
            Tx = JustPhi((Cursor_2.pos[0]-Invis_Home.pos[0]),(Cursor_2.pos[1]-Invis_Home.pos[1]))
            wait_time2 = wait_time2+1
                    
            if wait_time2 == 1:
                 EndPointCursorx = xcoord2cart(0.354,Tx);
                 EndPointCursory = ycoord2cart(0.354,Tx);
            if wait_time2 >20:
                continueRoutine = False;
        else:
            continueRoutine = True;
        
        # *Invis_Home* updates
        if Invis_Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Invis_Home.frameNStart = frameN  # exact frame index
            Invis_Home.tStart = t  # local t and not account for scr refresh
            Invis_Home.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Invis_Home, 'tStartRefresh')  # time at next scr refresh
            Invis_Home.setAutoDraw(True)
        
        # *Cursor_2* updates
        if Cursor_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cursor_2.frameNStart = frameN  # exact frame index
            Cursor_2.tStart = t  # local t and not account for scr refresh
            Cursor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cursor_2, 'tStartRefresh')  # time at next scr refresh
            Cursor_2.setAutoDraw(True)
        if Cursor_2.status == STARTED:  # only update if drawing
            Cursor_2.setPos((mouse_2.getPos()[0],mouse_2.getPos()[1]), log=False)
        
        # *EndpointMarker* updates
        if EndpointMarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndpointMarker.frameNStart = frameN  # exact frame index
            EndpointMarker.tStart = t  # local t and not account for scr refresh
            EndpointMarker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndpointMarker, 'tStartRefresh')  # time at next scr refresh
            EndpointMarker.setAutoDraw(True)
        if EndpointMarker.status == STARTED:  # only update if drawing
            EndpointMarker.setPos((EndPointCursorx, EndPointCursory), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReachComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reach"-------
    for thisComponent in ReachComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('target.started', target.tStartRefresh)
    trials.addData('target.stopped', target.tStopRefresh)
    trials.addData('Invis_Home.started', Invis_Home.tStartRefresh)
    trials.addData('Invis_Home.stopped', Invis_Home.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    trials.addData('mouse_2.x', x)
    trials.addData('mouse_2.y', y)
    trials.addData('mouse_2.leftButton', buttons[0])
    trials.addData('mouse_2.midButton', buttons[1])
    trials.addData('mouse_2.rightButton', buttons[2])
    trials.addData('mouse_2.started', mouse_2.tStartRefresh)
    trials.addData('mouse_2.stopped', mouse_2.tStopRefresh)
    trials.addData('Cursor_2.started', Cursor_2.tStartRefresh)
    trials.addData('Cursor_2.stopped', Cursor_2.tStopRefresh)
    trials.addData('EndpointMarker.started', EndpointMarker.tStartRefresh)
    trials.addData('EndpointMarker.stopped', EndpointMarker.tStopRefresh)
    # the Routine "Reach" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "Instr_rotate"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Instr_rotateComponents = [Instruct_text_2, key_resp_2]
for thisComponent in Instr_rotateComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_rotateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_rotate"-------
while continueRoutine:
    # get current time
    t = Instr_rotateClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_rotateClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct_text_2* updates
    if Instruct_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct_text_2.frameNStart = frameN  # exact frame index
        Instruct_text_2.tStart = t  # local t and not account for scr refresh
        Instruct_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct_text_2, 'tStartRefresh')  # time at next scr refresh
        Instruct_text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_rotateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_rotate"-------
for thisComponent in Instr_rotateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct_text_2.started', Instruct_text_2.tStartRefresh)
thisExp.addData('Instruct_text_2.stopped', Instruct_text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr_rotate" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_vmr = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Target_file_real.xlsx', selection='17:96'),
    seed=None, name='trials_vmr')
thisExp.addLoop(trials_vmr)  # add the loop to the experiment
thisTrials_vmr = trials_vmr.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_vmr.rgb)
if thisTrials_vmr != None:
    for paramName in thisTrials_vmr:
        exec('{} = thisTrials_vmr[paramName]'.format(paramName))

for thisTrials_vmr in trials_vmr:
    currentLoop = trials_vmr
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_vmr.rgb)
    if thisTrials_vmr != None:
        for paramName in thisTrials_vmr:
            exec('{} = thisTrials_vmr[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Reach_VMR"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Initilize local varibles
    wait_time = 0
    wait_time2 =0
    counter = 0
    target.opacity = 0;
    
    #Make sure these are invisbile to start
    EndpointMarker_2.opacity=0;
    Invis_Home_2.opacity = 1
    
    #Set the target position at the start of each routine
    rad1 = radians(tgt_angle)
    Targetxx = xcoord2cart(tgt_distance,rad1)
    Targetyy = ycoord2cart(tgt_distance,rad1)
    # setup some python lists for storing info about the mouse_3
    gotValidClick = False  # until a click is received
    mouse_3.mouseClock.reset()
    # keep track of which components have finished
    Reach_VMRComponents = [target_2, Invis_Home_2, mouse_3, Cursor_mouse, Cursor_VMR, EndpointMarker_2]
    for thisComponent in Reach_VMRComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Reach_VMRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reach_VMR"-------
    while continueRoutine:
        # get current time
        t = Reach_VMRClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Reach_VMRClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_2* updates
        if target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target_2.frameNStart = frameN  # exact frame index
            target_2.tStart = t  # local t and not account for scr refresh
            target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
            target_2.setAutoDraw(True)
        if target_2.status == STARTED:  # only update if drawing
            target_2.setPos((Targetxx,Targetyy), log=False)
        #Find distance from origin to cursor at every frame
        Dist_from_Home = sqrt(((mouse_3.getPos()[0]-Invis_Home_2.pos[0])**2)+(mouse_3.getPos()[1]-Invis_Home_2.pos[1])**2)
        
        #####################################################
        #Phase 0, using 'counter' to change phases
        #Finding Home phase
        #When cursor within certain distance of home, becomes visible
        #When its within home radius, waits 20 frames then goes to next phase
        
        if counter ==0:
            Invis_Home_2.opacity = 1;
            target_2.opacity = 0;
            
            if Dist_from_Home > 0.15:
                continueRoutine = True;
                Cursor_mouse.opacity =0
            if (Dist_from_Home <= 0.15) & (Dist_from_Home > 0.0125):
                continueRoutine = True;
                Cursor_mouse.opacity =1
            if Dist_from_Home < 0.0125:
                wait_time = wait_time+1
            if wait_time > 20: 
                target_2.opacity = 1;
                Invis_Home_2.opacity = 0.0;
                counter=1;
        ####################################################
        #Phase 1
        #REACH Phase
        #Checks target file for online feedback y/n
        #Sets 'rotated cursor' position based on mouse position
        #Once cursor crosses 'target ring', goes to next phase
        
        if counter == 1:
            if online_fb == 1:
                Cursor_mouse.opacity =1;
            if online_fb == 0:
                Cursor_mouse.opacity=0;
            Invis_Home.opacity = 0.0;
            target.opacity = 1;
            Cursor_VMR.opacity=1;
            
            #finds mouse x,y pos and converts to phi in degrees
            [rho2,phi2] = cart2pol(mouse_3.getPos()[0],mouse_3.getPos()[1])
            phi2 = degree(phi2)
        
            #Rx,Ry fed into Cursor_VMR to set its position
            Rx = (Dist_from_Home)*(cos(radians(phi2-rotation)))
            Ry = (Dist_from_Home)*(sin(radians(phi2-rotation)))
        
            if Dist_from_Home > 0.354:
                counter = 2
        
        #Phase 2
        #Endpoint phase
        #Checks target file for endpoint y/n
        #Tx calculates the phi of the rotated cursor
        #Tx plugged into the endpointmarker
        #endpoint stays for 20 frames, then routine ends
        
        if counter == 2:
            Cursor_VMR.opacity = 0;
            EndpointMarker_2.opacity =1;
                    
            Tx = JustPhi((Cursor_VMR.pos[0]-Invis_Home_2.pos[0]),(Cursor_VMR.pos[1]-Invis_Home_2.pos[1]))
            
            wait_time2 = wait_time2+1
            if wait_time2 == 1:
                EndPointCursorxx = xcoord2cart(0.354,Tx);
                EndPointCursoryy = ycoord2cart(0.354,Tx);
            if wait_time2 >20:
                continueRoutine = False;
        else:
            continueRoutine = True; 
        
        # *Invis_Home_2* updates
        if Invis_Home_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Invis_Home_2.frameNStart = frameN  # exact frame index
            Invis_Home_2.tStart = t  # local t and not account for scr refresh
            Invis_Home_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Invis_Home_2, 'tStartRefresh')  # time at next scr refresh
            Invis_Home_2.setAutoDraw(True)
        
        # *Cursor_mouse* updates
        if Cursor_mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cursor_mouse.frameNStart = frameN  # exact frame index
            Cursor_mouse.tStart = t  # local t and not account for scr refresh
            Cursor_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cursor_mouse, 'tStartRefresh')  # time at next scr refresh
            Cursor_mouse.setAutoDraw(True)
        if Cursor_mouse.status == STARTED:  # only update if drawing
            Cursor_mouse.setPos((mouse_3.getPos()[0], mouse_3.getPos()[1]), log=False)
        
        # *Cursor_VMR* updates
        if Cursor_VMR.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cursor_VMR.frameNStart = frameN  # exact frame index
            Cursor_VMR.tStart = t  # local t and not account for scr refresh
            Cursor_VMR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cursor_VMR, 'tStartRefresh')  # time at next scr refresh
            Cursor_VMR.setAutoDraw(True)
        if Cursor_VMR.status == STARTED:  # only update if drawing
            Cursor_VMR.setPos((Rx,Ry), log=False)
        
        # *EndpointMarker_2* updates
        if EndpointMarker_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndpointMarker_2.frameNStart = frameN  # exact frame index
            EndpointMarker_2.tStart = t  # local t and not account for scr refresh
            EndpointMarker_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndpointMarker_2, 'tStartRefresh')  # time at next scr refresh
            EndpointMarker_2.setAutoDraw(True)
        if EndpointMarker_2.status == STARTED:  # only update if drawing
            EndpointMarker_2.setPos((EndPointCursorxx,EndPointCursoryy), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Reach_VMRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reach_VMR"-------
    for thisComponent in Reach_VMRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_vmr.addData('target_2.started', target_2.tStartRefresh)
    trials_vmr.addData('target_2.stopped', target_2.tStopRefresh)
    trials_vmr.addData('Invis_Home_2.started', Invis_Home_2.tStartRefresh)
    trials_vmr.addData('Invis_Home_2.stopped', Invis_Home_2.tStopRefresh)
    # store data for trials_vmr (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    trials_vmr.addData('mouse_3.x', x)
    trials_vmr.addData('mouse_3.y', y)
    trials_vmr.addData('mouse_3.leftButton', buttons[0])
    trials_vmr.addData('mouse_3.midButton', buttons[1])
    trials_vmr.addData('mouse_3.rightButton', buttons[2])
    trials_vmr.addData('mouse_3.started', mouse_3.tStart)
    trials_vmr.addData('mouse_3.stopped', mouse_3.tStop)
    trials_vmr.addData('Cursor_mouse.started', Cursor_mouse.tStartRefresh)
    trials_vmr.addData('Cursor_mouse.stopped', Cursor_mouse.tStopRefresh)
    trials_vmr.addData('Cursor_VMR.started', Cursor_VMR.tStartRefresh)
    trials_vmr.addData('Cursor_VMR.stopped', Cursor_VMR.tStopRefresh)
    trials_vmr.addData('EndpointMarker_2.started', EndpointMarker_2.tStartRefresh)
    trials_vmr.addData('EndpointMarker_2.stopped', EndpointMarker_2.tStopRefresh)
    # the Routine "Reach_VMR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_vmr'


# ------Prepare to start Routine "Instr_wash"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instr_washComponents = [Instruct_text_3, key_resp_3]
for thisComponent in Instr_washComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_washClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_wash"-------
while continueRoutine:
    # get current time
    t = Instr_washClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_washClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct_text_3* updates
    if Instruct_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruct_text_3.frameNStart = frameN  # exact frame index
        Instruct_text_3.tStart = t  # local t and not account for scr refresh
        Instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruct_text_3, 'tStartRefresh')  # time at next scr refresh
        Instruct_text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_washComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_wash"-------
for thisComponent in Instr_washComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instruct_text_3.started', Instruct_text_3.tStartRefresh)
thisExp.addData('Instruct_text_3.stopped', Instruct_text_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr_wash" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_washout_nofb = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Target_file_real.xlsx', selection='97:105'),
    seed=None, name='trials_washout_nofb')
thisExp.addLoop(trials_washout_nofb)  # add the loop to the experiment
thisTrials_washout_nofb = trials_washout_nofb.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_washout_nofb.rgb)
if thisTrials_washout_nofb != None:
    for paramName in thisTrials_washout_nofb:
        exec('{} = thisTrials_washout_nofb[paramName]'.format(paramName))

for thisTrials_washout_nofb in trials_washout_nofb:
    currentLoop = trials_washout_nofb
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_washout_nofb.rgb)
    if thisTrials_washout_nofb != None:
        for paramName in thisTrials_washout_nofb:
            exec('{} = thisTrials_washout_nofb[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Reach"-------
    continueRoutine = True
    # update component parameters for each repeat
    target.setPos((Targetxx,Targetyy))
    #Initilize local varibles 
    mouse_2.setVisible(False)
    wait_time = 0 
    wait_time2 = 0
    counter = 0
    Cursor_2.setColor('white')
    
    
    ###########################
    
    #Make sure target, endpint invisible to start
    target.opacity = 0;
    EndpointMarker.opacity =0;
    
    
    #Convert target file to radians
    rad1 = radians(tgt_angle)
    
    #Set the target's x,y position
    Targetxx = xcoord2cart(tgt_distance,rad1)
    Targetyy = ycoord2cart(tgt_distance,rad1)
    
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ReachComponents = [target, Invis_Home, mouse_2, Cursor_2, EndpointMarker]
    for thisComponent in ReachComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ReachClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reach"-------
    while continueRoutine:
        # get current time
        t = ReachClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ReachClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        #Find distance from origin to cursor at every frame
        Dist_from_Home = sqrt(((Cursor_2.pos[0]-Invis_Home.pos[0])**2)+(Cursor_2.pos[1]-Invis_Home.pos[1])**2)
        
        #####################################################
        #Phase 0, using 'counter' to change phases
        #Finding Home phase
        #When cursor within certain distance of home, becomes visible
        #When its within home radius, waits 20 frames then goes to next phase
        
        
        if counter ==0:
            Invis_Home.opacity = 1;
            target.opacity = 0;
            
            if Dist_from_Home > 0.15:
                continueRoutine = True;
                Cursor_2.opacity =0
            if (Dist_from_Home <= 0.15) & (Dist_from_Home > 0.0125):
                continueRoutine = True;
                
                Cursor_2.opacity =1
            if Dist_from_Home < 0.0125:
                wait_time = wait_time+1
            if wait_time > 20: 
                counter=1;
        ##################################################
        #Phase 1
        #REACH Phase
        #Checks target file for online feedback y/n
        #Once cursor crosses 'target ring', goes to next phase
        
        if counter ==1:
            if online_fb == 1:
                Cursor_2.opacity =1;
            if online_fb == 0:
                Cursor_2.opacity=0;
            Invis_Home.opacity = 0.0;
            target.opacity = 1;
        
        
            if Dist_from_Home > 0.354:
                Cursor_2.fillColor = 'gray';
                Cursor_2.opacity=0;
                counter=2
        
        #Phase 2
        #Endpoint phase
        #Checks target file for endpoint y/n
        #Tx calculates the phi of the cursor
        #Tx plugged into the endpointmarker
        #endpoint stays for 20 frames, then routine ends
        
        
        if counter == 2:
            if endpoint_feedback == 1:
                EndpointMarker.opacity =1;
            if endpoint_feedback == 0:
                EndppointMarker.opacity=0;
            #Cursor_2.opacity=1;
                    
            Tx = JustPhi((Cursor_2.pos[0]-Invis_Home.pos[0]),(Cursor_2.pos[1]-Invis_Home.pos[1]))
            wait_time2 = wait_time2+1
                    
            if wait_time2 == 1:
                 EndPointCursorx = xcoord2cart(0.354,Tx);
                 EndPointCursory = ycoord2cart(0.354,Tx);
            if wait_time2 >20:
                continueRoutine = False;
        else:
            continueRoutine = True;
        
        # *Invis_Home* updates
        if Invis_Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Invis_Home.frameNStart = frameN  # exact frame index
            Invis_Home.tStart = t  # local t and not account for scr refresh
            Invis_Home.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Invis_Home, 'tStartRefresh')  # time at next scr refresh
            Invis_Home.setAutoDraw(True)
        
        # *Cursor_2* updates
        if Cursor_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cursor_2.frameNStart = frameN  # exact frame index
            Cursor_2.tStart = t  # local t and not account for scr refresh
            Cursor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cursor_2, 'tStartRefresh')  # time at next scr refresh
            Cursor_2.setAutoDraw(True)
        if Cursor_2.status == STARTED:  # only update if drawing
            Cursor_2.setPos((mouse_2.getPos()[0],mouse_2.getPos()[1]), log=False)
        
        # *EndpointMarker* updates
        if EndpointMarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndpointMarker.frameNStart = frameN  # exact frame index
            EndpointMarker.tStart = t  # local t and not account for scr refresh
            EndpointMarker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndpointMarker, 'tStartRefresh')  # time at next scr refresh
            EndpointMarker.setAutoDraw(True)
        if EndpointMarker.status == STARTED:  # only update if drawing
            EndpointMarker.setPos((EndPointCursorx, EndPointCursory), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReachComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reach"-------
    for thisComponent in ReachComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_washout_nofb.addData('target.started', target.tStartRefresh)
    trials_washout_nofb.addData('target.stopped', target.tStopRefresh)
    trials_washout_nofb.addData('Invis_Home.started', Invis_Home.tStartRefresh)
    trials_washout_nofb.addData('Invis_Home.stopped', Invis_Home.tStopRefresh)
    # store data for trials_washout_nofb (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    trials_washout_nofb.addData('mouse_2.x', x)
    trials_washout_nofb.addData('mouse_2.y', y)
    trials_washout_nofb.addData('mouse_2.leftButton', buttons[0])
    trials_washout_nofb.addData('mouse_2.midButton', buttons[1])
    trials_washout_nofb.addData('mouse_2.rightButton', buttons[2])
    trials_washout_nofb.addData('mouse_2.started', mouse_2.tStartRefresh)
    trials_washout_nofb.addData('mouse_2.stopped', mouse_2.tStopRefresh)
    trials_washout_nofb.addData('Cursor_2.started', Cursor_2.tStartRefresh)
    trials_washout_nofb.addData('Cursor_2.stopped', Cursor_2.tStopRefresh)
    trials_washout_nofb.addData('EndpointMarker.started', EndpointMarker.tStartRefresh)
    trials_washout_nofb.addData('EndpointMarker.stopped', EndpointMarker.tStopRefresh)
    # the Routine "Reach" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_washout_nofb'


# ------Prepare to start Routine "Instr_wash_fb"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Instr_wash_fbComponents = [text_2, key_resp_6]
for thisComponent in Instr_wash_fbComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_wash_fbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_wash_fb"-------
while continueRoutine:
    # get current time
    t = Instr_wash_fbClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_wash_fbClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_wash_fbComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_wash_fb"-------
for thisComponent in Instr_wash_fbComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instr_wash_fb" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_washout_fb = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Target_file_real.xlsx', selection='106:128'),
    seed=None, name='trials_washout_fb')
thisExp.addLoop(trials_washout_fb)  # add the loop to the experiment
thisTrials_washout_fb = trials_washout_fb.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_washout_fb.rgb)
if thisTrials_washout_fb != None:
    for paramName in thisTrials_washout_fb:
        exec('{} = thisTrials_washout_fb[paramName]'.format(paramName))

for thisTrials_washout_fb in trials_washout_fb:
    currentLoop = trials_washout_fb
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_washout_fb.rgb)
    if thisTrials_washout_fb != None:
        for paramName in thisTrials_washout_fb:
            exec('{} = thisTrials_washout_fb[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Reach"-------
    continueRoutine = True
    # update component parameters for each repeat
    target.setPos((Targetxx,Targetyy))
    #Initilize local varibles 
    mouse_2.setVisible(False)
    wait_time = 0 
    wait_time2 = 0
    counter = 0
    Cursor_2.setColor('white')
    
    
    ###########################
    
    #Make sure target, endpint invisible to start
    target.opacity = 0;
    EndpointMarker.opacity =0;
    
    
    #Convert target file to radians
    rad1 = radians(tgt_angle)
    
    #Set the target's x,y position
    Targetxx = xcoord2cart(tgt_distance,rad1)
    Targetyy = ycoord2cart(tgt_distance,rad1)
    
    # setup some python lists for storing info about the mouse_2
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    ReachComponents = [target, Invis_Home, mouse_2, Cursor_2, EndpointMarker]
    for thisComponent in ReachComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ReachClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Reach"-------
    while continueRoutine:
        # get current time
        t = ReachClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ReachClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        #Find distance from origin to cursor at every frame
        Dist_from_Home = sqrt(((Cursor_2.pos[0]-Invis_Home.pos[0])**2)+(Cursor_2.pos[1]-Invis_Home.pos[1])**2)
        
        #####################################################
        #Phase 0, using 'counter' to change phases
        #Finding Home phase
        #When cursor within certain distance of home, becomes visible
        #When its within home radius, waits 20 frames then goes to next phase
        
        
        if counter ==0:
            Invis_Home.opacity = 1;
            target.opacity = 0;
            
            if Dist_from_Home > 0.15:
                continueRoutine = True;
                Cursor_2.opacity =0
            if (Dist_from_Home <= 0.15) & (Dist_from_Home > 0.0125):
                continueRoutine = True;
                
                Cursor_2.opacity =1
            if Dist_from_Home < 0.0125:
                wait_time = wait_time+1
            if wait_time > 20: 
                counter=1;
        ##################################################
        #Phase 1
        #REACH Phase
        #Checks target file for online feedback y/n
        #Once cursor crosses 'target ring', goes to next phase
        
        if counter ==1:
            if online_fb == 1:
                Cursor_2.opacity =1;
            if online_fb == 0:
                Cursor_2.opacity=0;
            Invis_Home.opacity = 0.0;
            target.opacity = 1;
        
        
            if Dist_from_Home > 0.354:
                Cursor_2.fillColor = 'gray';
                Cursor_2.opacity=0;
                counter=2
        
        #Phase 2
        #Endpoint phase
        #Checks target file for endpoint y/n
        #Tx calculates the phi of the cursor
        #Tx plugged into the endpointmarker
        #endpoint stays for 20 frames, then routine ends
        
        
        if counter == 2:
            if endpoint_feedback == 1:
                EndpointMarker.opacity =1;
            if endpoint_feedback == 0:
                EndppointMarker.opacity=0;
            #Cursor_2.opacity=1;
                    
            Tx = JustPhi((Cursor_2.pos[0]-Invis_Home.pos[0]),(Cursor_2.pos[1]-Invis_Home.pos[1]))
            wait_time2 = wait_time2+1
                    
            if wait_time2 == 1:
                 EndPointCursorx = xcoord2cart(0.354,Tx);
                 EndPointCursory = ycoord2cart(0.354,Tx);
            if wait_time2 >20:
                continueRoutine = False;
        else:
            continueRoutine = True;
        
        # *Invis_Home* updates
        if Invis_Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Invis_Home.frameNStart = frameN  # exact frame index
            Invis_Home.tStart = t  # local t and not account for scr refresh
            Invis_Home.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Invis_Home, 'tStartRefresh')  # time at next scr refresh
            Invis_Home.setAutoDraw(True)
        
        # *Cursor_2* updates
        if Cursor_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cursor_2.frameNStart = frameN  # exact frame index
            Cursor_2.tStart = t  # local t and not account for scr refresh
            Cursor_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cursor_2, 'tStartRefresh')  # time at next scr refresh
            Cursor_2.setAutoDraw(True)
        if Cursor_2.status == STARTED:  # only update if drawing
            Cursor_2.setPos((mouse_2.getPos()[0],mouse_2.getPos()[1]), log=False)
        
        # *EndpointMarker* updates
        if EndpointMarker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndpointMarker.frameNStart = frameN  # exact frame index
            EndpointMarker.tStart = t  # local t and not account for scr refresh
            EndpointMarker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndpointMarker, 'tStartRefresh')  # time at next scr refresh
            EndpointMarker.setAutoDraw(True)
        if EndpointMarker.status == STARTED:  # only update if drawing
            EndpointMarker.setPos((EndPointCursorx, EndPointCursory), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReachComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Reach"-------
    for thisComponent in ReachComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_washout_fb.addData('target.started', target.tStartRefresh)
    trials_washout_fb.addData('target.stopped', target.tStopRefresh)
    trials_washout_fb.addData('Invis_Home.started', Invis_Home.tStartRefresh)
    trials_washout_fb.addData('Invis_Home.stopped', Invis_Home.tStopRefresh)
    # store data for trials_washout_fb (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    trials_washout_fb.addData('mouse_2.x', x)
    trials_washout_fb.addData('mouse_2.y', y)
    trials_washout_fb.addData('mouse_2.leftButton', buttons[0])
    trials_washout_fb.addData('mouse_2.midButton', buttons[1])
    trials_washout_fb.addData('mouse_2.rightButton', buttons[2])
    trials_washout_fb.addData('mouse_2.started', mouse_2.tStartRefresh)
    trials_washout_fb.addData('mouse_2.stopped', mouse_2.tStopRefresh)
    trials_washout_fb.addData('Cursor_2.started', Cursor_2.tStartRefresh)
    trials_washout_fb.addData('Cursor_2.stopped', Cursor_2.tStopRefresh)
    trials_washout_fb.addData('EndpointMarker.started', EndpointMarker.tStartRefresh)
    trials_washout_fb.addData('EndpointMarker.stopped', EndpointMarker.tStopRefresh)
    # the Routine "Reach" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_washout_fb'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
EndComponents = [text, key_resp_5]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
