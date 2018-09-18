from sly import Parser
from paslex import PascalLexer

class PasParser(Parser):

    tokens = PascalLexer.tokens

    @_('PROGRAM identifier SEMICOLON block DOT')
    def program(self,p):
        pass

    @_('variable_declaration_part procedure_declaration_part statement_part')
    def block(self,p):
        pass

    @_('empty')
    def variable_declaration_part(self,p):
        pass

    @_('VAR list_variable_declaration')
    def variable_declaration_part(self,p):
        pass

    @_('var_declaration SEMICOLON')
    def list_variable_declaration(self,p):
        pass

    @_('list_variable_declaration var_declaration')
    def list_variable_declaration(self,p):
        pass

    @_('identifier COLON type')
    def var_declaration(seld,p):
        pass

    @_('list_identifier')
    def var_declaration(self,p):
        pass

    @_('identifier COMA')
    def list_identifier(self,p):
        pass

    @_('list_identifier')
    def list_identifier(self,p):
        pass

    @_('simple_type')
    def type(self,p):
        pass

    @_('array_type')
    def type(self,p):
        pass

    @_('ARRAY LBR index_range RBR OF simple_type')
    def array_type(self,p):
        pass

    @_('INTCONST DOT DOT INTCONST')
    def index_range(self,p):
        pass

    @_('type_identifier')
    def simple_type(self,p):
        pass

    @_('identifier')
    def type_identifier(self,p):
        pass

    @_('list_procedure_declaration')
    def procedure_declaration_part(self,p):
        pass

    @_('empty')
    def list_procedure_declaration(self,p):
        pass

    @_('procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        pass

    @_('list_procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        pass

    @_('PROCEDURE ID SEMICOLON block')
    def procedure_declaration(self,p):
        pass

    @_('compound_statement')
    def statement_part(self,p):
        pass

    @_('BEGIN list_statement END')
    def compound_statement(self,p):
        pass

    @_('statement')
    def list_statement(self,p):
        pass

    @_('SEMICOLON list_statement SEMICOLON statement')
    def list_statement(self,p):
        pass

    @_('simple_statement')
    def statement(self,p):
        pass

    @_('structured_statement')
    def statement(self,p):
        pass

    @_('assignament_statement')
    def simple_statement(self,p):
        pass

    @_('procedure_statement')
    def simple_statement(self,p):
        pass

    @_('read_statement')
    def simple_statement(self,p):
        pass

    @_('write_statement')
    def simple_statement(self,p):
        pass

    @_('variable ASSIGN expression')
    def assignament_statement(self,p):
        pass

    @_('procedure_identifier')
    def procedure_statement(self,p):
        pass

    @_('identifier')
    def procedure_identifier(self,p):
        pass

    @_('READ LPAR list_input_variable RPAR')
    def read_statement(self,p):
        pass

    @_('input_variable')
    def list_input_variable(self,p):
        pass

    @_('list_input_variable COMA input_variable')
    def list_input_variable(self,p):
        pass

    @_('variable')
    def input_variable(self,p):
        pass

    @_('WRITE LPAR list_output_value RPAR')
    def write_statement(self,p):
        pass

    @_('output_value')
    def list_output_value(self,p):
        pass

    @_('list_output_value COMA output_value')
    def list_output_value(self,p):
        pass

    @_('expression')
    def output_value(self,p):
        pass

    @_('compound_statement')
    def structured_statement(self,p):
        pass

    @_('if_statement')
    def structured_statement(self,p):
        pass

    @_('while_statement')
    def structured_statement(self,p):
        pass

    @_('IF expression THEN statement')
    def if_statement(self,p):
        pass

    @_('IF expression THEN statement ELSE statement')
    def if_statement(self,p):
        pass

    @_('WHILE expression DO statement')
    def while_statement(self,p):
        pass

    @_('simple_expression')
    def expression(self,p):
        pass

    @_('simple_expression relational_operator simple_expression')
    def expression(self,p):
        pass

    @_('sign term list_adding_term')
    def simple_expression(self,p):
        pass

    @_('adding_operator term')
    def list_adding_term(self,p):
        pass

    @_('empty')
    def list_adding_term(self,p):
        pass

    @_('list_adding_term adding_operator term')
    def list_adding_term(self,p):
        pass

    @_('factor list_mult_factor')
    def term(self,p):
        pass

    @_('multiplying_operator factor')
    def list_mult_factor(self,p):
        pass

    @_('empty')
    def list_mult_factor(self,p):
        pass

    @_('list_mult_factor factor')
    def list_mult_factor(self,p):
        pass

    @_('variable')
    def factor(self,p):
        pass

    @_('INTCONST')
    def factor(self,p):
        pass

    @_('CHARCONST')
    def factor(self,p):
        pass

    @_('LPAR expression RPAR')
    def factor(self,p):
        pass

    @_('NOT factor')
    def factor(self,p):
        pass

    @_('EQ')
    def relational_operator(self,p):
        pass

    @_('NE')
    def relational_operator(self,p):
        pass

    @_('LT')
    def relational_operator(self,p):
        pass

    @_('LE')
    def relational_operator(self,p):
        pass

    @_('GE')
    def relational_operator(self,p):
        pass

    @_('GT')
    def relational_operator(self,p):
        pass

    @_('PLUS')
    def sign(self,p):
        pass

    @_('MINUS')
    def sign(self,p):
        pass

    @_('empty')
    def sign(self,p):
        pass

    @_('PLUS')
    def adding_operator(self,p):
        pass

    @_('MINUS')
    def adding_operator(self,p):
        pass

    @_('OR')
    def adding_operator(self,p):
        pass

    @_('TIMES')
    def multiplying_operator(self,p):
        pass

    @_('DIV')
    def multiplying_operator(self,p):
        pass

    @_('AND')
    def multiplying_operator(self,p):
        pass

    @_('entire_variable')
    def variable(self,p):
        pass

    @_('indexed_variable')
    def variable(self,p):
        pass

    @_('array_variable LBR expression RBR')
    def indexed_variable(self,p):
        pass

    @_('entire_variable')
    def array_variable(self,p):
        pass

    @_('variable_identifier')
    def entire_variable(self,p):
        pass

    @_('ID')
    def variable_identifier(self,p):
        pass

    @_('ID')
    def identifier(self,p):
        pass

    @_('')
    def empty(self,p):
        pass
