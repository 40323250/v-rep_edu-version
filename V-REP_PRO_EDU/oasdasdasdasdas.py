import vrep
import sys
# child threaded script: 
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)


if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode,Revolute_joint0_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint0',vrep.simx_opmode_oneshot_wait)
errorCode1,Revolute_joint1_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint1',vrep.simx_opmode_oneshot_wait)
errorCode2,Revolute_joint2_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint2',vrep.simx_opmode_oneshot_wait)
errorCode3,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait)
 


if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
 
errorCode=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint0_handle,2, vrep.simx_opmode_oneshot_wait)
errorCode1=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint1_handle,2, vrep.simx_opmode_oneshot_wait)
errorCode2=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint2_handle,2, vrep.simx_opmode_oneshot_wait)
errorCode3=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint_handle,2, vrep.simx_opmode_oneshot_wait)





