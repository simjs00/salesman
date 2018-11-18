import model
import helpers
import numpy as np
import pickle
import sys
import spacy

vocabs = set()
file = open("./training/"+"vocabs.pickle",'rb')
vocabs = list(pickle.load(file))
file.close()
model.saver.restore(model.sess, "./model/model.ckpt")
nlp = spacy.load('en_core_web_sm')

def get_word(ind) :
	return vocabs[ind] 
def get_index(word):
		word = word.replace("\n", "")
		word = word.lower()
		if(word!="") :
				if(word in vocabs) :
					i = vocabs.index(word)
					return i
		return -1

def print_testing() :
		data,data2 = helpers.get_data("./training/")
		fd = process(data,data2)
		predict= model.sess.run(model.decoder_prediction, fd)

		for j, (inp, pred,out) in enumerate(zip(fd[model.encoder_inputs].T, predict.T,fd[model.decoder_targets].T)):
			# print ("input {} : ".format(inp))
			# print ("predict {} : ".format(pred))
			# print ("out {} : ".format(out))
			print '\n'
			print "input"
			print(inp)
			for data in inp :
					if( data-2>=0	and data-2<257):
						sys.stdout.write(get_word(data-2)+" ")
						sys.stdout.flush()
			
			print '\n'
			print "predict"
			print(pred)
			for data in pred :
					if( data-2>=0 and data-2<257):
						sys.stdout.write(get_word(data-2)+" ")
						sys.stdout.flush()

			
			print '\n'
			print "target"
			print(out)
			for data in out :
					if( data-2>=0	and data-2<257):
						sys.stdout.write(get_word(data-2)+" ")
						sys.stdout.flush()

	
def process(input_val,output_val):
    encoder_inputs_, _ = helpers.batch(input_val,50)
    decoder_targets_, _ =helpers.batch(output_val,50)
    return {
        model.encoder_inputs: encoder_inputs_,
        model.encoder_inputs_length: np.full(len(input_val),50),
    	model.decoder_targets: decoder_targets_,
    }

def process_ori(input_val):
    encoder_inputs_, _ = helpers.batch(input_val,50)
    return {
        model.encoder_inputs: encoder_inputs_,
        model.encoder_inputs_length: np.full(len(input_val),50),
    }

def get_answer(question) :
	results_token =nlp(u""+question)
	results =[]
	for i,data in enumerate(results_token) :
		results.append(data.text)
	data=[[]]
	for val in results :
		i = get_index(val)
		if(i!=-1) :
			data[0].append(i+2)
	fd = process_ori(data)
	predict= model.sess.run(model.decoder_prediction, fd)
	answer = ""
	for j, pred in enumerate(predict.T):
		for k,data in enumerate(pred) :
			if( data-2>=0 and data-2<257):
					if(k<len(pred)-1) :
						answer += get_word(data-2)+ " "
					elif(k==len(pred)-1) :
						answer += get_word(data-2)
	#final_output = []
	#count = answer.count(" . ")
	# if(count > 0 ) :
	# 	new_str = answer.split(" . ")
	# 	for ans in new_str :
	# 		final_output.append(ans)
	# else :
	#final_output.append(answer)

	return answer
