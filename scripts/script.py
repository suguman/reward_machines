import os

env = 'Rooms9C'
alg = "ddpg"

mydict = {}
mydict['Rooms9'] = {}
mydict['Rooms9']['time'] = '3e6'
mydict['Rooms9']['rm'] = [('M1', '1.6e6'), ('M2', '3e6'), ('M4', '2e6')]
mydict['Rooms9']['gamma'] = 0.99
mydict['Rooms9']['options'] = ['rs', 'rc', 'cr']

mydict['Rooms9C'] = {}
mydict['Rooms9C']['time'] = '3e6'
mydict['Rooms9C']['rm'] = [('M1', '2e6'), ('M2', '2e6'), ('M3', '3.2e6'), ('M4', '1.5e6'),('M5', '3.2e6')]
mydict['Rooms9C']['gamma'] = 0.99
mydict['Rooms9C']['options'] = ['cr', 'basic']

mydict['Rooms16'] = {}
mydict['Rooms16']['time'] = '1.5e7'
mydict['Rooms16']['rm'] = [('M1', '3.5e6'), ('M2', '6.5e6'), ('M3', '1.1e7')]
mydict['Rooms16']['gamma'] = 0.99
mydict['Rooms16']['options'] = ['rs', 'cr', 'rc']

mydict['Rooms16C'] = {}
mydict['Rooms16C']['time'] = '1.5e7'
#mydict['Rooms16C']['rm'] = [('M1', '3.3e6'), ('M2', '5.2e6'), ('M3', '9e6'), ('M4', '1.7e7'), ('M5', '2.1e7')]
mydict['Rooms16C']['rm'] = [('M3', '9e6'), ('M4', '1.7e7'), ('M5', '2.1e7')]
mydict['Rooms16C']['gamma'] = 0.99
mydict['Rooms16C']['options'] = ['cr', 'basic']

mydict['Fetch'] = {}
mydict['Fetch']['time'] = '2.5e5'
mydict['Fetch']['rm'] = [('M1', '2.2e5'), ('M2','2.2e5'), ('M3','4.2e5')]
mydict['Fetch']['gamma'] = 0.95
mydict['Fetch']['options'] = ['cr', 'basic']



num_iter = 3
DIR = '../results'
dict1 = mydict[env]
for (rm,timestep) in dict1['rm']:
    env_name = '-'.join([env, rm,'v0'])
    for option in dict1['options']:
        if option == 'rs':
            flag = '--use_rs'
        if option == 'cr':
            flag = '--use_crm'
        if option == 'rc':
            flag = '--use_crm --use_rs'
        if option == "basic":
            flag = ''

        if alg=="dhrm":
            flag += " --r_max=1000 --r_mix=-1000 "
        dirname = '/'.join([DIR,env,rm,alg, option])
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        for i in range(num_iter):
            path = dirname + "/" + str(i) 
            #print(path)

            temp = env+rm+alg+option+str(i)
            
            cmd = " ".join(['screen -dmS', temp, 'python3 run.py --alg='+alg,
                           '--env='+env_name,
                           '--num_timesteps='+timestep,
                            '--gamma='+str(dict1['gamma']),
                            "--log_path="+path,
                            flag])

            print(cmd)
