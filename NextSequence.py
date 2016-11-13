class NextSequence:
    # operation = ["*", "+","-","/","^"]
    sequence = []
    2, 4, 6, 8

    def __init__(self):
        print("Start")

    def ask_sequence(self):
        temp = input("Input your sequence, make sure your numbers are split by ',' with no spaces\n")
        self.sequence = temp.split(",")
        self.sequence = list(map(int, self.sequence))


    def is_multiplication(self, c):
        multiplyer = c[1] / c[0]
        for a in range(1, len(c) - 1):
            if multiplyer != c[a + 1] / c[a]:
                return [False, False]
        return [True,multiplyer]

    def is_addition(self, a):
        factor = a[1] - a[0]
        for b in range(len(a) -1):
            if a[b]+factor != a[b+1]:
                return [False,False]
        return [True , factor]

    def pattern_differenceM(self, b):
        dif_array = []
        for a in range(len(b)-1):
            dif_array.append(b[a+1]-b[a])
        if self.is_multiplication(dif_array)[0]:
            return self.is_multiplication(dif_array)
        return False



    def addition_prev(self,array):
        last_number = 1
        current_sum = 0
        lastElement = array[len(array)-1]
        for i in range(len(array)-2, 0, -1):
            current_sum = current_sum + array[i]
            if current_sum == lastElement:
                second = len(array)-2
                temp_sum = 1
                for j in range(1,last_number+1):
                    temp_sum = temp_sum + (array[len(array)-2-j])
                if(array[len(array)-2] == temp_sum):
                    return [True, last_number]
            last_number = last_number+1
        return[False, False]

    def fucked_up_sequence_1(self):
        last = self.sequence[len(self.sequence)-1]
        second_last = self.sequence[len(self.sequence)-2]

        if self.sequence[len(self.sequence)-3] == last / second_last:
             if self.sequence[len(self.sequence)-4] == self.sequence[len(self.sequence)-2] / self.sequence[len(self.sequence)-3]:
                return True
        return False




    def pattern_differenceA(self, b):
        dif_array = []
        for a in range(len(b) - 1):
            dif_array.append(b[a + 1] - b[a])
        if self.is_addition(dif_array)[0]:
            return self.is_addition(dif_array)
        return False


    def findPattern(self):
        half = len(self.sequence)
        number = self.sequence[half]
        temp1 = self.sequence
        temp1.remove(number)






    def next_value(self):

        if (self.is_multiplication(self.sequence)[0]):
            return int(self.sequence[1] / self.sequence[0] * self.sequence[len(self.sequence)-1])
        if (self.is_addition(self.sequence)[0]):
            return int(self.sequence[1]-self.sequence[0]+ self.sequence[len(self.sequence)-1])
        if self.pattern_differenceA(self.sequence):
            return int(self.sequence[len(self.sequence)-1] - self.sequence[len(self.sequence)-2])+self.pattern_differenceA(self.sequence)[1] + self.sequence[len(self.sequence) -1 ]
        if self.fucked_up_sequence_1():
            return int(self.sequence[len(self.sequence)-12]*self.sequence[len(self.sequence)-2])
        if self.addition_prev(self.sequence)[0]:
            sum = 1;
            for i in range (self.addition_prev(self.sequence)[1]):
                sum = sum + self.sequence[self.sequence[len(self.sequence)]-i]
            return sum



a = NextSequence()
while True:
    a.ask_sequence()


    print ("The Next Number is : " + str(a.next_value()))
