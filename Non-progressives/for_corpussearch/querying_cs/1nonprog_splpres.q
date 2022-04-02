begin_remark: finds all IPs with a simple present form
end_remark

define: me_def_splpresent.def
remove_nodes: t
print_indices: t
node: IP*
query: ((IP* iDoms spl_pres) 
		AND (IP* iDoms !pres_part|pass_part|perf_part))