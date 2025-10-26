import numpy as np
import random

class game_2048:
    def __init__(self):
        self.initialise()

    def initialise(self):
        self.matrix = np.zeros((4,4))
        self.choice_list = [2,2,2,2,2,2,2,2,4,4]
        for i in range(2):
            l,b = random.randint(0,3),random.randint(0,3)

            self.matrix[l,b] = random.choice(self.choice_list)

    def place_numbers(self):
        if random.random() < 0.2:
            return 2
        elif random.random() < 0.1:
            return 4
        else:
            return 0
        
    def Left_move(self):
        #before shifting and adding, place all the 2 and 4
        score = []
        

        # now move all the numbers in the right direction and merge if needed
        for i in range(4):
            n = 1
            while n<4:
                if self.matrix[i][n] != 0:
                    #move towards left until encounter non zero or end of array
                    m = n-1
                    while m>=0:
                        if self.matrix[i][m] == 0:
                            self.matrix[i][m],self.matrix[i][n] = self.matrix[i][n],self.matrix[i][m]
                            n =m
                        elif self.matrix[i][m] == self.matrix[i][n]:
                            #if they are same number, then add those numbers
                            self.matrix[i][m],self.matrix[i][n] = self.matrix[i,n]*2,0
                            score.append(self.matrix[i][m])
                            n =m
                        m -=1
                n +=1
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self.place_numbers()
        return score

    def Right_move(self):
        #before shifting and adding, place all the 2 and 4
        score = []
      

        # now move all the numbers in the right direction and merge if needed
        for i in range(4):
            n = 3
            while n>-1:
                if self.matrix[i][n] != 0:
                    m = n+1
                    while m<4:
                        if self.matrix[i][m] == 0:
                            self.matrix[i][m],self.matrix[i][n] = self.matrix[i][n],self.matrix[i][m]
                            n =m
                        elif self.matrix[i][m] == self.matrix[i][n]:
                            #if they are same number, then add those numbers
                            self.matrix[i][m],self.matrix[i][n] = self.matrix[i,n]*2,0
                            score.append(self.matrix[i][m])
                            n =m
                        m +=1
                n -=1
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self.place_numbers()
        return score

    def Up_move(self):
        #before shifting and adding, place all the 2 and 4
        score = []

        # now move all the numbers in the right direction and merge if needed
        for i in range(4):
            n = 1
            while n<4:
                if self.matrix[n][i] != 0:
                    #move towards left until encounter non zero or end of array
                    m = n-1
                    while m>=0:
                        if self.matrix[m][i] == 0:
                            self.matrix[m][i],self.matrix[n][i]= self.matrix[n][i],self.matrix[m][i]
                            n =m
                        elif self.matrix[m][i] == self.matrix[n][i]:
                            #if they are same number, then add those numbers
                            self.matrix[m][i],self.matrix[n][i] = self.matrix[n][i]*2,0
                            score.append(self.matrix[m][i])
                            n =m
                        m -=1
                n +=1
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self.place_numbers()
        return score

    def Down_move(self):
        #before shifting and adding, place all the 2 and 4
  
        score = []

        # now move all the numbers in the right direction and merge if needed
        for i in range(4):
            n = 3
            while n>-1:
                if self.matrix[n][i] != 0:
                    m = n+1
                    while m<4:
                        if self.matrix[m][i] == 0:
                            self.matrix[m][i],self.matrix[n][i] = self.matrix[n][i],self.matrix[m][i]
                            n =m
                        elif self.matrix[m][i] == self.matrix[n][i]:
                            #if they are same number, then add those numbers
                            self.matrix[m][i],self.matrix[n][i] = self.matrix[n][i]*2,0
                            score.append(self.matrix[m][i])
                            n =m
                        m +=1
                n -=1
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = self.place_numbers()
        return score
    
    def check_termination(self):
        flag = 0
        matrix = self.matrix.copy()
        # do all operations and check if matrix is same after each, after each operation revert the state to original state
        moves = [self.Up_move,self.Down_move,self.Right_move,self.Left_move]
        for m in moves:
            matrix = self.matrix.copy()
            _ = m()            
            if np.array_equal(matrix,self.matrix):
                flag += 1
            
        
        if flag == 4:
            return -1
        self.matrix = matrix.copy()
        return 0



 
    def run(self,a):
        matrix = self.matrix.copy()
        if a == 0:
            r = self.Up_move()
        elif a == 1:
            r = self.Down_move()
        elif a == 2:
            r = self.Right_move()
        elif a == 3:
            r = self.Left_move()
        if np.array_equal(matrix,self.matrix):

            return self.check_termination()
        else:
            if not r:
                return 0
            else:
                return sum(r)
        

    def print_matrix(self):
        for i in self.matrix:
            print(f" {i} \n")
    


def main():
    game = game_2048()
    score = 0
    moves = [0,1,2,3,1,3,3,3,2,1,2,3,2,2,1,1,1,2,3,1,0,0,2,1,2]

    for move in moves:
        reward = game.run(move)
        score += reward
        print(f"Move: {move}, Reward: {reward}")
        print(game.matrix)  
        print("---------------------------------------------")

    print(f"Total score: {score}")

if __name__ == "__main__":
    main()



                


