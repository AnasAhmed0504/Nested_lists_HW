class Our_Zip:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.cur_col_idx = 0
        
    
    
    def has_next(self):
        for seq in self.iterables:
            if self.cur_col_idx < len(seq):
                return True
        return False
    

    def get_next(self):
        ret = [0] * len(self.iterables)
        for idx, seq in enumerate(self.iterables):
            if self.cur_col_idx < len(seq):
                
                ret[idx] = self.iterablese[idx][self.cur_col_idx]
            else:
                ret[idx] = None
        self.cur_col_idx += 1
        
        return tuple(ret)
