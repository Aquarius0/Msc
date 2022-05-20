grammar Query;

query:		query c_and query
		| p_id opEqual q_value
		| p_id
		| EOF
		;

p_id:		ldse p_id
		| us_sgn p_id
		| label p_id
		| label
		| us_sgn
		;		

q_value:	q_value delim value+
		| value+
		| EOF
		;
		
value:		label
		| ilg+
		;
		
ilg:		opMinus
		| us_sgn+
		| c_colon+
		| c_slash+
		| WS+
		| CAMMA
		| c_percent+
		| s_bslash+
		| opSem+
		| c_q+
		| opEqual+
		| ch_ilg+
		| c_dot+
		;

label:		ldse
		| LET_DIG
		;

delim:		WS delim
		| CAMMA delim
		| WS
		| CAMMA
		;
		
ch_ilg:	c_star+
		| par_close+
		| par_open+
		| c_brack+
		| c_acolad+
		| c_dollar+
		| c_and_hex+
		| c_adsgn+
		| opNot+
		| c_or+
		| opBinInvert+
		| c_irg1+
		| opLt+
		| opGt+
		| quote+
		| dquote+
		;
		
ldse:		LET_DIG_S_LET;

opNot:	EXCAM_SGN;

opBinInvert:	BIN_INVERT;

opEqual:	EQ;

opLt:	LT_SGN;

opGt:	GT_SGN;


opMinus:	HYPHEN;


opSem:	SEMI_COLON;

cmt:		HASHTAG
		| ddash WS
		;
		
ddash:		opMinus opMinus;

quote:		QUOTE;

dquote:	DQUOTE;

us_sgn:	US;


		
c_and:		CH_AND;

c_and_hex:	CH_AND_HEX;

c_or:		CH_OR;

c_slash:	SLASH;



c_dot:		DOT;

c_colon:	COLON;

s_bslash:	B_SLASH;

c_q:		QM;

par_open:	PAR_O;

par_close:	PAR_C;

c_star:	STAR;

c_percent:	PERCENT;

c_brack:	BRACK;

c_acolad:	ACOLAD;

c_dollar:	DOLLAR;

c_adsgn:	ADSGN;

c_irg1:	IRG_SGN1;



LET_DIG_S_LET:	LETTER+(LET_DIG)?;

LET_DIG:	(LETTER | DIGIT)+;

SLASH:		('/' | '%2f');

WS:		(' ' | '%20' | '+');

CAMMA:		(',' | '%2c');


DIGIT:		'0'..'9';

LETTER: 	'a'..'z';

QUOTE:		'\'' | '%27';

DQUOTE: 	'"' | '%22';

HYPHEN:	'-' | '2d';

US:		'_'| '%5f';

EQ:		'=' | '%3d';

DOT:		'.' | '%2e';

B_SLASH:	'\\' | '%5c';

QM:		'?' | '%3f';

PERCENT:	'%' | '%25';

CH_AND:	'&';

CH_AND_HEX:	'%26';

COLON:		':' | '%3a';

SEMI_COLON:	';' | '%3b';

STAR:		'*';

PAR_O:		'(' | '%28';

PAR_C:		')' | '%29';

BRACK:		('[' | ']');

ACOLAD:	('{' | '}');

DOLLAR:	'$' | '%24';

ADSGN:		'@' | '%40';

EXCAM_SGN:	'!' | '%21';

BIN_INVERT:	'~';

IRG_SGN1:	'`' | '%60';

CH_OR:		'|' | '%7c';

LT_SGN:	'<' | '%3c';

GT_SGN:	'>' | '%3e';

HASTAG:	'#'; 

