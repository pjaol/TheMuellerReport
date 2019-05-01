# The Mueller Report NLP #

Using Spacy from <https://spacy.io>
Take the searchable report from CNN <https://cdn.cnn.com/cnn/2019/images/04/18/mueller-report-searchable.pdf>
Extract the text, I used Mac Automator but PDFBox or other tools will provide the same capability.
There are 2 output files
* entities.txt is a pipe delimited list of entites and types
 * Type| Label
 * ORG|Department of Justice
* <https://github.com/pjaol/TheMuellerReport/blob/master/entities.txt>

The second output is a graphviz dot file connecting all the entities based on position and enumeration
It's a big file 1.x MB <https://github.com/pjaol/TheMuellerReport/blob/master/mueller.gv>

To view this file I use a tool called Gephi
<https://gephi.org>

I've included the Gephi output <https://github.com/pjaol/TheMuellerReport/blob/master/mueller_gephi.gephi>
Which you should be able to just load up and play with.

There's over 5K entities and 21K edges producing a messy graph, to gain any insight you have to play with 
Gephi layouts
* Enable labels
* Layout >  Noverlap and Expansion
* Appearence > Nodes > Size > Ranking > Degree
* Appearence > Nodes > Color > Ranking > Degree

![Mueller Report Graph](https://raw.githubusercontent.com/pjaol/TheMuellerReport/master/screenshot_073400.png)


## ToDo ##
The number of items is overwhelming I'd like to do the following 
* Partition based on sub-networks
* Convert Events to Edges if connecting Orgs or People


## Caveats ##
Nothing in life is simple, given the size of the report you have to 
decide how to read it in chunks. I select byte size chunks vs say paragraphs. 
It's possible / probable that something will get missed but given the scanned quality of the document you've got other issues to worry about.

