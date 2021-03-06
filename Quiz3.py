import math
def dot(vector01,vector02):
  "This fuction takes in two vectors and first checks if they are lists. Then it checks if they are of the same dimensions. Then if they are of the same dimensions it multiplies the elements in the same positions and adds them at the end. If they are not of the same dimensions it return invalid input."
  #These lines are to check to see if its not a list
  if type(vector01) != list or type(vector02) != list:
    print ("invalid input")
    return False
  if len(vector01)==0 or len(vector02)==0:
    print ("invalid input")  
    return False
  #This line is to check if the dimensions of my vectors are the same
  if len(vector01)==len(vector02):
    x = 0
    #If the dimensions are the same go ahead and do the multiplication of each element
    for i in range(len(vector01)):
      #After the multiplication we are adding it to x and giving us the answer at the end as a scalar
      x+=vector01[i]*vector02[i]
    return x
  #If the dimensions are different print invalid input and return none
  else:
    print ("invalid input")
    return None

#Valid Case Test
vector01=[1,2,3]
vector02=[4,5,6]
print (dot(vector01,vector02))

#Invalid Case Test
vector011=[1,2,3]
vector022=[4,5]
#print (dot(vector011,vector022))

def vecSubtract(vector03,vector04):
  "This fuction takes in two vector of the same dimension and subtracts them. First in checks if the dimension are the same, if they aren't it prints invalid input. If they are the same dimension it takes the first element of the first vector and the first element of the second vector and stores it on a blank matrix. It keeps doing this for all elements in the vector"
  #This line is checking the dimensions of the two vectors
  if len(vector03)==len(vector04):
    x = []
    #This line is taking the elements of vector one and subtracting vector two elements respectively 
    for i in range(len(vector03)):
      #This line takes in the subtraction and stores them to the blank matrix to retunr a vector
        x.append(vector03[i]-vector04[i])    
    return x
    #This line is to print invalid input if the dimensions aren't the same
  else:
    print("invalid input")
    return None

#Valid Case Test
vector03=[1,2,3]
vector04=[4,5,6]
print (vecSubtract(vector03,vector04))

#Invalid Case Test
vector033=[1,2,3]
vector044=[4,5]
#print (vecSubtract(vector033,vector044))

def scalarVecMulti(scalar01,vector05):
  "This fuction takes in a scalar and multiplies it with a vector. First in takes the lenght of the vector and multiplies the first element of the vector to the scalar and it stores it to the blank list. Then it does this for all elements and returns a vector."
  x=[]
  #This line checks the dimensions of the vector 
  for i in range(len(vector05)):
    #This lines takes the elements of the vector and multiplies if by the scalar respectively and stores it into a blank list.
    x.append(scalar01*vector05[i])
    #This line returns the vector
  return x

#Valid Case Test
scalar01=10
vector05=[1,2,3]
print (scalarVecMulti(scalar01,vector05))

#Invalid Case Test
scalar011= "Hello"
vector055=[1,2,3]
#print (scalarVecMulti(scalar011,vector055))

def infNorm(vector06):
  "This fuction is to take the max of a vector. This goes through each element and takes the greater magnitude in of the vector. Therefore it takes the absolute value of each element and sees which one is greater. If the element is lower it keeps the previous one. Then it returns the max element of the vector as a scalar"
  x=0
  #This line takes the lenghta of teh vector
  for i in range(len(vector06)):
    #This line takes the absolute value of all elements in the vector and takes the greater one, if its lower it takes the previous one.
    if abs(vector06[i]) > x:
      #This line takes the greater element and replaces it with x
      x= abs(vector06[i]) 
  #This line returns a scalar
  return x

#Valid Case Test
vector06=[1,2,3,4,-5]
print (infNorm(vector06))

#Invalid Case Test
vector066="Hi"
#print (infNorm(vector066))

def normalize(vector07):
  "This function takes the max of a vector. This is similar to question 4. The only difference is that this fuction calls function 4 and divides every element in the vector by its max. We use the infNorm to calculate the max value. This fuction returns a vector"
  #This line is used to called the infNorm that we used before
  x=infNorm(vector07)
  y=[]
  #This line takes the dimension of the vector
  for i in range(len(vector07)):
    #This line takes the division of each element by the max magnitude and stores it to the blank list
    y.append(vector07[i]/x)
    #This line returns a vector with the division
  return (y)

#Valid Case Test
vector07=[3,4,5]
print (normalize(vector07))

#Invalid Case Test
vector077="Hi"
#print (normalize(vector077))
