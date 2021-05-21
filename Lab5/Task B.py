#TASK B
fair = 0.9
nofair = 1-fair
smart = 0.8
nosmart = 1-smart
study = 0.0
nostudy = 1-study

prep = 0.9*smart*study + 0.7*nosmart*study + 0.5*smart*nostudy + 0.1*nostudy*nosmart
noprep = 1-prep

print('Probability to be prepared:', prep)

pass_test = 0.9*smart*prep*fair + 0.1*smart*prep*nofair + 0.7*smart*noprep*fair + 0.1*smart*noprep*nofair + 0.7*nosmart*prep*fair + 0.1*nosmart*prep*nofair + 0.2*nosmart*noprep*fair + 0.1*nosmart*noprep*nofair
nopass = 1-pass_test

print('Probability to pass the exam:', pass_test)

