import spacy
import en_core_web_sm
from graphviz import Digraph
import hashlib

from pprint import pprint

nlp = spacy.load('en_core_web_sm')
entities = dict()

dot = Digraph(comment='The Mueller Report')
ids = dict()




def processChunk(data) :
    doc = nlp(data)

    total = len(doc.ents)
    last = None
    
    for ent in doc.ents:
        label = ent.label_
        text = ent.text
        
        print(text, label)

        #Need to trim down connections
        if (label not in ("ORDINAL", "CARDINAL")) :
            hash_object = hashlib.md5(text.lower().encode('utf-8'))
            hid = hash_object.hexdigest()
                 
            #unique the items
            if hid not in ids :
                dot.node(hid, text, type=label)

            if last != None :
                if last != hid:
                    dot.edge(hid, last)

            ids[hid] = 1
            last = hid
        
        if label not in entities :
            entities[label] = dict()
            entities[label][text] = 0
        else :
            if text not in entities[label] :
                entities[label][text] =0
            else:
                entities[label][text] +=1

     
    
#        if (label == "PERSON") :
#            print(text +" ->")
#            for e in ent.lefts :
#                print("<-"+e.text)
#            for e in ent.rights :
#                print("->"+e.text)
#            pprint(dump(ent))
#            print(ent.head.head)

def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))
                
def printOutCome() :

    f = open("entities.txt", "w")
    for types in entities :
        for ents in entities[types] :
            f.write(types + "|" + ents+"\n")
    f.close()

    f2 = open("mueller.gv", "w")
    f2.write(dot.source+"\n")
    f2.close()
    #dot.render('mueller.gv', view=True)


def main(file) :
    f = open(file, "r",encoding='utf-16-le')
    chunk = 102400
#    while True :
    for i in range(0,10):
        data = f.read(chunk)
        processChunk(data)
        if data == "" :
            break

    printOutCome()


if __name__ == "__main__" :
    main("mueller-report-searchable.txt")
