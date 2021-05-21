#TASK A

# Define independent probabilities
fair = 0.9
nofair = 1-fair
smart = 0.8
nosmart = 1-smart
study = 0.6
nostudy = 1-study

# Define the probability of being prepared given the 
# values of the independent probabilities smart and study.
prep_if_smart = 0.9*study + 0.5*nostudy
noprep_if_smart = 1 - prep_if_smart
prep_if_nosmart = 0.7*study + 0.1*nostudy
noprep_if_nosmart = 1 - prep_if_nosmart

# Define the probability of passing the test
pass_test = (
  0.9*smart*prep_if_smart*fair 
  + 0.1*smart*prep_if_smart*nofair 
  + 0.7*smart*noprep_if_smart*fair 
  + 0.1*smart*noprep_if_smart*nofair 
  + 0.7*nosmart*prep_if_nosmart*fair 
  + 0.1*nosmart*prep_if_nosmart*nofair 
  + 0.2*nosmart*noprep_if_nosmart*fair 
  + 0.1*nosmart*noprep_if_nosmart*nofair
)

print('Probability to pass the test:', pass_test)

# Probabilities with observations
prep_if_study_and_smart = 0.9
noprep_if_study_and_smart = 1 - prep_if_study_and_smart
prep_if_study_and_nosmart = 0.7
noprep_if_study_and_nosmart = 1 - prep_if_study_and_nosmart

# First define the probability of passing the test if studying
pass_if_study = (
    0.9*smart*prep_if_study_and_smart*fair 
    + 0.1*smart*prep_if_study_and_smart*nofair 
    + 0.7*smart*noprep_if_study_and_smart*fair 
    + 0.1*smart*noprep_if_study_and_smart*nofair 
    + 0.7*nosmart*prep_if_study_and_nosmart*fair 
    + 0.1*nosmart*prep_if_study_and_nosmart*nofair 
    + 0.2*nosmart*noprep_if_study_and_nosmart*fair 
    + 0.1*nosmart*noprep_if_study_and_nosmart*nofair
)

# Then use Bayes theorem to find the reverse probability;
# the probability of having studied if passing the test
study_if_passed = (pass_if_study*study)/pass_test

print('Probability of having studied if passing the test:', study_if_passed)