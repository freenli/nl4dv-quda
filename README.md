# NL4DV-Quda

**NL4DV-Quda** is a refined version of **NL4DV** where the task inference module is replaced by a neural network trained on Quda.

As a result, NL4DV-Quda is more robust in task classification and extends NL4DV to a broader range of usage scenarios.

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