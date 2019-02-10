class Steps:
    num_mod = 0
    exp_int_list, cuberoot_list, sqrt_list = [], [], []

    def append(self,steps):
        self.num_mod += steps.num_mod
        self.exp_int_list.append(steps.exp_int_list)
        self.cuberoot_list.append(steps.cuberoot_list)
        self.sqrt_list.append(steps.sqrt_list)

    def total_steps(self):
        return 0 #TODO how to weight each?