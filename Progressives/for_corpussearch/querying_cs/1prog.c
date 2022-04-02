define: lex-all.def
node: IP*

coding_query:

1: {
	%presVAG: 	((IP* idoms *BEP*) AND
				(IP* idoms *VAG*|*HAG*|*DAG*))
	%pastVAG: 	((IP* idoms *BED*) AND
				(IP* idoms *VAG*|*HAG*|*DAG*))
	%futVAG:  	(((IP* idoms *MD*) AND
				(IP* idoms *BE*) AND
				(IP* idoms *VAG*|*HAG*|*DAG*)))
	%prsperfVAG: (((IP* idoms *HVP*) AND
				(IP* idoms *BEN*)) AND
				(IP* idoms *VAG*|*HAG*|*DAG*))
	%pstperfVAG: (((IP* idoms *HVD*) AND
				(IP* idoms *BEN*)) AND
				(IP* idoms *VAG*|*HAG*|*DAG*))
	%futperfVAG: (((IP* idoms *MD*) AND
				(IP* idoms *HV*)) AND
				(IP* idoms *BEN*)) AND
				(IP* idoms *VAG*|*HAG*|*DAG*)
	%impVAG:  	((IP* idoms *BEI*) AND
				(IP* idoms *VAG*|*HAG*|*DAG*))
	%infVAG:	((IP* idoms *BE*) AND
				(IP* idoms *VAG*|*HAG*|*DAG*))
	%other1: ELSE
}
2: {
	%CONJ: ((IP* idoms *VAG*|*DAG*|*HAG*) AND 
			(*VAG*|*DAG*|*HAG* idoms CONJ))
	%germanic: (*VAG*|*DAG*|*HAG* idoms ayenstonden|abiden|don1|aken|welden|lasten1|allighten|anbiden|onden1|answeren|arisen|asken|brennen|bakbiten|bithinken|eken|seigen|biginnen|biholden|bihesten|bihoten|benden|bearen|beren|bisechen|bitaken|beaten|ben|bistonden|bidden|gon|biggen|bileven|bireusen|birlen|biten|beteon|blasen|blauen|bleden|blessen|bliken|blissen|leten|blouen|bodien|borien|buwan|breken|bringen|bicomen|bien|binden|callen|casten|sheden|chesen|chiden|clothen|clappen|clensen|clepen|clevien|clouten1|climben|knelen|comen|connen|kerven|creopen|craulen|cursen|kissen|delen|demen|deren|deuen|draggen|dreden|drauen|drien|dremen|drinken|driven|droppen|drouknen|dwellen|cennen|dien|ebben|rennen|eten|liven|wellen|fallen|faren|fasten|fagnen|fighten|feden|felen|feren|fikelen|flen1|flien|fleten|flouen|flitan|falden|folwen|foryeten|forsaken|forbeden|foryeven|fore-sen|forsweren|fresen|ful-filen|fillen|fishen|yernen|geinen|yelden|yellen|yenen|yeven|yongen|yerren|gaderen|galpen|gangen|gapen|gasten|gauren|geten|gladen|glemen|gloen|gliden|glisen|gnasten|gronen|graven1|grennen|greten|grieten|grouen|grimen|girden1|haven|holden1|halwen|halsen1|halsen2|hongen|haten|heien|helden|heren|healen|helpen|herkenen|herien1|listen2|hopien|hungren|whielen|hiden|brainen|irennen|wonen1|kennen|kepen|knouen|knouelechen|leden1|laughen|longen3|louen1|losen|lien1|lenen|leonen|leren|lernen|letten|livien|leaven|lihtnen|liften|lien2|lighten|liken|loken|lokken|longen1|loven2|loven1|louren|louten|leken|makien|melten|menen1|menen2|meten4|milcen|misliken1|mornen|misbileven|neighen|nimen|tholen|todelen|underfon|unknouen|speken|unseien|openen|overrennen|overthrouen|outcasten|plaien|prikien|pullen|putten|pinen|pipen|quaken|quethen|raren|recchen|reden1|rekenen|renten2|resten1|resen1|reven|riusen|riden|risen|rixen|rixlen|rosen|sauen1|seilen|shaken|sechen|shaven|shitten|sheuen|shillen|shimen|shinen|slepen|sithen|seen|semen2|cenden|sengen|*seitten|sowen|shriven|seien|sellen|sinbeten*|singen|slideren|slen|sliden|smaken|smirken|smiten|snakeren|sorwen|souken|sparen|sparklen|spiren1|spreden|springen|spinnen|stonden|staren|sterten|sterven|stiren|stigen|stiken|stinken|stoppen|stormen|streuen|strenen|strengthen|striden|striken|sweren|swinken|swounen|swimmen|siken|thanken|thinken2|theoten|thirsten|threten1|thurghwonen|taken|techen|tithen|tellen|tocomen|toten1|treden|trouen|twiselen|understonden|eilen|fulfillen|unwiten|upberen|upstien|uprisen|wenden|wawen|washen|vaken|walken1|wallen1|wonen2|wanen|wandren|wanten|waxsen|wacchen|weden2|wepen|welcommen|welfaren|venen|warien|werken|werpen|wharven|witen1|weighen|whelen|whirlen|withdrauen|willen1|wilnen|withholden|witnessen|wondren|worshipen|wounden|wrestlen|wreken|wresten|wringen|writen|wishen)
	%romance: (*VAG*|*DAG*|*HAG* idoms accorden|agreen|anoien|appieren|ablen|abreggen|accusen|adden|affermen|alargen|allegen|amblen|amenden|apperen|appreven|ascenden|assaillen|assenten|baptisen|beggen|bitraien|bisegen|blemishen|bobben|boillen|braien|cesen|chalengen|chargen|charmen|chasten|chacen|chaungen|commaunden|comforten|communen|compellen|compleinen|comprehenden|concernen|conceiven|conjuren|consenten|consideren|constreinen|conteinen|continuen|conveien|copulaten|costeien|coveiten|counseilen|counten|crien|citen|dalien|dampnen|declaren|defenden|deliten|departen|despisen|descenden|desiren|destroien|discorden|discoveren|describen|disencresen|dispreisen|disputen|disseveren|douten|dressen|duren|edifien|encheven|enclinen|encresen|encompassen|enfourmen|enjoien|entenden|entren|envirounen|errien|exceden|excusen|executen|exhorten|explanen|expounen|expressen|failen|falsen|flateren|flecchen|florishen|flouren|forfeten|fructifien|gendren|glosen|governen|graunten|grucchen|halen|hasten|hurten|embracen|joien|jugen|justen|langouren|languishen|manacen|marchen1|medlen|merveillen|meven|maintenen|ministren|monesten|multiplien|musen|noien|norishen|noten2|obeishen|obeien|occupien|ordeinen|overpassen|parten|passen|paien|pesen|perishen|purseuen|pertenen|perverten|plesen|purveien|povren|possessen|praien|prechen|preferren|preisen|presenten|preserven|pressen|pretenden|preven|procuren|promisen|promitten|prophecien|purchasen|purgien|purposen|purifien|raumpen|rasen1|ravishen|rebuken|receiven|recommenden|reformen|refrainen|regnen|rehersen|remembren|repenten|replien1|representen|repreven|reprocen|requeren|resorten|returnen|rewarden|robben|rushen|saluen|saven|scalden|siuen|stablishen|stroien|supplaunten|supporten|supposen|sustenen|signifien|tenden1|touchen|treilen|translaten|tracen|travailen|tremblen|trespassen|troublen|usen|varien|virounen|waimenten|wasten|waiten|imaginen)
	%blended: (*VAG*|*DAG*|*HAG* idoms bulmen|defoulen|offren|tabouren|turnen|warnen)
	%others: (*VAG*|*DAG*|*HAG* idoms chiteren|berien|blaberen|chateren|chiveren|fagen|grinten|houven|kenchen|lakken|lashen|laiten|rumien|shunchen|shoderen|smellen|smilen|snobben|sobben|stomblen|talken|tarrien|tollen1|toteren|tumblen|trusten|tutelen|underfongen|weilen)
	%other2: ELSE
}
3: {
	%1: (*VAG*|*DAG*|*HAG* idoms adden|don1|aken|welden|lasten1|onden1|asken|brennen|eken|seigen|beggen|benden|bearen|beren|beaten|ben|bidden|gon|biggen|birlen|biten|blasen|blauen|bleden|blessen|bliken|blissen|leten|blouen|bobben|boillen|buwan|braien|breken|bringen|bulmen|bien|binden|callen|casten|cesen|chargen|charmen|chasten|chacen|chaungen|sheden|chesen|chiden|clothen|clappen|clensen|clepen|clouten1|climben|knelen|comen|connen|kerven|counten|creopen|craulen|crien|cursen|kissen|citen|delen|demen|deren|deuen|douten|draggen|dreden|drauen|drien|dremen|dressen|drinken|driven|droppen|dwellen|duren|cennen|dien|ebben|rennen|eten|liven|wellen|fagen|failen|fallen|falsen|faren|fasten|fagnen|fighten|feden|felen|feren|flen1|flien|fleten|flouen|flitan|falden|fresen|fillen|fishen|yernen|geinen|yelden|yellen|yenen|yeven|yongen|yerren|galpen|gapen|gasten|gauren|geten|gladen|glemen|gloen|gliden|glisen|glosen|gnasten|gronen|graunten|graven1|grennen|greten|grieten|grucchen|grouen|grimen|grinten|girden1|haven|holden1|halsen1|halsen2|halen|hongen|hasten|haten|heien|helden|heren|healen|helpen|listen2|houven|hurten|whielen|hiden|brainen|wonen1|joien|jugen|justen|kenchen|kennen|kepen|lakken|leden1|laughen|longen3|louen1|lashen|losen|lien1|laiten|lenen|leonen|leren|lernen|letten|leaven|liften|lien2|lighten|liken|loken|lokken|longen1|loven2|loven1|louren|louten|leken|marchen1|melten|menen1|menen2|meten4|meven|milcen|mornen|musen|neighen|nimen|noien|noten2|tholen|speken|parten|passen|paien|pesen|plaien|plesen|praien|prechen|preisen|pressen|preven|pullen|putten|pinen|pipen|quaken|quethen|raumpen|raren|rasen1|recchen|reden1|regnen|renten2|resten1|resen1|reven|riusen|riden|risen|rixen|robben|rosen|rushen|sauen1|saven|seilen|scalden|shaken|sechen|shaven|shitten|shunchen|sheuen|shillen|shimen|shinen|slepen|sithen|seen|semen2|cenden|sengen|*seitten|sowen|siuen|shriven|seien|sellen|singen|slen|sliden|smaken|smellen|smirken|smiten|smilen|snobben|sobben|sounen|souken|sparen|spiren1|spreden|springen|spinnen|stonden|staren|sterten|sterven|stiren|stigen|stiken|stinken|stoppen|stormen|streuen|strenen|strengthen|striden|striken|stroien|sweren|swinken|swounen|swimmen|siken|thanken|thinken2|theoten|thirsten|threten1|taken|talken|techen|tithen|tellen|tempten|tenden1|touchen|tollen1|toten1|treilen|tracen|treden|trusten|trouen|turnen|eilen|wenden|wawen|weilen|washen|vaken|walken1|wallen1|wonen2|wanen|wandren|wanten|warnen|wasten|waiten|waxsen|wacchen|weden2|wepen|venen|werken|werpen|wharven|witen1|weighen|whelen|whirlen|willen1|wilnen|wounden|wreken|wresten|wringen|writen|wishen)
	%1half: (*VAG*|*DAG*|*HAG* idoms berien|clevien|errien|herien1|hopien|knouen|livien|lihtnen|makien|medlen|povren|prikien|purgien|rixlen|rumien|servien|usen|warien|wrestlen)
	%2: (*VAG*|*DAG*|*HAG* idoms abiden|accorden|agreen|anoien|appieren|ablen|abreggen|accusen|affermen|alargen|allegen|allighten|amblen|amenden|anbiden|chiteren|answeren|apperen|appreven|arisen|ascenden|assaillen|assenten|bakbiten|baptisen|bithinken|biginnen|biholden|bihesten|bihoten|bisechen|bitaken|bitraien|bistonden|bileven|bireusen|bisegen|beteon|blaberen|blemishen|bodien|borien|bicomen|chalengen|chateren|chiveren|commaunden|comforten|communen|compellen|compleinen|concernen|conceiven|conjuren|consenten|constreinen|conteinen|conveien|costeien|coveiten|counseilen|dalien|dampnen|declaren|defenden|defoulen|deliten|departen|despisen|descenden|desiren|destroien|discorden|describen|dispreisen|disputen|drouknen|encheven|enclinen|encresen|enfourmen|enjoien|enqueren|entenden|entren|exceden|excusen|exhorten|explanen|expounen|expressen|fikelen|flateren|flecchen|florishen|flouren|folwen|foryeten|forfeten|forsaken|forbeden|foryeven|fore-sen|forsweren|ful-filen|gaderen|gangen|gendren|governen|halwen|herkenen|hungren|irennen|embracen|knouelechen|langouren|languishen|manacen|merveillen|maintenen|misliken1|monesten|norishen|obeishen|obeien|offren|todelen|unseien|openen|ordeinen|outcasten|perishen|purseuen|pertenen|perverten|purveien|possessen|preferren|presenten|preserven|pretenden|procuren|promisen|promitten|purchasen|purposen|ravishen|rebuken|receiven|reformen|refrainen|rehersen|rekenen|repenten|replien1|repreven|reprocen|resorten|returnen|rewarden|saluen|shoderen|sinbeten*|slideren|snakeren|sorwen|sparklen|stablishen|studien|stomblen|sufferen|supplaunten|supporten|supposen|sustenen|thurghwonen|tabouren|tarrien|tocomen|toteren|tumblen|translaten|travailen|tremblen|trespassen|troublen|tribulen|tutelen|twiselen|fulfillen|varien|virounen|unwiten|upberen|upstien|uprisen|waimenten|welcommen|welfaren|withdrauen|withholden|witnessen|wondren|worshipen)
	%2half: (*VAG*|*DAG*|*HAG* idoms unknouen|requeren)
	%3: (*VAG*|*DAG*|*HAG* idoms ayenstonden|appertenen|comprehenden|consideren|continuen|copulaten|discoveren|disencresen|disseveren|edifien|encompassen|envirounen|executen|fructifien|ministren|multiplien|misbileven|occupien|underfon|overpassen|overrennen|overthrouen|prophecien|purifien|recommenden|remembren|representen|signifien|understonden|underfongen|imaginen)
	%other3: ELSE
}
4: {
	%transitive: ((IP* idoms *VAG*|*DAG*|*HAG*) AND 
				 (IP* idoms NP-OB1|NP-OB2))
	%ambiguous:	((IP* idoms *VAG*|*DAG*|*HAG*) AND
				(*VAG*|*DAG*|*HAG* idoms discorden|longen3|consenten|anoien|deren|assenten|sorwen|lakken|bileven|halwen|semen2|grucchen|agreen|obeishen|liken|plesen|accorden|vaken|pertain|lasten1|knouen) AND
				(IP* idoms !NP-OB1|NP-OB2))
	%prep_intransitive: ((IP* idoms *VAG*|*DAG*|*HAG*) AND 
						(IP* idoms PP) AND
						(IP* idoms !NP-OB1|NP-OB2))
	%intransitive: ((IP* idoms *VAG*|*DAG*|*HAG*) AND 
				   (IP* idoms !NP-OB1|NP-OB2))
	%other4: ELSE
}