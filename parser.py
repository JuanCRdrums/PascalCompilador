from sly import Parser
from paslex import PascalLexer



class PasParser(Parser):

    tokens = PascalLexer.tokens

    precedence = (
        ('left', 'OR'),
		('left', 'AND'),
		('left', 'NOT'),
		('left', 'PLUS','MINUS'),
		('left', 'TIMES','DIV'),
        ('right', 'ELSE'),
    )

    start = 'program'

    @_('PROGRAM identifier SEMICOLON block DOT')
    def program(self,p):
        return p

    @_('variable_declaration_part procedure_declaration_part statement_part')
    def block(self,p):
        return p

    @_('empty')
    def variable_declaration_part(self,p):
        return p

    @_('VAR list_variable_declaration')
    def variable_declaration_part(self,p):
        return p

    @_('var_declaration SEMICOLON')
    def list_variable_declaration(self,p):
        return p

    @_('list_variable_declaration var_declaration')
    def list_variable_declaration(self,p):
        return p

    @_('identifier COLON type')
    def var_declaration(seld,p):
        return p

    @_('list_identifier')
    def var_declaration(self,p):
        return p

    @_('identifier COMA')
    def list_identifier(self,p):
        return p

    @_('list_identifier')
    def list_identifier(self,p):
        return p

    @_('simple_type')
    def type(self,p):
        return p

    @_('array_type')
    def type(self,p):
        return p

    @_('ARRAY LBR index_range RBR OF simple_type')
    def array_type(self,p):
        return p

    @_('INTCONST DOT DOT INTCONST')
    def index_range(self,p):
        return p

    @_('type_identifier')
    def simple_type(self,p):
        return p

    @_('identifier')
    def type_identifier(self,p):
        return p

    @_('list_procedure_declaration')
    def procedure_declaration_part(self,p):
        return p

    @_('empty')
    def list_procedure_declaration(self,p):
        return p

    @_('procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        return p

    @_('list_procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        return p

    @_('PROCEDURE ID SEMICOLON block')
    def procedure_declaration(self,p):
        return p

    @_('compound_statement')
    def statement_part(self,p):
        return p

    @_('BEGIN list_statement END')
    def compound_statement(self,p):
        return p

    @_('statement list_statement')
    def list_statement(self,p):
        return p

    @_('empty')
    def list_statement(self,p):
        return p;

    @_('SEMICOLON list_statement')
    def list_statement(self,p):
        return p

    @_('simple_statement')
    def statement(self,p):
        return p

    @_('structured_statement')
    def statement(self,p):
        return p

    @_('assignament_statement')
    def simple_statement(self,p):
        return p

    @_('procedure_statement')
    def simple_statement(self,p):
        return p

    @_('read_statement')
    def simple_statement(self,p):
        return p

    @_('write_statement')
    def simple_statement(self,p):
        return p

    @_('variable ASSIGN expression')
    def assignament_statement(self,p):
        return p

    @_('procedure_identifier')
    def procedure_statement(self,p):
        return p

    @_('identifier')
    def procedure_identifier(self,p):
        return p

    @_('READ LPAR list_input_variable RPAR')
    def read_statement(self,p):
        return p

    @_('input_variable')
    def list_input_variable(self,p):
        return p

    @_('list_input_variable COMA input_variable')
    def list_input_variable(self,p):
        return p

    @_('variable')
    def input_variable(self,p):
        return p

    @_('WRITE LPAR list_output_value RPAR')
    def write_statement(self,p):
        return p

    @_('output_value')
    def list_output_value(self,p):
        return p

    @_('list_output_value COMA output_value')
    def list_output_value(self,p):
        return p

    @_('expression')
    def output_value(self,p):
        return p

    @_('compound_statement')
    def structured_statement(self,p):
        return p

    @_('if_statement')
    def structured_statement(self,p):
        return p

    @_('while_statement')
    def structured_statement(self,p):
        return p

    @_('IF expression THEN statement')
    def if_statement(self,p):
        return p

    @_('IF expression THEN statement ELSE statement')
    def if_statement(self,p):
        return p

    @_('WHILE expression DO statement')
    def while_statement(self,p):
        return p

    @_('simple_expression')
    def expression(self,p):
        return p

    @_('simple_expression relational_operator simple_expression')
    def expression(self,p):
        return p

    @_('sign term list_adding_term')
    def simple_expression(self,p):
        return p

    @_('empty')
    def list_adding_term(self,p):
        return p

    @_('list_adding_term adding_operator term')
    def list_adding_term(self,p):
        return p

    @_('factor list_mult_factor')
    def term(self,p):
        return p

    @_('empty')
    def list_mult_factor(self,p):
        return p

    @_('list_mult_factor multiplying_operator factor')
    def list_mult_factor(self,p):
        return p

    @_('variable')
    def factor(self,p):
        return p

    @_('INTCONST')
    def factor(self,p):
        return p

    @_('CHARCONST')
    def factor(self,p):
        return p

    @_('LPAR expression RPAR')
    def factor(self,p):
        return p

    @_('NOT factor')
    def factor(self,p):
        return p

    @_('EQ')
    def relational_operator(self,p):
        return p

    @_('NE')
    def relational_operator(self,p):
        return p

    @_('LT')
    def relational_operator(self,p):
        return p

    @_('LE')
    def relational_operator(self,p):
        return p

    @_('GE')
    def relational_operator(self,p):
        return p

    @_('GT')
    def relational_operator(self,p):
        return p

    @_('PLUS')
    def sign(self,p):
        return p

    @_('MINUS')
    def sign(self,p):
        return p

    @_('empty')
    def sign(self,p):
        return p

    @_('PLUS')
    def adding_operator(self,p):
        return p

    @_('MINUS')
    def adding_operator(self,p):
        return p

    @_('OR')
    def adding_operator(self,p):
        return p

    @_('TIMES')
    def multiplying_operator(self,p):
        return p

    @_('DIV')
    def multiplying_operator(self,p):
        return p

    @_('AND')
    def multiplying_operator(self,p):
        return p

    @_('entire_variable')
    def variable(self,p):
        return p

    @_('indexed_variable')
    def variable(self,p):
        return p

    @_('array_variable LBR expression RBR')
    def indexed_variable(self,p):
        return p

    @_('entire_variable')
    def array_variable(self,p):
        return p

    @_('variable_identifier')
    def entire_variable(self,p):
        return p

    @_('ID')
    def variable_identifier(self,p):
        line = p.lineno
        index = p.index
        return p

    @_('ID')
    def identifier(self,p):
        line = p.lineno
        index = p.index
        return p

    @_('')
    def empty(self,p):
        return p

if __name__ == '__main__':
    lexer = PascalLexer()
    parser = PasParser()
    toopen = open('tests/test1.pas')
    code = toopen.read()
    result = parser.parse(lexer.tokenize(code))
    print(result)
