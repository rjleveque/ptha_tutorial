
from pylab import *
from IPython.display import Markdown, Latex

msg1 = 'Set p_hat in the cell above and then hit Shift-Enter to check.\n\n' + \
       'Or set p_hat to "??" for the correct answer and explanation.'

msg2 = 'Your answer is correct!  \n\n'
msg3 = 'Sorry, that is not correct.\n\n'
msg4 = 'The correct answer is:\n\n'

def check_answer1(p_hat):
    p_hat_correct = 1 - (1-0.2)*(1-0.4)*(1-0.6)
    msg_solution = "This can be computed as `p_hat = 1 - (1-0.2)*(1-0.4)*(1-0.6).`"
    msg_correct = "     `p_hat = %g`\n\n" % p_hat_correct
    if p_hat == "??":
        msg = Markdown(msg4 + msg_correct + msg_solution)
        #print msg4 + msg_correct + msg_solution
    elif p_hat == "?":
        msg = Markdown(msg1)
    elif p_hat == p_hat_correct:
        msg = Markdown(msg2 + msg_correct + msg_solution)
    else:
        msg = Markdown(msg3 + msg1)
    return msg

def check_answer2(p_hat):
    p_hat_correct = 1 - (1-0.002)**7
    msg_solution = "Since 7 of the 10 events give flooding above 1.5 m, \n\n" + \
        "the correct value can be computed as `p_hat = 1 - (1-0.002)**7`."
    msg_correct = "     `p_hat = %g`\n\n" % p_hat_correct
    if p_hat == "??":
        msg = Markdown(msg4 + msg_correct + msg_solution)
        #print msg4 + msg_correct + msg_solution
    elif p_hat == "?":
        msg = Markdown(msg1)
    elif abs(p_hat - p_hat_correct) < 3e-5:
        msg = Markdown(msg2 + msg_correct + msg_solution)
    elif abs(p_hat - p_hat_correct) < 0.002:
        msg_close = 'Good estimate -- your value is close to correct. \n\n' +\
            'Can you figure out how to compute it exactly?\n\n'
        msg = Markdown(msg_close + msg1)
    else:
        msg = Markdown(msg3 + msg1)
    return msg
