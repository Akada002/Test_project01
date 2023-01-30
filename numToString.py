'''The numToString is class that has a function int2str which converts a number to word format string'''


class numToString:
    def int2str(self,num):
        
        '''To convert integer to a string format
        Takes a number and prints it in a word format. 
        Parameters:
        arg1(num): integer 
  
        Returns:
        string: word format of integer

        Limitations:
        executes values from -10**12 to 10**12
        
        For example:
        if num = 5
        >>> "five"
        if num = 55
        >>> "fifty-five"
        '''
        
        num_dict = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty',
            30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety'
        }
        if abs(num)>10**12:
            raise ValueError('invalid num')

        if num <0:
        # Find value of positive counterpart and add negative to the result
            return 'Negative '+self.int2str(num*-1)
        # checking if the number is positive and less than 20
        elif num<=20:
            return num_dict[num]
            
        elif num <100:
        #checking the number if it exists in the num_dict dictionary    
            if num_dict.get(num):   
                return num_dict[num]
        #if the number isn't found in the dictionary the below code is executed        
            else:                   
            
                i=10
        #the number is split into hundreds and last two digits(ten's and one's) and sent to this function recursively
                return num_dict[(num//i)*i] +'-'+ self.int2str(num%i)
        
        #checking if the number is less than 10**3 and if it is, then splitting it and calling this function recursively
        elif num < 10**3: 
            i=100
            if num%i!=0:
        #check if the num percentile of 100 is not equal to zero
                return num_dict[(num//i)] +' hundred and '+ self.int2str(num%i)
            else:
                return num_dict[(num//i)] +' hundred '
                
        #checking if the number is less than 10**6 and if it is, then splitting it into thousands and calling this function recursively
        elif num < 10**6:
            i=10**3
            if num%i!=0:
                return self.int2str(num//i) +' thousand ' +self.int2str(num%i)
            else:
                return self.int2str(num//i) +' thousand '
        
        #checking if the number is less than 10**9 and if it is, then splitting it into millions and calling this function recursively
        elif num < 10**9:
            i=10**6
            if num%i!=0:
                return self.int2str(num//i) +' million ' +self.int2str(num%i)
            else:
                return self.int2str(num//i) +' million '
        
        #checking if the number is less than 10**12 and if it is, then splitting it into billions and calling this function recursively
        elif num < 10**12:
            i=10**9
            if num%i!=0:
                return self.int2str(num//i) +' billion ' +self.int2str(num%i)
            else:
                return self.int2str(num//i) +' billion '
        
        # If input number is not in the boundaries i.e (-10**12,10**12) return below message
        else:
            raise  ValueError('Invalid number')



# print(numToString().int2str(-1000111000111111111111))
#edit