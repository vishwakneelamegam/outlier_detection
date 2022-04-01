import math

class outlierDetection:
  def __init__(self,threshold,datas):
    self.threshold = threshold
    self.datas = datas
  def calculateMean(self):
    try:
      sum = 0
      for data in self.datas:
        sum = sum + data
      sum = sum / len(self.datas)
      return sum
    except Exception as e:
      return 0
  def calculateStandardDeviation(self,mean):
    try:
      sum = 0
      for data in self.datas:
        sum = sum + ((data - mean) ** 2)
      return math.sqrt(sum / len(self.datas) - 1)
    except Exception as e:
      return 0
  def detectOutlier(self):
    try:
      outlier = []
      mean = self.calculateMean()
      standardDeviation = self.calculateStandardDeviation(mean)
      for data in self.datas:
        zScore = (data - mean) / standardDeviation
        if abs(zScore) > self.threshold:
          outlier.append(data)
      return outlier
    except Exception as e:
      print(e)
      return []

obj = outlierDetection(3,[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10])
obj.detectOutlier()
