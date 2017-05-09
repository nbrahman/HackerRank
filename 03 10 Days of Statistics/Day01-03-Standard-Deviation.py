from math import sqrt

class StandardDeviation(object):
    def calculateMean (self,x,d):
        return round(sum(x)/len(x),d)

    def calculateStandardDeviation(self,x,d):
        m=self.calculateMean(x,d)
        for i in range(len(x)):
            x[i]=(x[i]-m)**2
        print (round(sqrt(self.calculateMean(x,d)),d))


if __name__ == '__main__':
    n = input().strip()
    n = int(n)
    x = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    m = StandardDeviation()
    m.calculateStandardDeviation(x,1)