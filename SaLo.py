#Import to Module
import pickle

#Function
def save(object, namefile="dump.p"):
	pickle.dump(object, open(namefile, "wb"))

def load(object, namefile):
	object = pickle.load(open(namefile, "rb"))


	