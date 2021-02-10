import pomegranate as pm
import numpy as np
from Bio import SeqIO

coding_probas = pm.DiscreteDistribution({'A' : 0.35, 'C' : 0.20, 'G' : 0.05, 'T' : 0.40})
non_coding_probas = pm.DiscreteDistribution({'A' : 0.10, 'C' : 0.40, 'G' : 0.40, 'T' : 0.10})

coding = pm.State(coding_probas, name='coding')
non_coding = pm.State(non_coding_probas, name='non_coding')

model = pm.HiddenMarkovModel()
model.add_states([coding, non_coding])
model.add_transition(model.start, non_coding, 0.90)
model.add_transition(model.start, coding, 0.10)

model.add_transition(coding, non_coding, 0.7)
model.add_transition(non_coding, coding, 0.3)

#model.add_transition(s3, model.end, 0.30)

model.bake()

dna = np.array(list(str(SeqIO.read("ecoli.fasta", "fasta").seq)))

model.fit([dna], algorithm='viterbi')
model.plot()

with open('ex.txt', 'w') as file:
    file.write(str(model.predict(dna)))