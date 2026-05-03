import pickle

data = {"name": "Peter", "course": "Python", "participant": 12}

# Save (dump)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Laden (load)
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)
