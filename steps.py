class Steps:
    num_mod = 0
    exp_list, cuberoot_list, sqrt_list = [], [], []
    log_list = []
    def append(self,steps):
        self.num_mod += steps.num_mod
        self.exp_list.append(steps.exp_list)
        self.cuberoot_list.append(steps.cuberoot_list)
        self.sqrt_list.append(steps.sqrt_list)
        self.log_list.append(steps.log_list)
        
    def total_steps(self):
        return 0 #TODO how to weight each?