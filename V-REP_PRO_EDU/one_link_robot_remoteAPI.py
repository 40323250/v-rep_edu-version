import vrep
import sys
# child threaded script: 
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
clientID2 = clientID
clientID3 = clientID2
clientID4 = clientID3

if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint0',vrep.simx_opmode_oneshot_wait)
 
if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
 
errorCode=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint0_handle,2, vrep.simx_opmode_oneshot_wait)


if clientID2!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode1,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint1',vrep.simx_opmode_oneshot_wait)
 
if errorCode1 == -1:
    print('Can not find left or right motor')
    sys.exit()
 
errorCode1=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint1_handle,2, vrep.simx_opmode_oneshot_wait)


if clientID2!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode1,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait)
 
if errorCode1 == -1:
    print('Can not find left or right motor')
    sys.exit()
 
errorCode1=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint1_handle,2, vrep.simx_opmode_oneshot_wait)










