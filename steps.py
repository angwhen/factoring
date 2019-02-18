class Steps:
    def __init__(self):
        self.num_mod = 0
        self.exp_list, self.cuberoot_list, self.sqrt_list = [], [], []
        self. log_list = []

    def add_mod(self,num=1):
        self.num_mod += num
    def add_exp(self,x,y):
        self.exp_list.append((x,y))
    def add_cuberoot(self,x):
        self.cuberoot_list.append(x)
    def add_sqrt(self,x):
        self.sqrt_list.append(x)
    def add_log(self,x):
        self.log_list.append(x)

    def append(self,steps):
        self.num_mod += steps.num_mod
        self.exp_list.extend(steps.exp_list)
        self.cuberoot_list.extend(steps.cuberoot_list)
        self.sqrt_list.extend(steps.sqrt_list)
        self.log_list.extend(steps.log_list)
    
    def __str__(self):
        return "num mod: %d  num_sqrt: %d num_cuberoot: %d" %(self.num_mod,len(self.sqrt_list),len(self.cuberoot_list))



# dicts for each algo, number : (factors list, steps) 
class AlgoSteps:
    def __init__(self):
        self.num_list = []
        self.factors_list = []
        self.steps_list = []

    # TODO: account for different steps for the same number on different runs of the algo
    def add(self,num,factors, steps):
        self.num_list.append(num)
        self.factors_list.append(factors)
        self.steps_list.append(steps)

    def extend(self,AlgoSteps):
        return 0


def get_gen_steps_list(algo_steps):
    steps_list = algo_steps.steps_list
    gen_steps_list = []
    for step in steps_list:
        gen_steps_list.append(get_gen_steps(step))
    return gen_steps_list

def get_gen_steps(steps):
    gen_steps = steps.num_mod + len(steps.exp_list) + len(steps.cuberoot_list)
    gen_steps += len(steps.sqrt_list) + len(steps.log_list)
    return gen_steps