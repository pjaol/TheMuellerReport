import spacy
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')



def processChunk(data) :
    doc = nlp(data)
    for ent in doc.ents:
        print(ent.text, ent.label_)




def main(file) :
    f = open(file, "r",encoding='utf-16-le')
    chunk = 102400
    while True :
        data = f.read(chunk)
        processChunk(data)
        if data == "" :
            break



if __name__ == "__main__" :
    main("mueller-report-searchable.txt")
