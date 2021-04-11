import os

env = 'Rooms16'

mydict = {}
mydict['Rooms9'] = {}
mydict['Rooms9']['time'] = '3e6'
mydict['Rooms9']['rm'] = ['M1', 'M2']
mydict['Rooms9']['gamma'] = 0.99
mydict['Rooms9']['options'] = ['rs', 'rc', 'cr']

mydict['Rooms16'] = {}
mydict['Rooms16']['time'] = '1.5e7'
mydict['Rooms16']['rm'] = ['M1', 'M2','M3']
mydict['Rooms16']['gamma'] = 0.99
mydict['Rooms16']['options'] = ['rs', 'cr', 'rc']

num_iter = 10
DIR = '../results'
dict1 = mydict[env]
for rm in dict1['rm']:
    env_name = '-'.join([env, rm,'v0'])
    for option in dict1['options']:
        if option == 'rs':
            flag = '--use_rs'
        if option == 'cr':
            flag = '--use_crm'
        if option == 'rc':
            flag = '--use_crm --use_rs'

        dirname = '/'.join([DIR,env,rm,option])
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        for i in range(num_iter):
            path = dirname + "/" + str(i) 
            #print(path)

            temp = env+rm+option
            
            cmd = " ".join(['screen -dmS', temp, 'python3 run.py --alg=ddpg',
                           '--env='+env_name,
                           '--num_timesteps='+dict1['time'],
                            '--gamma='+str(dict1['gamma']),
                            "--log-path="+path])

            print(cmd)
