import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **karg):
        self.contents = []
        for key, value in karg.items():
            self.contents += [key] * value

    def draw(self,number):


        if number>len(self.contents):
            return self.contents
        else:
            drawn_balls = []
            for i in range(number):
                random_ball = random.choice(self.contents)
                
                drawn_balls.append(random_ball)
                self.contents.remove(random_ball)
            return drawn_balls

    def draw_exp(self,number):
        all_balls = copy.deepcopy(self.contents)
        if number>len(self.contents):
            return self.contents
        else:
            drawn_balls = random.sample(all_balls,number)
            
            return drawn_balls


def check(drawn_balls,exp_balls):
  c_drawn_balls = copy.deepcopy(drawn_balls)
  print('test')
  for i in range(len(exp_balls)):
    try:
      c_drawn_balls.remove(exp_balls[i])
      print('removing: '+str(exp_balls[i]))
    except:
      return False
    
  return True
    

    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    exp_balls = []
    m=0
    for key, value in expected_balls.items():
            exp_balls += [key] * value
    #print(exp_balls)
    for i in range(num_experiments):
        
        drawn_balls = hat.draw_exp(num_balls_drawn)
        

        if check(drawn_balls,exp_balls)== True:
          m+=1
          print(drawn_balls,exp_balls)
        

    print('num of exp: ' +str(num_experiments) + 'num of trues' + str(m))
    return m/num_experiments
