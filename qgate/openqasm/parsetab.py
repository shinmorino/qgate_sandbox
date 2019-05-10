
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/left^leftIDleftUleftCXleftBARRIERleftOPENQASMINCLUDEBARRIER CREG CX EQ FILENAME GATE ID IF INCLUDE MEASURE NMINTEGER OPAQUE OPENQASM PI QREG REAL RESET U UNARYOP mainprogram : header_or_empty includelist_or_empty program_begin program program_end  program_begin :  program_end :  header_or_empty : OPENQASM REAL ';' \n                        |  includelist_or_empty : includelist\n                             |  includelist : includelist include\n                    | include  include : INCLUDE FILENAME ';'   program : statement\n                | program statement\n                |  statement : decl\n                  | gatedecl goplist '}'\n                  | gatedecl  '}'\n                  | OPAQUE ID idlist ';'\n                  | OPAQUE ID '(' ')' idlist ';'\n                  | OPAQUE ID '(' exp ')' idlist ';'\n                  | qop\n                  | IF '(' ID EQ NMINTEGER ')' open_if qop\n                  | BARRIER anylist ';'  open_if :  decl : QREG ID '[' NMINTEGER ']' ';'\n             | CREG ID '[' NMINTEGER ']' ';'  gatedecl : GATE ID idlist '{'\n                 | GATE ID '(' ')' idlist '{'\n                 | GATE ID '(' idlist ')' idlist '{'  goplist : uop\n                | BARRIER idlist ';'\n                | goplist uop\n                | goplist BARRIER idlist ';'  qop : uop\n            | MEASURE argument '-' '>' argument ';'\n            | RESET argument ';'  uop : U '(' explist ')' argument ';' %prec U\n            | CX argument ',' argument ';' %prec CX\n            | ID anylist ';' %prec ID\n            | ID '(' ')' anylist ';' %prec ID\n            | ID '(' explist ')' anylist ';' %prec ID  anylist : idlist\n                | mixedlist  idlist : ID\n               | idlist ',' ID  mixedlist : ID '[' NMINTEGER ']'\n                  | mixedlist ',' ID\n                  | mixedlist ',' ID '[' NMINTEGER ']'\n                  | idlist ',' ID '[' NMINTEGER ']'  argument : ID\n                 | ID '[' NMINTEGER ']'   explist : explist ',' exp\n                | exp  exp : REAL\n            | NMINTEGER\n            | PI\n            | ID\n            | exp '+' exp %prec '+'\n            | exp '-' exp %prec '-'\n            | exp '*' exp %prec '*'\n            | exp '/' exp %prec '/'\n            | '-' exp %prec '-'\n            | exp '^' exp\n            | '(' exp ')'\n            | UNARYOP '(' exp ')'\n    "
    
