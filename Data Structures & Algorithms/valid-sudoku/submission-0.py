class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ninedict = {}
        for i in range(len(board)):
            rowdic = {}
            for num in board[i]:
                if num!= "." and num not in rowdic:
                    rowdic[num] = 1
                elif num in rowdic:
                    return False
            coldic = {}
            for j in range(len(board)):
                
                if board[j][i] != "." and board[j][i]not in coldic:
                    coldic[board[j][i]] = 1
                elif board[j][i] in coldic:
                    return False
            
       
            # for z in range(len(board))
            #     if (i//3, z//3) in ninedict:
            #         if board[i][j] in ndict[(i//3, z//3)]:
            #             return False
            #     if (i//3, z//3) not in ninedict and board[i][j] != ".":
            #         ninedict[(i//3, z//3)] = []
            #     ninedict[(i//3, z//3)].append(board[i][j])
            for j in range(len(board[i])):  # Inner loop for columns
                # Skip empty cells
                if board[i][j] == ".":
                    continue
                
                # Calculate the key for the 3x3 subgrid
                key = (i // 3, j // 3)
                
                # Initialize the key in ninedict if not already present
                if key not in ninedict:
                    ninedict[key] = []
                
                # Check if the current number already exists in the subgrid
                if board[i][j] in ninedict[key]:
                    return False
                
                # Add the current number to the subgrid
                ninedict[key].append(board[i][j])
                        
                # if board[i//3][z+ i//3]!= "." and board[i//3][z+ i//3] not in (ninedict1 or ninedict2 or ninedict3):
                #     ninedict1[board[i//3][z+ i//3]] = 1
                # elif board[i//3][z+ i//3] in (ninedict1 or ninedict2 or ninedict3):
                #     return False
                # if board[i//3 + 1][z+ i//3]!= "." and board[i//3 + 1][z+ i//3] not in (ninedict1 or ninedict2 or ninedict3):
                #     ninedict2[board[i//3][z+ i//3]] = 1
                # elif board[i//3 + 1][z+ i//3] in (ninedict1 or ninedict2 or ninedict3):
                #     return False
                # if board[i//3 + 2][z+ i//3]!= "." and board[i//3 + 2][z+ i//3]not in (ninedict1 or ninedict2 or ninedict3):
                #     ninedict3[board[i//3][z+ i//3]] = 1
                # elif board[i//3 + 2][z+ i//3] in (ninedict1 or ninedict2 or ninedict3):
                #     return False
        return True

            