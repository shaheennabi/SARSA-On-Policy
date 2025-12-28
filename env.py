
class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols 
        self.current_state = None
        self.start = (0,0)
        self.terminal_state = (rows-1, cols-1)




    def reset(self):
        self.current_state = self.start
        return self.__coordinate_to_stateId(self.current_state)
    


    def __coordinate_to_stateId(self, coordinate):
        row, col = coordinate
        return row * self.cols + col
    


    def step(self, action):
        row, col = self.current_state

        if action == 0: #up
            new_row, new_col = row-1, col
        
        elif action == 1: #right
            new_row, new_col = row, col+1
        
        elif action == 2: #left
            new_row, new_col = row, col-1

        elif action == 3: #down
            new_row, new_col = row+1, col

        else:
            raise ValueError("Invalid Action")
        

        ## out of grid actions
        if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
            new_row, new_col = row, col

        self.current_state = new_row, new_col

        

        ## coordinate to state_id
        next_state = self.__coordinate_to_stateId(self.current_state)

        ## reward

        if self.current_state == self.terminal_state:
            reward = 0
            done = True
        
        else:
            reward = -1
            done = False
        
        return next_state, reward, done