_lr_action_items = {'GATE':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,149,150,151,152,153,158,159,],[-5,-7,-9,-6,-2,-4,-8,14,-10,-11,14,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-18,-34,-24,-25,-36,-19,-21,]),'{':([53,54,115,117,141,],[86,-43,-44,142,154,]),'MEASURE':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,147,149,150,151,152,153,157,158,159,],[-5,-7,-9,-6,-2,-4,-8,21,-10,-11,21,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-23,-18,-34,-24,-25,-36,21,-19,-21,]),'NMINTEGER':([35,51,58,59,68,70,74,77,82,92,93,94,95,96,99,100,104,118,130,],[62,62,90,62,62,103,62,109,112,62,62,62,62,62,62,62,132,143,146,]),'RESET':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,147,149,150,151,152,153,157,158,159,],[-5,-7,-9,-6,-2,-4,-8,16,-10,-11,16,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-23,-18,-34,-24,-25,-36,16,-19,-21,]),']':([90,103,109,112,143,146,],[119,131,136,138,155,156,]),'>':([76,],[108,]),'PI':([35,51,59,68,74,92,93,94,95,96,99,100,],[64,64,64,64,64,64,64,64,64,64,64,64,]),';':([4,11,32,33,34,36,37,38,41,54,73,81,89,97,102,110,114,115,119,127,131,134,135,136,138,139,148,155,156,],[9,13,-41,57,-43,-42,-49,71,75,-43,105,111,-44,126,-46,137,140,-44,-45,144,-50,149,150,151,152,153,158,-48,-47,]),'/':([60,61,62,63,64,91,101,106,120,121,122,123,124,125,128,129,145,],[95,-56,-54,-53,-55,95,95,95,-63,95,-62,95,-60,-59,95,95,-64,]),'ID':([0,2,5,6,8,9,10,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,30,31,35,39,40,43,46,47,48,49,51,55,56,57,59,65,68,69,71,74,75,78,79,80,84,85,86,88,92,93,94,95,96,98,99,100,105,107,108,111,113,116,126,133,137,140,142,144,147,149,150,151,152,153,154,157,158,159,],[-5,-7,-9,-6,-2,-4,-8,15,-10,31,34,37,-11,40,34,37,15,-20,45,-33,15,-14,50,37,54,61,72,54,-12,-16,15,-29,54,61,54,89,-38,61,34,61,102,-35,61,-22,-15,-31,54,37,115,-26,54,61,61,61,61,61,34,61,61,-17,54,37,-30,37,54,-39,54,-32,-37,-27,-40,-23,-18,-34,-24,-25,-36,-28,15,-19,-21,]),'^':([60,61,62,63,64,91,101,106,120,121,122,123,124,125,128,129,145,],[93,-56,-54,-53,-55,93,93,93,-63,93,-62,93,93,93,93,93,-64,]),'FILENAME':([7,],[11,]),'OPAQUE':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,149,150,151,152,153,158,159,],[-5,-7,-9,-6,-2,-4,-8,19,-10,-11,19,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-18,-34,-24,-25,-36,-19,-21,]),'BARRIER':([0,2,5,6,8,9,10,12,13,17,22,23,25,26,27,43,46,47,48,57,71,75,78,79,86,105,111,126,137,140,142,144,149,150,151,152,153,154,158,159,],[-5,-7,-9,-6,-2,-4,-8,20,-10,-11,20,-20,-33,49,-14,-12,-16,80,-29,-38,-35,-22,-15,-31,-26,-17,-30,-39,-32,-37,-27,-40,-18,-34,-24,-25,-36,-28,-19,-21,]),'(':([15,18,29,31,35,40,51,59,67,68,74,92,93,94,95,96,99,100,],[35,39,51,55,59,74,59,59,100,59,59,59,59,59,59,59,59,59,]),'UNARYOP':([35,51,59,68,74,92,93,94,95,96,99,100,],[67,67,67,67,67,67,67,67,67,67,67,67,]),',':([32,34,36,37,52,53,54,60,61,62,63,64,66,73,81,83,87,89,101,102,110,115,117,119,120,121,122,123,124,125,128,131,134,141,145,148,155,156,],[56,-43,69,-49,84,85,-43,-52,-56,-54,-53,-55,99,85,85,99,85,-44,-61,-46,85,-44,85,-45,-63,-57,-62,-58,-60,-59,-51,-50,85,85,-64,85,-48,-47,]),'}':([26,47,48,57,79,86,111,126,137,140,142,144,153,154,],[46,78,-29,-38,-31,-26,-30,-39,-32,-37,-27,-40,-36,-28,]),')':([35,54,55,60,61,62,63,64,66,74,83,87,91,101,106,115,120,121,122,123,124,125,128,129,132,145,],[65,-43,88,-52,-56,-54,-53,-55,98,107,113,116,120,-61,133,-44,-63,-57,-62,-58,-60,-59,-51,145,147,-64,]),'CREG':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,149,150,151,152,153,158,159,],[-5,-7,-9,-6,-2,-4,-8,28,-10,-11,28,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-18,-34,-24,-25,-36,-19,-21,]),'REAL':([1,35,51,59,68,74,92,93,94,95,96,99,100,],[4,63,63,63,63,63,63,63,63,63,63,63,63,]),'+':([60,61,62,63,64,91,101,106,120,121,122,123,124,125,128,129,145,],[92,-56,-54,-53,-55,92,-61,92,-63,-57,-62,-58,-60,-59,92,92,-64,]),'IF':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,149,150,151,152,153,158,159,],[-5,-7,-9,-6,-2,-4,-8,18,-10,-11,18,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-18,-34,-24,-25,-36,-19,-21,]),'*':([60,61,62,63,64,91,101,106,120,121,122,123,124,125,128,129,145,],[96,-56,-54,-53,-55,96,96,96,-63,96,-62,96,-60,-59,96,96,-64,]),'QREG':([0,2,5,6,8,9,10,12,13,17,22,23,25,27,43,46,57,71,75,78,105,126,140,144,149,150,151,152,153,158,159,],[-5,-7,-9,-6,-2,-4,-8,24,-10,-11,24,-20,-33,-14,-12,-16,-38,-35,-22,-15,-17,-39,-37,-40,-18,-34,-24,-25,-36,-19,-21,]),'[':([34,37,45,50,89,102,],[58,70,77,82,118,130,]),'INCLUDE':([0,2,5,6,9,10,13,],[-5,7,-9,7,-4,-8,-10,]),'$end':([0,2,3,5,6,8,9,10,12,13,17,22,23,25,27,43,44,46,57,71,75,78,105,126,140,144,149,150,151,152,153,158,159,],[-5,-7,0,-9,-6,-2,-4,-8,-13,-10,-11,-3,-20,-33,-14,-12,-1,-16,-38,-35,-22,-15,-17,-39,-37,-40,-18,-34,-24,-25,-36,-19,-21,]),'EQ':([72,],[104,]),'OPENQASM':([0,],[1,]),'-':([35,37,42,51,59,60,61,62,63,64,68,74,91,92,93,94,95,96,99,100,101,106,120,121,122,123,124,125,128,129,131,145,],[68,-49,76,68,68,94,-56,-54,-53,-55,68,68,94,68,68,68,68,68,68,68,-61,94,-63,-57,-62,-58,-60,-59,94,94,-50,-64,]),'U':([0,2,5,6,8,9,10,12,13,17,22,23,25,26,27,43,46,47,48,57,71,75,78,79,86,105,111,126,137,140,142,144,147,149,150,151,152,153,154,157,158,159,],[-5,-7,-9,-6,-2,-4,-8,29,-10,-11,29,-20,-33,29,-14,-12,-16,29,-29,-38,-35,-22,-15,-31,-26,-17,-30,-39,-32,-37,-27,-40,-23,-18,-34,-24,-25,-36,-28,29,-19,-21,]),'CX':([0,2,5,6,8,9,10,12,13,17,22,23,25,26,27,43,46,47,48,57,71,75,78,79,86,105,111,126,137,140,142,144,147,149,150,151,152,153,154,157,158,159,],[-5,-7,-9,-6,-2,-4,-8,30,-10,-11,30,-20,-33,30,-14,-12,-16,30,-29,-38,-35,-22,-15,-31,-26,-17,-30,-39,-32,-37,-27,-40,-23,-18,-34,-24,-25,-36,-28,30,-19,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'idlist':([15,20,31,40,49,55,65,80,88,98,107,116,133,],[32,32,53,73,81,87,32,110,117,32,134,141,148,]),'anylist':([15,20,65,98,],[33,41,97,127,]),'exp':([35,51,59,68,74,92,93,94,95,96,99,100,],[60,60,91,101,106,121,122,123,124,125,128,129,]),'program':([12,],[22,]),'argument':([16,21,30,84,108,113,],[38,42,52,114,135,139,]),'statement':([12,22,],[17,43,]),'program_begin':([8,],[12,]),'qop':([12,22,157,],[23,23,159,]),'mainprogram':([0,],[3,]),'includelist':([2,],[6,]),'goplist':([26,],[47,]),'uop':([12,22,26,47,157,],[25,25,48,79,25,]),'include':([2,6,],[5,10,]),'gatedecl':([12,22,],[26,26,]),'explist':([35,51,],[66,83,]),'decl':([12,22,],[27,27,]),'includelist_or_empty':([2,],[8,]),'open_if':([147,],[157,]),'mixedlist':([15,20,65,98,],[36,36,36,36,]),'program_end':([22,],[44,]),'header_or_empty':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> mainprogram","S'",1,None,None,None),
  ('mainprogram -> header_or_empty includelist_or_empty program_begin program program_end','mainprogram',5,'p_mainprogram','yacc.py',18),
  ('program_begin -> <empty>','program_begin',0,'p_program_begin','yacc.py',21),
  ('program_end -> <empty>','program_end',0,'p_program_end','yacc.py',25),
  ('header_or_empty -> OPENQASM REAL ;','header_or_empty',3,'p_header_or_empty','yacc.py',29),
  ('header_or_empty -> <empty>','header_or_empty',0,'p_header_or_empty','yacc.py',30),
  ('includelist_or_empty -> includelist','includelist_or_empty',1,'p_includelist_or_empty','yacc.py',34),
  ('includelist_or_empty -> <empty>','includelist_or_empty',0,'p_includelist_or_empty','yacc.py',35),
  ('includelist -> includelist include','includelist',2,'p_includelist','yacc.py',39),
  ('includelist -> include','includelist',1,'p_includelist','yacc.py',40),
  ('include -> INCLUDE FILENAME ;','include',3,'p_include','yacc.py',44),
  ('program -> statement','program',1,'p_program','yacc.py',51),
  ('program -> program statement','program',2,'p_program','yacc.py',52),
  ('program -> <empty>','program',0,'p_program','yacc.py',53),
  ('statement -> decl','statement',1,'p_statement','yacc.py',57),
  ('statement -> gatedecl goplist }','statement',3,'p_statement','yacc.py',58),
  ('statement -> gatedecl }','statement',2,'p_statement','yacc.py',59),
  ('statement -> OPAQUE ID idlist ;','statement',4,'p_statement','yacc.py',60),
  ('statement -> OPAQUE ID ( ) idlist ;','statement',6,'p_statement','yacc.py',61),
  ('statement -> OPAQUE ID ( exp ) idlist ;','statement',7,'p_statement','yacc.py',62),
  ('statement -> qop','statement',1,'p_statement','yacc.py',63),
  ('statement -> IF ( ID EQ NMINTEGER ) open_if qop','statement',8,'p_statement','yacc.py',64),
  ('statement -> BARRIER anylist ;','statement',3,'p_statement','yacc.py',65),
  ('open_if -> <empty>','open_if',0,'p_open_if','yacc.py',79),
  ('decl -> QREG ID [ NMINTEGER ] ;','decl',6,'p_decl','yacc.py',83),
  ('decl -> CREG ID [ NMINTEGER ] ;','decl',6,'p_decl','yacc.py',84),
  ('gatedecl -> GATE ID idlist {','gatedecl',4,'p_gatedecl','yacc.py',92),
  ('gatedecl -> GATE ID ( ) idlist {','gatedecl',6,'p_gatedecl','yacc.py',93),
  ('gatedecl -> GATE ID ( idlist ) idlist {','gatedecl',7,'p_gatedecl','yacc.py',94),
  ('goplist -> uop','goplist',1,'p_goplist','yacc.py',98),
  ('goplist -> BARRIER idlist ;','goplist',3,'p_goplist','yacc.py',99),
  ('goplist -> goplist uop','goplist',2,'p_goplist','yacc.py',100),
  ('goplist -> goplist BARRIER idlist ;','goplist',4,'p_goplist','yacc.py',101),
  ('qop -> uop','qop',1,'p_qop','yacc.py',105),
  ('qop -> MEASURE argument - > argument ;','qop',6,'p_qop','yacc.py',106),
  ('qop -> RESET argument ;','qop',3,'p_qop','yacc.py',107),
  ('uop -> U ( explist ) argument ;','uop',6,'p_uop','yacc.py',118),
  ('uop -> CX argument , argument ;','uop',5,'p_uop','yacc.py',119),
  ('uop -> ID anylist ;','uop',3,'p_uop','yacc.py',120),
  ('uop -> ID ( ) anylist ;','uop',5,'p_uop','yacc.py',121),
  ('uop -> ID ( explist ) anylist ;','uop',6,'p_uop','yacc.py',122),
  ('anylist -> idlist','anylist',1,'p_anylist','yacc.py',144),
  ('anylist -> mixedlist','anylist',1,'p_anylist','yacc.py',145),
  ('idlist -> ID','idlist',1,'p_idlist','yacc.py',149),
  ('idlist -> idlist , ID','idlist',3,'p_idlist','yacc.py',150),
  ('mixedlist -> ID [ NMINTEGER ]','mixedlist',4,'p_mixedlist','yacc.py',158),
  ('mixedlist -> mixedlist , ID','mixedlist',3,'p_mixedlist','yacc.py',159),
  ('mixedlist -> mixedlist , ID [ NMINTEGER ]','mixedlist',6,'p_mixedlist','yacc.py',160),
  ('mixedlist -> idlist , ID [ NMINTEGER ]','mixedlist',6,'p_mixedlist','yacc.py',161),
  ('argument -> ID','argument',1,'p_argument','yacc.py',178),
  ('argument -> ID [ NMINTEGER ]','argument',4,'p_argument','yacc.py',179),
  ('explist -> explist , exp','explist',3,'p_explist','yacc.py',188),
  ('explist -> exp','explist',1,'p_explist','yacc.py',189),
  ('exp -> REAL','exp',1,'p_exp','yacc.py',199),
  ('exp -> NMINTEGER','exp',1,'p_exp','yacc.py',200),
  ('exp -> PI','exp',1,'p_exp','yacc.py',201),
  ('exp -> ID','exp',1,'p_exp','yacc.py',202),
  ('exp -> exp + exp','exp',3,'p_exp','yacc.py',203),
  ('exp -> exp - exp','exp',3,'p_exp','yacc.py',204),
  ('exp -> exp * exp','exp',3,'p_exp','yacc.py',205),
  ('exp -> exp / exp','exp',3,'p_exp','yacc.py',206),
  ('exp -> - exp','exp',2,'p_exp','yacc.py',207),
  ('exp -> exp ^ exp','exp',3,'p_exp','yacc.py',208),
  ('exp -> ( exp )','exp',3,'p_exp','yacc.py',209),
  ('exp -> UNARYOP ( exp )','exp',4,'p_exp','yacc.py',210),
]