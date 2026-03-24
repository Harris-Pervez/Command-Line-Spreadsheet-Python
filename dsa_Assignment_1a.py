#===================================
#===================================
#===================================
#===================================

class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selection = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        
        
        #======================
        # Helper Function 
    def helper(self,row,col):
        if (row>=0 and row<self.rows) and (col>=0 and col<self.cols):
            return True
        return False
        
#======================
    def CreateSheet(self, rows, cols):
        '''
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.
 
        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet
        
        Return value:
            None
        '''
        self.rows=rows
        self.cols=cols
        self.sheet=[]
        for row in range(rows):
            sub_sheet=[]
            for col in range(cols):
                sub_sheet.append(None)
            self.sheet.append(sub_sheet)
            
#======================

#======================
    def Goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''
        if self.helper(row,col):
            self.cursor=[row,col]
        else:
            print("Invalid postion !")
#======================

#======================        
    def Insert(self, val):
        '''
        Inserts value at the position indicated by the cursor.
 
        Parameters:
            val --> value to be inserted at the cursor location
        
        Return value:
            None
        '''
        self.sheet[self.cursor[0]][self.cursor[1]]=val
    
#======================

#======================        
    def Delete(self):
        '''
        Deletes a value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            None
        '''

        self.sheet[self.cursor[0]][self.cursor[1]]=None
#======================

#======================    
    def ReadVal(self):
        '''
        Prints the value from the position indicated by the cursor.
 
        Parameters:
            None
        
        Return value:
            value stored at the cursor location 

        '''
        loc=self.sheet[self.cursor[0]][self.cursor[1]]
        print(loc)
        
        return loc
#======================

#======================    
    def Select(self,row, col):   
        '''
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor
 
        Parameters:
            row --> Row number to be selected 
            col --> Column number to be selected
        
        Return value:
            None
        '''
        if self.helper(row,col):
            r1, c1 = self.cursor
            r2, c2 = row, col

            self.selection = [
                min(r1, r2),
                min(c1, c2),
                max(r1, r2),
                max(c1, c2)
            ]
        else:
            print("Invalid position !")
#======================

#======================        
    def GetSelection(self):
        '''
        Returns a tuple with current selecion cooridnates
        Parameters:
            None
        
        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection
            
            Example: (1,1,3,4)
        '''
        return tuple(self.selection)
        
#======================

#======================        
    def Sum(self,row,col):
        '''
        Stores the sum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum
        
        Return value:
            None
        '''
        if self.helper(row,col):    
            sum_var=0
            for ro in range(self.selection[0],self.selection[2]+1):
                for co in range(self.selection[1],self.selection[3]+1):
                    if self.sheet[ro][co] is not None:
                        sum_var+=self.sheet[ro][co]
            if sum_var!=0:
                self.sheet[row][col]=sum_var
        else:
            print('Invalid Position !')
#======================

#======================    
    def Mul(self,row,col):
        '''
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product
        
        Return value:
            None
        '''  
        if self.helper(row,col):
            mul_var=1
            for ro in range(self.selection[0],self.selection[2]+1):
                for co in range(self.selection[1],self.selection[3]+1):
                    if self.sheet[ro][co] is not None:
                        mul_var*=self.sheet[ro][co]
            if mul_var!=1:           
                self.sheet[row][col]=mul_var 
        else:
            print('Invalid position !')

#======================

#======================        
    def Avg(self,row,col):
        '''
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average
        
        Return value:
            None
        '''
        if self.helper(row,col):
            sum_var=0
            count=0
            
            for ro in range(self.selection[0],self.selection[2]+1):
                for co in range(self.selection[1],self.selection[3]+1):
                    if self.sheet[ro][co] is not None:
                        sum_var+=self.sheet[ro][co]
                        count+=1
            try:
                avg=sum_var/count        
                self.sheet[row][col]=avg
            except:
                pass   
        else:
            print('Invalid position !')
#======================

#======================
    def Max(self,row, col):
        '''
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum
        
        Return value:
            None
        '''
        if self.helper(row,col):    
            max_var=0
            for ro in range(self.selection[0],self.selection[2]+1):
                for co in range(self.selection[1],self.selection[3]+1):
                    if self.sheet[ro][co] is not None:
                        if self.sheet[ro][co]>max_var:
                            max_var=self.sheet[ro][co]
            if max_var!=0:
                self.sheet[row][col]=max_var
        else:
            print('Invalid position !')        
#======================
#======================
    def PrintSheet(self):
        '''
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None    

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0       
            1   
            2           10               
            3                   12
            4 
        '''
        print("\nPrintSheet()\n")
        print("row/col:", end="\t")
        for c in range(self.cols):
            print(c, end="\t")
        print()

        for r in range(self.rows):
            print(r, ":\t\t", end="")
            for c in range(self.cols):
                val = self.sheet[r][c]
                print(val if val is not None else "-", end="\t")
            print()
        
#====================== 
#======================
#======================
#    BONUS
#======================
    
    def Undo(self):
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
              
        
        raise NotImplementedError

#----------------------

    def Redo(self):
        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        raise NotImplementedError
                
                
#======================
#======================
#======================
# 
#
#
#    DRIVER FUNCTION
#
#======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    print("Welcome to DS SpreadSheet Program")
    com=input("Enter Command prompt : ").split()
    if com[0]=="CreateSheet":
        sheet = Spreadsheet()
        sheet.CreateSheet(int(com[1]),int(com[2]))
        print("Sheet successfully created !")
        while True:
            cmd=input(">>").lower().split()
            try:
                if cmd[0]=="quit":
                    break
                elif cmd[0]=="goto":
                    sheet.Goto(int(cmd[1]),int(cmd[2]))
                elif cmd[0]=="insert":
                    sheet.Insert(int(cmd[1]))
                elif cmd[0]=="readval":
                    sheet.ReadVal()
                elif cmd[0]=="delete":
                    sheet.Delete()
                elif cmd[0]=="select":
                    sheet.Select(int(cmd[1]),int(cmd[2]))
                elif cmd[0]=="getselection":
                    print(sheet.GetSelection())
                elif cmd[0]=="sum":
                    sheet.Sum(int(cmd[1]),int(cmd[2]))
                elif cmd[0]=="mul":
                    sheet.Mul(int(cmd[1]),int(cmd[2]))
                elif cmd[0]=="avg":
                    sheet.Avg(int(cmd[1]),int(cmd[2]))
                elif cmd[0]=="max":
                    sheet.Max(int(cmd[1]),int(cmd[2]))
                elif cmd[0]=="printsheet":
                    sheet.PrintSheet()
                else:
                    print('Not a Recogonizable command !')
                    
            except:
                print("You might have write some wrong command !")
                pass
    else:
        print("Please! Enter a valid command to create the spreedsheet")
            
            
        
if __name__ == '__main__':
    main()
    
#======================


