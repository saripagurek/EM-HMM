import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hmmlearn import hmm

n_states = 2

#example, 2 fixations in correct exploit state
test1 = [0, 1, 0, 0, 1, 0, 0, 1, 0]
test2 = [1, 0, 0, 1, 0, 0, 1, 0, 0]

data = []

for i in range(5):
    data.append(test1)
for j in range(7):
    data.append(test2)
for i in range(5):
    data.append(test1)

len_sequences = [5, 7, 5]

model = hmm.CategoricalHMM(n_components=n_states)
model.fit(data, len_sequences)

p = model.predict_proba(data, len_sequences)

print(p)

sns.set_style("whitegrid")
counter = 0
sequence_index = 0
trial = 1
line1_x = []
line1_y = []
line2_x = []
line2_y = []
for h in range(len(p)):
    hidden_state = p[h]
    if hidden_state[0] > hidden_state[1]:
        most_likely = hidden_state[0]
        col = "blue"
        line1_x.append(trial)
        line1_y.append(most_likely)
    else:
        most_likely = hidden_state[1]
        col = "red"
        line2_x.append(trial)
        line2_y.append(most_likely)
    point = [trial, most_likely]
    print("point")
    print(point)
    counter += 1
    if sequence_index < len(len_sequences) - 1:
        if counter > len_sequences[sequence_index]:
            counter = 0
            sequence_index += 1
            trial += 1
plt.plot(line1_x, line1_y, marker="o", markersize=5, markerfacecolor="blue")
plt.plot(line2_x, line2_y, marker="o", markersize=5, markerfacecolor="red")
plt.xlabel('Trial #')
plt.ylabel('p(state)')
plt.title("Exploit or Explore")
plt.legend()
plt.show()


'''
model.startprob_ = state_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

# Define the sequence of observations
observations_sequence = np.array([0, 1, 0, 1, 0, 0]).reshape(-1, 1)
observations_sequence

# Predict the most likely sequence of hidden states
hidden_states = model.predict(observations_sequence)
print("Most likely hidden states:", hidden_states)

log_probability, hidden_states = model.decode(observations_sequence,
                                              lengths=len(observations_sequence),
                                              algorithm='viterbi')

print('Log Probability :', log_probability)
print("Most likely hidden states:", hidden_states)
'''

