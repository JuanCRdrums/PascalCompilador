from sly import Parser
from paslex import PascalLexer
from astobjects import *
from astmonkey import visitors,transformers



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
        return Program(p.identifier,p.block)

    @_('variable_declaration_part procedure_declaration_part statement_part')
    def block(self,p):
        return Block(p.variable_declaration_part,p.procedure_declaration_part,p.statement_part)

    @_('empty')
    def variable_declaration_part(self,p):
        return Empty()

    @_('VAR list_variable_declaration')
    def variable_declaration_part(self,p):
        return VariableDeclatarionPart(p.list_variable_declaration)

    @_('var_declaration SEMICOLON')
    def list_variable_declaration(self,p):
        return ListVariableDeclaration([p.var_declaration])

    @_('var_declaration SEMICOLON list_variable_declaration')
    def list_variable_declaration(self,p):
        p.list_variable_declaration.append(p.var_declaration)
        return ListVariableDeclaration(p.list_variable_declaration)

    @_('identifier COLON type')
    def var_declaration(self,p):
        return VarDeclaration(p.identifier,p.type,None)

    @_('list_identifier COLON type')
    def var_declaration(self,p):
        return VarDeclaration(None,p.type,p.list_identifier)

    @_('identifier')
    def list_identifier(self,p):
        return ListIdentifier([p.identifier])

    @_('identifier COMA list_identifier')
    def list_identifier(self,p):
        p.list_identifier.append(p.identifier)
        return ListIdentifier(p.list_identifier)

    @_('simple_type')
    def type(self,p):
        return Type(p.simple_type)

    @_('array_type')
    def type(self,p):
        return Type(p.array_type)

    @_('ARRAY LBR index_range RBR OF simple_type')
    def array_type(self,p):
        return ArrayType(p.index_range,p.simple_type)

    @_('INTCONST DOT DOT INTCONST')
    def index_range(self,p):
        return IndexRange(p[0],p[2])

    @_('type_identifier')
    def simple_type(self,p):
        return SimpleType(p.type_identifier)

    @_('identifier')
    def type_identifier(self,p):
        return TypeIdentifier(p.identifier)

    @_('list_procedure_declaration')
    def procedure_declaration_part(self,p):
        return ListProcedureDeclaration(p.list_procedure_declaration)

    @_('empty')
    def list_procedure_declaration(self,p):
        return ListProcedureDeclaration([])

    @_('procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        return ListProcedureDeclaration([p.procedure_declaration])

    @_('list_procedure_declaration procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        p.list_procedure_declaration.append(p.procedure_declaration)
        return ListProcedureDeclaration(p.list_procedure_declaration)

    @_('PROCEDURE ID SEMICOLON block')
    def procedure_declaration(self,p):
        return ProcedureDeclaration(p[1],p.block)

    @_('compound_statement')
    def statement_part(self,p):
        return StatementPart(p.compound_statement)

    @_('BEGIN statement list_statement END')
    def compound_statement(self,p):
        return CompoundStatement(p.statement,p.list_statement)

    @_('SEMICOLON statement list_statement')
    def list_statement(self,p):
        p.list_statement.append(p.statement)
        return ListStatement(p.list_statement)

    @_('empty')
    def list_statement(self,p):
        return ListStatement([])

    @_('simple_statement')
    def statement(self,p):
        return Statement(p.simple_statement)

    @_('structured_statement')
    def statement(self,p):
        return Statement(p.structured_statement)

    @_('assignament_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.assignament_statement)

    @_('procedure_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.procedure_statement)

    @_('read_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.read_statement)

    @_('write_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.write_statement)

    @_('variable ASSIGN expression')
    def assignament_statement(self,p):
        return AssignamentStatement(p.variable,p.expression)

    @_('procedure_identifier')
    def procedure_statement(self,p):
        return ProcedureStatement(p.procedure_identifier)

    @_('identifier')
    def procedure_identifier(self,p):
        return ProcedureIdentifier(p.identifier)

    @_('READ LPAR list_input_variable RPAR')
    def read_statement(self,p):
        return ReadStatement(p.list_input_variable)

    @_('input_variable')
    def list_input_variable(self,p):
        return ListInputVariable([p.input_variable])

    @_('list_input_variable COMA input_variable')
    def list_input_variable(self,p):
        p.list_input_variable.append(p.input_variable)
        return ListInputVariable(p.list_input_variable)

    @_('variable')
    def input_variable(self,p):
        return InputVariable(p.variable)

    @_('WRITE LPAR list_output_value RPAR')
    def write_statement(self,p):
        return WriteStatement(p.list_output_value)

    @_('output_value')
    def list_output_value(self,p):
        return ListOutputValue([p.output_value])

    @_('list_output_value COMA output_value')
    def list_output_value(self,p):
        p.list_output_value.append(p.output_value)
        return ListOutputValue(p.list_output_value)

    @_('expression')
    def output_value(self,p):
        return OutputValue(p.expression)

    @_('compound_statement')
    def structured_statement(self,p):
        return StructuredStatement(p.compound_statement)

    @_('if_statement')
    def structured_statement(self,p):
        return StructuredStatement(p.if_statement)

    @_('while_statement')
    def structured_statement(self,p):
        return StructuredStatement(p.while_statement)

    @_('IF expression THEN statement')
    def if_statement(self,p):
        return IfStatement(p.expression,p.statement,None)

    @_('IF expression THEN statement ELSE statement')
    def if_statement(self,p):
        return IfStatement(p.expression,p.statement0,p.statement1)

    @_('WHILE expression DO statement')
    def while_statement(self,p):
        return WhileStatement(p.expression,p.statement)

    @_('simple_expression')
    def expression(self,p):
        return Expression(p.simple_expression,None,None)

    @_('simple_expression relational_operator simple_expression')
    def expression(self,p):
        return Expression(p.simple_expression0,p.relational_operator,p.simple_expression1)

    @_('sign term list_adding_term')
    def simple_expression(self,p):
        return SimpleExpression(p.sign,p.term,p.list_adding_term)

    @_('empty')
    def list_adding_term(self,p):
        return ListAddingTerm([])

    @_('list_adding_term adding_operator term')
    def list_adding_term(self,p):
        p.list_adding_term.append(p.adding_operator,p.term)
        return ListAddingTerm(p.list_adding_term)

    @_('factor list_mult_factor')
    def term(self,p):
        return Term(p.factor,p.list_mult_factor)

    @_('empty')
    def list_mult_factor(self,p):
        return ListMultFactor([])

    @_('list_mult_factor multiplying_operator factor')
    def list_mult_factor(self,p):
        p.list_mult_factor.append(p.multiplying_operator,p.factor)
        return ListMultFactor(p.list_mult_factor)

    @_('variable')
    def factor(self,p):
        return Factor(p.variable)

    @_('INTCONST')
    def factor(self,p):
        return Factor(p)

    @_('CHARCONST')
    def factor(self,p):
        return Factor(p)

    @_('LPAR expression RPAR')
    def factor(self,p):
        return Factor(p.expression)

    @_('NOT factor')
    def factor(self,p):
        return Factor(p.factor)

    @_('EQ')
    def relational_operator(self,p):
        return RelationalOperator(p)

    @_('NE')
    def relational_operator(self,p):
        return RelationalOperator(p)

    @_('LT')
    def relational_operator(self,p):
        return RelationalOperator(p)

    @_('LE')
    def relational_operator(self,p):
        return RelationalOperator(p)

    @_('GE')
    def relational_operator(self,p):
        return RelationalOperator(p)

    @_('GT')
    def relational_operator(self,p):
        return RelationalOperator(p)

    @_('PLUS')
    def sign(self,p):
        return Sign(p)

    @_('MINUS')
    def sign(self,p):
        return Sign(p)

    @_('empty')
    def sign(self,p):
        return Sign(None)

    @_('PLUS')
    def adding_operator(self,p):
        return AddingOperator(p)

    @_('MINUS')
    def adding_operator(self,p):
        return AddingOperator(p)

    @_('OR')
    def adding_operator(self,p):
        return AddingOperator(p)

    @_('TIMES')
    def multiplying_operator(self,p):
        return MultiplyingOperator(p)

    @_('DIV')
    def multiplying_operator(self,p):
        return MultiplyingOperator(p)

    @_('AND')
    def multiplying_operator(self,p):
        return MultiplyingOperator(p)

    @_('entire_variable')
    def variable(self,p):
        return Variable(p.entire_variable)

    @_('indexed_variable')
    def variable(self,p):
        return Variable(p.indexed_variable)

    @_('array_variable LBR expression RBR')
    def indexed_variable(self,p):
        return IndexedVariable(p.array_variable,p.expression)

    @_('entire_variable')
    def array_variable(self,p):
        return ArrayVariable(p.entire_variable)

    @_('variable_identifier')
    def entire_variable(self,p):
        return EntireVariable(p.variable_identifier)

    @_('ID')
    def variable_identifier(self,p):
        line = p.lineno
        index = p.index
        return VarID(p)

    @_('ID')
    def identifier(self,p):
        line = p.lineno
        index = p.index
        return Id(p[0])

    @_('')
    def empty(self,p):
        return Empty()

if __name__ == '__main__':
    lexer = PascalLexer()
    parser = PasParser()
    toopen = open('tests/test1.pas')
    code = toopen.read()
    result = parser.parse(lexer.tokenize(code))
    if result:
        print("Parser succesfully")
