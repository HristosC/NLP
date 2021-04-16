# NLP
NLP Project for the NLP Course
<p align="middle">
  <b>-------Lexical Analysis (lexical_analysis.py)-------</b>
  </br> </br>
      Reads a text from a file and produces a list of sentences. 	
      Each sentence is a list of words.</br>
      Takes in a test.txt file with a text that can be full of different special characters (for example "!" "," "." "'" """ "[" "]") </br>
      Every time we meet a terminal symbol ( "!" "." "?" ) a sentence is created.
      If we meet any other special character then we delete it.
      <br><br>
      <b>Original Text:</b> <br> <br>
      <img src="https://user-images.githubusercontent.com/36642254/115015277-13504500-9ebc-11eb-8855-17b909503cd5.png"> <br> <br>
      <b>Sentence Produced:</b> <br> <br>
      <img src="https://user-images.githubusercontent.com/36642254/115015203-fb78c100-9ebb-11eb-8a44-87d24f7f6f5a.png"> <br> <br>
</p>

<p align="middle">
  <b>-------Syntactic analysis (syntactic_analysis.py)-------</b>
  </br> </br>
      Takes as input a list of sentences and produces their syntax trees<br><br>
      <b>The Grammar rules of Syntactic Analysis: </b>
      <br>
   
      /*---------------------------------------------------------------------*/
      /* Sentence (snt) 					*/
      /* Proper Nouns (pn) 				*/
      /* Intransitive Verbs (iv) 				*/
      /* Auxiliary Verbs (av) 				*/
      /* Verbs (v) 					*/
      /* Transitive Verbs (tv) 				*/
      /* Adverb (adv) 					*/
      /* Adjectives (adj) 					*/
      /* Determiner (det) 					*/
      /* Noun (n) 					*/
      /* Noun Phrase (np) 					*/
      /* Verb Phrase (vb) 					*/
      /*---------------------------------------------------------------------*/

      /*---------------------------------------------------------------------*/
      /* Sentence (snt) 					*/
      /*---------------------------------------------------------------------*/
      snt(s(NP,VP)) 	--> np(NP), vp(VP).

      /*---------------------------------------------------------------------*/
      /* Noun Phrase (np) 					*/
      /*---------------------------------------------------------------------*/
      np(np(N))		--> pn(N).
      np(np(D,N))	--> det(D), n(N).
      np(np(N))		--> n(N).

      /*---------------------------------------------------------------------*/
      /* Verb Phrase (vb) 					*/
      /*---------------------------------------------------------------------*/
      % Intransitive verbs :
      vp(vp(V)) 		--> iv(V). 
      vp(vp(V,ADV)) 	--> iv(V), adv(ADV). 
      % Auxiliary verbs
      vp(vp(AV,A)) 	--> av(AV), adj(A).
      % Transitive verbs :
      vp(vp(TV, PN, NP)) 	--> tv(TV), np(PN), np(NP).
      % verbs
      vp(vp(V,NP)) 	--> v(V), np(NP).
      /*---------------------------------------------------------------------*/
      /*==========================================================*/
      /* 	VOCABULARY OF EXAMPLE			*/
      /*==========================================================*/
      /* the dog needs food. the cat has the food. the dog hates the 	*/
      /* cat. the dog chased the cat. the cat is scary.		*/
      /*---------------------------------------------------------------------*/
      /* det : the	verbs : needs, has, hates, chased, is	*/
      /* adjectives : scary			nouns : cat, dog	*/
      /*---------------------------------------------------------------------*/

      /*---------------------------------------------------------------------*/
      /* Intransitive Verbs (iv) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :

      % extension of vocabulary :
      iv(iv(runs))-->[runs].
      iv(iv(run))-->[run].
      iv(iv(running))-->[running].
      iv(iv(hurts))-->[hurts].
      iv(iv(hurt))-->[hurt].
      iv(iv(hurting))-->[hurting].
      iv(iv(walks))-->[walks].
      iv(iv(walk))-->[walk].
      iv(iv(walking))-->[walking].
      iv(iv(jumps))-->[jumps].
      iv(iv(jump))-->[jump].
      iv(iv(jumping))-->[jumping].
      iv(iv(shoots))-->[shoots].
      iv(iv(shoot))-->[shoot].
      iv(iv(shooting))-->[shooting].

      /*---------------------------------------------------------------------*/
      /* Auxiliary Verbs (av) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      av(av(is))-->[is].
      % extension of vocabulary :
      av(av(does))-->[does].
      av(av(are))-->[are].
      av(av(do))-->[do].

      /*---------------------------------------------------------------------*/
      /* Transitive Verbs (tv) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :

      % extension of vocabulary :
      tv(tv(gives))	-->[gives]. 
      tv(tv(give))	-->[give]. 
      tv(tv(gave))	-->[gave]. 
      tv(tv(giving))	-->[giving].

      /*---------------------------------------------------------------------*/
      /* Verbs (v) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      v(v(chased))-->[chased].
      v(v(chase))-->[chase].
      v(v(needs))-->[needs].
      v(v(need))-->[need].
      v(v(hates))-->[hates]. 
      v(v(hate))-->[hate].
      v(v(has))  -->[has].   
      v(v(have))  -->[have].
      % extension of vocabulary :
      v(v(loves))-->[loves]. 
      v(v(love))-->[love].
      v(v(kicks))-->[kicks]. 
      v(v(kick))-->[kick].
      v(v(jumps))-->[jumps]. 
      v(v(jump))-->[jump].

      /*---------------------------------------------------------------------*/
      /* Adjectives (adj) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      adj(adj(scary))-->[scary].
      % extension of vocabulary :
      adj(adj(tall))-->[tall].
      adj(adj(short))-->[short].
      adj(adj(blonde))-->[blonde].
      adj(adj(slim))-->[slim].
      adj(adj(fat))-->[fat].

      /*---------------------------------------------------------------------*/
      /* Adverb (adv) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example :

      % extension of vocabulary :
      adv(adv(quickly))-->[quickly].
      adv(adv(slowly))-->[slowly].
      adv(adv(independently))-->[independently].

      /*---------------------------------------------------------------------*/
      /* Noun (n) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example
      n(n(food))-->[food].
      n(n(cat))-->[cat].
      n(n(cats))-->[cats].
      n(n(dog))-->[dog].
      n(n(dogs))-->[dogs].
      % extension of vocabulary
      n(n(book))-->[book].
      n(n(books))-->[books].
      n(n(feather))-->[feather].
      n(n(feathers))-->[feathers].
      n(n(baby))-->[baby].
      n(n(babies))-->[babies].
      n(n(boy))-->[boy].
      n(n(boys))-->[boys].
      n(n(girl))-->[girl].
      n(n(girls))-->[girls].
      n(n(icecream))-->[icecream].
      n(n(icecreams))-->[icecreams].

      /*---------------------------------------------------------------------*/
      /* Proper Nouns (pn) 				*/
      /*---------------------------------------------------------------------*/
      pn(pn(mary))-->[mary].
      pn(pn(john))-->[john].
      pn(pn(tomy))-->[tomy].

      /*---------------------------------------------------------------------*/
      /* Determiner (det) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      det(det(the)) -->[the].
      % extension of vocabulary
      det(det(a))   -->[a].
      det(det(an))   -->[an].

      /*==========================================================*/
      /* 	END OF RULES		*/
      /*==========================================================*/

 </p>
<p align="middle">      
      <b>Original Text:</b> <br> <br>
      <img src="https://user-images.githubusercontent.com/36642254/115017334-100a8880-9ebf-11eb-922e-a294504ba050.png"> <br> <br>
      <b>Sentence Produced:</b> <br> <br>
      <img src="https://user-images.githubusercontent.com/36642254/115017374-1c8ee100-9ebf-11eb-9cc2-6d6dd92e15c3.png"> <br> <br>
</p>

<p align="middle">
  <b>-------Semantic analysis (semantic_analysis.py)-------</b>
  </br> </br>
      Takes as input a list of sentences and produces their	
      semantics - easier if done along with syntactic analysis
</p>

      /*==========================================================*/
      /* 	SEMANTICS  CREATION  RULES 		*/
      /*==========================================================*/

      sem(1,Sem) --> sem_np(N), sem_vp(1,V,N1),  	{Sem=..[V,N,N1]}.
      % example : [the,dog,hates,the,cat]
      % Sem = hates(dog,cat)
      % example : [mary,loves,the,cat]
      % Sem = loves(mary,cat)

      sem(2,Sem) --> sem_np(N), sem_vp(2,_,A),  	{Sem=..[A,N]}.
      % example : [the,cat,is,scary]
      % Sem = scarys(cat)
      % example : [nikos,is,slim]
      % Sem = slim(nikos)

      sem(3,Sem) --> sem_np(N), sem_iv(V,s),       	{Sem=..[V,N]}.
      % example : [maria,runs]
      % Sem = runs(maria)
      % example : [the,gun,shoots]
      % Sem = shoots(gun)

      sem(4,Sem) --> sem_np(N), sem_iv(V,s), sem_adv(A),	{Sem=..[V,N,A]}.
      % example : [george,runs,quickly]
      % Sem = runs(george,quickly)

      sem(5,Sem) -->sem_np(N), sem_tv(V,s), sem_np(N1), sem_np(N2), {Sem=..[V,N,N1,N2]}.
      % example : [george,gave,mary,a,book]
      % Sem = gave(george,mary,book)

      /* noun phrase */
      sem_np(N)	--> sem_pn(N).
      sem_np(N) 	--> sem_det(_), sem_n(N).
      sem_np(N) 	--> sem_n(N).

      /* verb phrase */
      sem_vp(1,V,N) --> sem_v(V,s), sem_np(N).
      sem_vp(2,is,A) --> sem_av(is), sem_adj(A).


      /*==========================================================*/
      /* 	SEMANTICS  VOCABULARY			*/
      /*==========================================================*/

      /*---------------------------------------------------------------------*/
      /* Intransitive Verbs (sem_iv) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :

      % extension of vocabulary :
      sem_iv(runs,s)	-->[runs].
      sem_iv(runs,q)	-->[running].
      sem_iv(hurts,s)	-->[hurts].
      sem_iv(hurts,q)	-->[hurting].
      sem_iv(walks,s)	-->[walks].
      sem_iv(walks,q)	-->[walking].
      sem_iv(jumps,s)	-->[jumps].
      sem_iv(jumps,q)	-->[jumping].
      sem_iv(shoots,s)	-->[shoots].
      sem_iv(shoots,q)	-->[shooting].

      /*---------------------------------------------------------------------*/
      /* Auxiliary Verbs (sem_av) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      sem_av(is)		-->[is].
      % extension of vocabulary :
      sem_av(does)	-->[does].
      sem_av(do)	-->[do].
      sem_av(does)	-->[did].
      sem_av(are)	-->[are].

      /*---------------------------------------------------------------------*/
      /* Transitive Verbs (sem_tv) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :

      % extension of vocabulary :
      sem_tv(gives,s)	-->[gives]. 
      sem_tv(gives,q)	-->[give]. 
      sem_tv(gave,s)	-->[gave]. 
      sem_tv(giving,q2)	-->[giving].

      /*---------------------------------------------------------------------*/
      /* Verbs (sem_v) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      sem_v(chased,_)	-->[chased].
      sem_v(chase,_)	-->[chase].
      sem_v(needs,s)	-->[needs].
      sem_v(need,q)	-->[need].
      sem_v(hates,s)	-->[hates]. 
      sem_v(hate,q)	-->[hate].
      sem_v(has,s)  	-->[has].   
      sem_v(have,q) 	-->[have].
      % extension of vocabulary :
      sem_v(loves,s)	-->[loves]. 
      sem_v(loves,q)	-->[love].
      sem_v(hates,s)	-->[hates]. 
      sem_v(hates,q)	-->[hate].
      sem_v(has,s)  	-->[has].   
      sem_v(has,q)  	-->[have].
      sem_v(kicks,s)	-->[kicks]. 
      sem_v(kicks,q)	-->[kick].
      sem_v(jumps,s)	-->[jumps]. 
      sem_v(jumps,q)	-->[jump].

      /*---------------------------------------------------------------------*/
      /* Adjectives (sem_adj) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      sem_adj(scary)	-->[scary].
      % extension of vocabulary :
      sem_adj(tall)		-->[tall].
      sem_adj(short)		-->[short].
      sem_adj(blonde)		-->[blonde].
      sem_adj(slim)		-->[slim].
      sem_adj(fat)		-->[fat].

      /*---------------------------------------------------------------------*/
      /* Adverb (sem_adv) 				*/
      /*---------------------------------------------------------------------*/
      % needed for example :

      % extension of vocabulary :
      sem_adv(quickly)		-->[quickly].
      sem_adv(slowly)		-->[slowly].
      sem_adv(independently)	-->[independently].

      /*---------------------------------------------------------------------*/
      /* Noun (sem_n) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example
      sem_n(food)		-->[food].
      sem_n(cat)		-->[cat].
      sem_n(cats)		-->[cats].
      sem_n(dog)		-->[dog].
      sem_n(dogs)		-->[dogs].
      % extension of vocabulary
      sem_n(book)		-->[book].
      sem_n(books)		-->[books].
      sem_n(feather)		-->[feather].
      sem_n(feathers)		-->[feathers].
      sem_n(baby)		-->[baby].
      sem_n(babies)		-->[babies].
      sem_n(boy)		-->[boy].
      sem_n(boys)		-->[boys].
      sem_n(girl)		-->[girl].
      sem_n(girls)		-->[girls].
      sem_n(icecream)		-->[icecream].
      sem_n(icecreams)		-->[icecreams].

      sem_n(X)			-->sem_pn(X). % a proper noun is also a noun
      /*---------------------------------------------------------------------*/
      /* Proper Nouns (sem_pn) 				*/
      /*---------------------------------------------------------------------*/
      sem_pn(mary)		-->[mary].
      sem_pn(john)		-->[john].
      sem_pn(tomy)		-->[tomy].

      /*---------------------------------------------------------------------*/
      /* Determiner (det) 					*/
      /*---------------------------------------------------------------------*/
      % needed for example :
      sem_det(the)	-->[the].
      % extension of vocabulary
      sem_det(a)	-->[a].
      sem_det(an)	-->[an].

      /*==========================================================*/
      /* 	END OF SEMANTICS  VOCABULARY		*/
      /*==========================================================*/
<p align="middle">
      <br>
      <b>Original Text:</b> <br> <br>
      <img src="https://user-images.githubusercontent.com/36642254/115017334-100a8880-9ebf-11eb-922e-a294504ba050.png"> <br> <br>
      <b>Sentence Produced:</b> <br> <br>
      <img src="https://user-images.githubusercontent.com/36642254/115019344-c2dbe600-9ec1-11eb-95bb-60358d91f3d5.png"> <br> <br>
</p>
