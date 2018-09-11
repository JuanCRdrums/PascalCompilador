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

    @_('integer_constant DOT DOT integer_constant')
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

    @_('procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        pass

    @_('list_procedure_declaration SEMICOLON procedure_declaration')
    def list_procedure_declaration(self,p):
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
