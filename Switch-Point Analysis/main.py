import matplotlib.pyplot as plt
import pandas as pd
import ruptures as rpt
import rpt_rewrite


'''
# generate signal
n_samples, dim, sigma = 1000, 3, 4
n_bkps = 4  # number of breakpoints
signal, bkps = rpt.pw_constant(n_samples, dim, n_bkps, noise_std=sigma)
'''


#data = pd.read_csv('data.csv', usecols=['Trial', 'Fix_X', 'Fix_Y', 'SceneFix'], nrows = 500)
data = pd.read_csv('data_exploit.csv', usecols=['Trial', 'Fix_X', 'Fix_Y', 'SceneFix', 'ParticipantID'])
data = data[data['ParticipantID'] == 9]
data = data.drop(columns=['ParticipantID'])


trialData = data['Trial'].to_numpy()
trialData.tolist()
trialMarkers = []
counter = 0

for i in range(1, len(trialData)):
    curTrial = trialData[i]
    prevTrial = trialData[i - 1]
    if curTrial > prevTrial:
        trialMarkers.append(counter)
    counter += 1


data.set_index("Trial", inplace=True)
data = data.sort_index()

print(data)

test = data.values.reshape(-1, 3)

algo = rpt.Pelt(model="l2", min_size=28)
algo.fit(test)
result = algo.predict(pen=1)

output = rpt_rewrite.display(test,result, trialMarkers)
plt.xlabel("Fixation #")
plt.suptitle("PID: 9", fontsize=24)
plt.tight_layout()
plt.text(10, 10, "test")
plt.show()

print(result)
