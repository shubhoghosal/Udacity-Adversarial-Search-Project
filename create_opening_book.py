import pickle
from isolation import Isolation
state = Isolation()
my_data = {state: 57}  # opening book always chooses the middle square on an open board
with open("data.pickle", 'wb') as f:
    pickle.dump(my_data, f)