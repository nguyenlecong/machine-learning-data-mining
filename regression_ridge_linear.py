import matplotlib.pyplot as plt 
import numpy as np

# only training set
# D = {(4,3),(7,4),(9,6)} 
'''  
# x values 
x = [4.0,7.0,9.0]  
# y values 
y = [3.0,4.0,6.0] 
'''

# training (2) testing (8) sets  
# x values 
x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0] 
# y values 
y = [2.0,4.0,5.0,7.0,6.0,8.0,9.0,11.0,12.0,12.0]



'''
Ridge linear regression model
f(x;w) = xw+b
L(D)=sum(f(x;w)-y)**2+lamda*(w**2)
First-order optimization condition
L'(D) = 0
'''
lamb = 2 # lambda: 0 -> +inf
tr_size = 2 # training size

def obj_function(w,b):
 of = 0.0
 for i in range(len(x)):
  of += (w*x[i]+b-y[i])*(w*x[i]+b-y[i]) # +lamb*w*w
 return of
			
# first order condition 
def first_order(train_size):
 w_opt = 0.0# (term_4 - term_3)/(term_1 - term_2 + lambda) 
 b_opt = 0.0# 
 
 mean_x = 0.0 #mean(x) 
 mean_y = 0.0 #mean(y)
 for i in range(train_size):
  mean_x += x[i]
  mean_y += y[i]
 mean_x /= len(x)
 mean_y /= len(y)
 #print(mean_x, mean_y)
 term_1 = 0.0 #x**2
 term_2 = 0.0 #x*mean(x)
 term_3 = 0.0 #x*mean(y)
 term_4 = 0.0 #x*y
 for i in range(train_size):
  term_1 += x[i]**2
  term_2 += x[i]*mean_x
  term_3 += x[i]*mean_y
  term_4 += x[i]*y[i]
 #print(term_1,term_2,term_3,term_4)
 w_opt = (term_4 - term_3)/(term_1 - term_2 + lamb) # plus Tikhonov's regularization
 print('w_opt='+str(w_opt)) 
 for i in range(train_size):
  b_opt += y[i] - w_opt*x[i]
 b_opt /= len(x)
 print('b_opt='+str(b_opt))
 return w_opt,b_opt

w_star, b_star = first_order(tr_size) #only two samples

print('w*='+str(w_star))
print('b*='+str(b_star))
print('obj_function='+str(obj_function(w_star,b_star)))
 
# plotting points as a scatter plot 
plt.scatter(x, y, label= "điểm dữ liệu", color= "green",  
            marker= "*", s=15) 
# fx values
fx = np.arange(-1.0, 12, 0.1)
# fy values
fy = fx*0
# fullfill fy
for i in range(len(fx)):
 fy[i] = w_star*fx[i] + b_star # f(x;w)=w*x + b

# potting the points 
plt.plot(fx, fy, label= "hồi quy có nhiễu", color= "red")

# x-axis label 
plt.xlabel('x - trục') 
# frequency label 
plt.ylabel('y - trục') 
# plot title 
plt.title('Đường tuyến tính có nhiễu với lambda = '+str(lamb)) 
# showing legend 
plt.legend() 
  
# function to show the plot 
plt.show() 

