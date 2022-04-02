begin_remark:  gets all progressive constructions in present, past and future tenses, in indicative, subjunctive, infinitive and imperative modes.
end_remark

define:  me_test3.def
remove_nodes: t
print_indices: t
node:   IP*
query:  ((IP* iDoms be|beperf)	
		AND (IP* iDoms pres_part))