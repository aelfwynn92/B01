---
title: "README"
author: "I. R. Malta^[Leibniz-Zentrum Allgemeine Sprachwissenschaft, malta@leibniz-zas.de]"
date: "29/03/2022"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

All scripts posted here are meant for linguistic research only. If taken, please reference!
  
  
## 1. The author

Izabella Rosa Malta is a doctoral researcher in the SFB project Register and the development of periphrasis in the history of English (SFB Register B01) and in the Research Area 3 ‘Syntax & Lexicon’.

Her PhD dissertation examines the alternation between the periphrastic progressive form with its synthetic counterpart in the transitional period between Middle English and Early Modern English (ca. 14-16th centuries) to shed light on what the profile of specific changes can tell about register knowledge. The research is under the scope of Project B01 of SFB1412.

More [here](https://sfb1412.hu-berlin.de/projects/b01/).

\----
  
## 2. Data
  
For the sake of research on the alternation between progressive (periphrastic) and non-progressive (simple forms) constructions, I consider here these two main groups and their respective files inside folders with the same labels. Within each one, the files were organised as shown below.   

### 2.1. Aliases and CorpusSearch command line in GitBash

In order to facilitate queries in [CorpusSearch](http://corpussearch.sourceforge.net/CS.html)/[PPCME2](https://www.ling.upenn.edu/hist-corpora/PPCME2-RELEASE-4/index.html) through a command line in GitBash, I wrote scripts in Python for creating aliases.    
  
The aliases can be used to query inside any folder for Text type, Period, Period within Text type, and Period within Text type without Religious Treatise (me13g9p). I provide the scripts in Python with their output .txt files, which consist of lists to be copied to the dotbashrc file through command **nano .bashrc** in Windows 10.   
    
**Alias-creator script for Text types:** "aliases_dotbashrc_genres.py"   
**Output (Text types alias list):** aliases_dotbashrc_genres.txt"   
**Alias-creator script for Periods:** "aliases_dotbashrc_periods.py"  
**Output (Periods alias list):** "aliases_dotbashrc_periods.txt"    
**Alias-creator script for Periods within Text types:** "aliases_dotbashrc_periods-within-genres.py"    
**Output (Periods within Text types alias list):** "aliases_dotbashrc_periods-within-genres.txt"  
**Alias-creator script for Periods and Text types without reltreat:** "aliases_dotbashrc_me13g-9p_v2.py"  
**Output (Periods within Text types withour reltreat alias list):** "aliases_dotbashrc_me13g-9p_v2.txt"
  
### 2.2. CorpusSearch (Randall, 2005)
  
.q files: To be run in the entire corpus folder through GitBash (for Windows 10). Catches specific dependency structures. Returns a .out file.    
.out files:  .q file's output. Shows all sentences with the following information: Middle English text excerpt, text ID, sentence ID and dependency structure.   
.c files: Coding queries to be run on the .out file. Add a CODING-IP* line in each retrieved sentence with tags. The tags are specified in layers: TAM (Tense, Aspect and Mode), Origin (Germanic, Romance, Blended, CONJ), Word length (1, 1half, 2, 2half, 3, 3half, 4 and so on) and Transitivity (transitive, intransitive, prep_intransitive, ambiguous). Returns a .out file.   
.cod file: .cod file's output.    
.cod.ooo files: Whenever I run a specific .c file ("find_coding_ip.c"), I get only the CODING-IP* lines printed. Useful for creating dataframes.   
.def files: List of Parts-of-Speech tags (to define .q file) and list of Middle English forms assigned to lemmas (to define .c file).   

### 2.3. CorpusSearch lexica

**Progressives .q file:** verblex4.q    
**Progressives .out file:** verblex.out   
**Non-progressives .q files:** verblex_present.q, verblex_past.q, verblex_perfect.q, verblex_infinitive.q, verblex_imperative.q   
**Non-progressives .out files:** verblex_present.out, verblex_past.out, verblex_perfect.out, verblex_infinitive.out, verblex_imperative.out   

The .out file has been converted to .xlsx, where I insert classification into origin and word length.     
  
For Progressives: verblex4_lemma.xlsx.    
For Non-progressives, .xlsx files: “verblex_imperative.xlsx”, “verblex_infinitive.xlsx”, “verblex_past.xlsx”, “verblex_perfect.xlsx”, and “verblex_present.xlsx”.   
  
### 2.4. Scripts in Python to create .def files

To optimise work on .def files, I wrote the following scripts in Python:

### For Progressives

**Form-lemma assignment script:** me_form_lemma4.py   
**Output:** my_lemma_file4.txt (then saved as lex-all.def)    
**Lemma list by origin:** prog_origin_layers.py    
**Output:** prog_origin_layers.txt (to be copied to .c file in layer 2)    
**Lemma list by word length:** prog_wordlength_layers.py    
**Output:** prog_wordlength_layers (to be copied to .c file in layer 3)    
**LOCATION:** Progressives/form_lemma_origin_wordlength

### For Non-progressives

**Sample (simple present):** Sample from what I have so far in verblex_present.xlsx. Will not be useful when I have this spreadsheet finished. Files were probably based on older version nonprog_lemmas_sample.py.  
**Sample of Germanic verbs:** nonprog_lemmas_sample_GER.py    
**Output:** nonprog_lemmas_sample_GER.txt   
**Sample of Romance verbs:** nonprog_lemmas_sample_ROM.py   
**Output:** nonprog_lemmas_sample_ROM.txt   
Both .txt files had their content copied to the .def and .c files in layers 2 and 3, respectively.  
**LOCATION:** Non-proggressives/SAMPLE_splpres_origin

**Form-lemma assignment script:** nonprog_present_me_form_lemma.py    
**Output:** nonprog_present_my_lemma_file.txt (then saved as nonprog-lex-all.def)   
**Lemma list by origin:** nonprog_present_origin-layers1.py     
**Output:** SAMPLE_nonprog_present_origin_layers.txt (to be copied to .c file in layer 2)   
**Lemma list by word length:** nonprog_present_wordlength-layers1.py    
**Output:** SAMPLE_nonprog_present_wordlength_layers.txt (to be copied to .c file in layer 3)   
**LOCATION:** Non-progressives/form_lemma_origin_wordlength   
