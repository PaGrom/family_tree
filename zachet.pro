name(alik).
name(borya).
name(vitya).
name(lena).
name(dasha).
gorod(harkov).
gorod(uman).
gorod(poltava).
gorod(slavyansk).
gorod(kramatorsk).

jitel(X,Y).

jitel(X,Y) :-
			name(X), gorod(Y), X=alik, not(Y=uman), jitel(borya, kramatorsk);
			name(X), gorod(Y), X=borya, Y=harkov, not(jitel(vitya, harkov));
			name(X), gorod(Y), X=vitya, Y=harkov, not(jitel(borya, harkov));
			name(X), gorod(Y), X=vitya, not(Y=slavyansk), jitel(lena, harkov);
			name(X), gorod(Y), X=dasha, Y=uman, not(jitel(lena, kramatorsk));
			name(X), gorod(Y), X=lena, Y=kramatorsk, not(jitel(dasha, uman)).

solution(X1,Y1,X2,Y2,X3,Y3,X4,Y4,X5,Y5) :-
			name(X1),name(X2),name(X3),name(X4),name(X5),
			mesto(Y1),mesto(Y2),mesto(Y3),mesto(Y4),mesto(Y5),
			jitel(X1,Y1),jitel(X2,Y2),jitel(X3,Y3),jitel(X4,Y4),jitel(X5,Y5),!.