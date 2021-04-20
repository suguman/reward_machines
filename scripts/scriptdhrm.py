import os

env = 'Rooms16C'

mydict = {}
mydict['Rooms9'] = {}
mydict['Rooms9']['time'] = '3e6'
mydict['Rooms9']['rm'] = ['M1', 'M2']
mydict['Rooms9']['gamma'] = 0.99
mydict['Rooms9']['options'] = ['cr', 'basic']

mydict['Rooms9C'] = {}
mydict['Rooms9C']['time'] = '3e6'
mydict['Rooms9C']['rm'] = ['M1', 'M2']
mydict['Rooms9C']['gamma'] = 0.99
mydict['Rooms9C']['options'] = ['cr', 'basic']

mydict['Rooms16'] = {}
mydict['Rooms16']['time'] = '1.5e7'
mydict['Rooms16']['rm'] = ['M1', 'M2','M3']
mydict['Rooms16']['gamma'] = 0.99
mydict['Rooms16']['options'] = ['cr', 'basic']

mydict['Rooms16C'] = {}
mydict['Rooms16C']['time'] = '1.5e7'
mydict['Rooms16C']['rm'] = ['M1', 'M2','M3']
mydict['Rooms16C']['gamma'] = 0.99
mydict['Rooms16C']['options'] = ['cr', 'basic']


num_iter = 3
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
        if option == "basic":
            flag = ''
            
        dirname = '/'.join([DIR,env,rm,option])
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        for i in range(num_iter):
            path = dirname + "/" + str(i) 
            #print(path)

            temp = env+rm+option+str(i)
            
            cmd = " ".join(['screen -dmS', temp, 'python3 run.py --alg=dhrm',
                           '--env='+env_name,
                           '--num_timesteps='+dict1['time'],
                            '--gamma='+str(dict1['gamma']),
                            "--log_path="+path,
                            flag,
                            "--use_self_loops"])

            print(cmd)
