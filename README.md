# NL4DV

**NL4DV** stands for **N**atural **L**anguage toolkit **for** **D**ata **V**isualization. It takes a **natural language query** about a given **dataset** as input and outputs a **structured JSON object** containing:
* Data attributes, 
* Analytic tasks, and
* Visualizations (Vega-Lite specifications)


## Use ##
- Download the jar packages
  - stanford-english-corenlp-2018-10-05-models.jar on https://stanfordnlp.github.io/CoreNLP/download.html
  - stanford-parser.jar on https://nlp.stanford.edu/software/lex-parser.shtml#Download
  - put the two jar files in "jars" folder

- Download the sentence embedding model
  - Universal Sentence Encoder v4 on https://tfhub.dev/google/universal-sentence-encoder/4
  - put the folder in root directory
      
- Running
  - nl4dv/examples
  - python app.py