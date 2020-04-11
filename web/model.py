from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

loadModel = load_model("model/SMS_Fraud2.hdf5")

def cek(xxx):
	txt = [xxx]
	labels = ['promo', 'penipuan', 'normal',]
	tokenizer = Tokenizer(num_words=1000, oov_token=True)
	tokenizer.fit_on_texts(txt)
	seq = tokenizer.texts_to_sequences(txt)	
	padded = pad_sequences(seq, maxlen=max_length)
	pred = loadModel.predict(padded)
	result = labels[np.argmax(pred)]
	return result