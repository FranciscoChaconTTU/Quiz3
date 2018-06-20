# Quiz3
def dot(vector01,vector02):
  if len(vector01)==len(vector02):
    x = 0
    for i in range(vector01):
      for j in range(vector02):
        x+=[i]*[j]
      return x
  else:
    return "invalid input"

vector01=(1,2,3)
vector02=(4,5,6)

#print (dot(vector01,vector02))

def vecSubtract(vector01,vector02):
  if len(vector01[0])==len(vector02[0]):
    x = []
    for i in range(vector01):
      for j in range(vector02):
        x.append([i]-[j])    
      return x
  else:
    return "invalid input"

vector01=[1,2,3]
vector02=[4,5]

print (vecSubtract(vector01,vector02))
