from sly import Parser



class Program:
    def __init__(self,id,block):
        self.id = id
        self.block = block

class Block:
    def __init__(self,vardec,procdec,stat):
        self.vardec = vardec
        self.procdec = procdec
        self.stat = stat

class VariableDeclatarionPart:
    def __init__(self,listDeclaration = None):
        self.listDeclaration = listDeclaration

class ListVariableDeclaration:
    def __init__(self,varDeclaration = None,listVarDeclaration = None):
        self.varDeclaration = varDeclaration
        self.listVarDeclaration = listVarDeclaration

class VarDeclaration:
    def __init__(self,identifier = None,type = None,listIdentifier = None):
        self.identifier = identifier
        self.type = type
        self.listIdentifier = listIdentifier

class ListIdentifier:
    def __init__(self,identifier = None,listIdentifier = None):
        self.identifier = identifier
        self.listIdentifier = listIdentifier

class Type:
    def __init__(self,type):
        self.type = type

class ArrayType:
    def __init__(self,indexRange,simpleType):
        self.indexRange = indexRange
        self.simpleType = simpleType

class IndexRange:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

class SimpleType:
    def __init__(self,typeId):
        self.typeId = typeId

class TypeIdentifier:
    def __init__(self,id):
        self.id = id

class ListProcedureDeclaration:
    def __init__(self,listProcedureDeclaration = None,procedureDeclaration = None):
        self.listProcedureDeclaration = listProcedureDeclaration
        self.procedureDeclaration = procedureDeclaration

class ProcedureDeclaration:
    def __init__(self,id,block):
        self.id = id
        self.block = block

class StatementPart:
    def __init__(self,compound):
        self.compound = compound

class CompoundStatement:
    def __init__(self,statement,listStatement):
        self.statement = statement
        self.listStatement = listStatement

class ListStatement:
    def __init__(self,statement = None, listStatement = None):
        self.statement = statement
        self.listStatement = listStatement

class Statement:
    def __init__(self,statement):
        self.statement = statement

class SimpleStatement:
    def __init__(self,statement):
        self.statement = statement

class AssignamentStatement:
    def __init__(self,variable,expression):
        self.variable = variable
        self.expression = expression

class ProcedureStatement:
    def __init__(self,id):
        self.id = id

class ProcedureIdentifier:
    def __init__(self,id):
        self.id = id

class ReadStatement:
    def __init__(self,list):
        self.list = list

class ListInputVariable:
    def __init__(self,variable,list = None):
        self.variable = variable
        self.list = list

class InputVariable:
    def __init__(self,variable):
        self.variable = variable

class WriteStatement:
    def __init__(self,list):
        self.list = list

class ListOutputValue:
    def __init__(self,value,list = None):
        self.value = value
        self.list = list

class OutputValue:
    def __init__(self,expression):
        self.expression = expression

class StructuredStatement:
    def __init__(self,statement):
        self.statement = statement

class IfStatement:
    def __init__(self,expression,statement1,statement2 = None):
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

class WhileStatement:
    def __init__(self,expression,statement):
        self.expression = expression
        self.statement = statement

class Expression:
    def __init__(self,simple1,relational = None, simple2 = None):
        self.simple1 = simple1
        self.relational = relational
        self.simple2 = simple2

class SimpleExpression:
    def __init__(self,sign,term,list):
        self.sign = sign
        self.term = term
        self.list = list

class ListAddingTerm:
    def __init__(self,list = None,op = None,term = None):
        self.list = list
        self.op = op
        self.term = term

class Term:
    def __init__(self,factor,list):
        self.factor = factor
        self.list = list

class ListMultFactor:
    def __init__(self,list = None,op = None,factor = None):
        self.list = list
        self.op = op
        self.factor = factor

class Factor:
    def __init__(self,element):
        self.element = element

class RelationalOperator:
    def __init__(self,op):
        self.op = op

class Sign:
    def __init__(self,element = None):
        self.element = element

class AddingOperator:
    def __init__(self,element):
        self.element = element

class MultiplyingOperator:
    def __init__(self,element):
        self.element = element

class Variable:
    def __init__(self,var):
        self.var = var

class IndexedVariable:
    def __init__(self,var,exp):
        self.var = var
        self.exp = exp

class ArrayVariable:
    def __init__(self,var):
        self.var = var

class EntireVariable:
    def __init__(self,var):
        self.var = var

class VarID:
    def __init__(self,id):
        self.id = id
class Id:
    def __init__(self,id):
        self.id = id

class Empty:
    pass

class NodeVisitor(object):
	def visit(self, node):
		'''
		Enecuta un metodo de la forma visit_NodeName(node) donde
		NodeName es el nombre de la clase de un nodo particular.
		if isinstance(node, list):
			for item in node:
				self.visit(item)
		elif isinstance(node, AST):
			method = 'visit_' + node.__class__.__name__
			visitor = getattr(self, method, self.generic_visit)
			visitor(node)
		'''
		attr = [i for i in node.__dict__.keys() if i[:1] != '_']
		for i in attr:
			print(i)

	def generic_visit(self,node):
		for field in getattr(node, '_fields'):
			value = getattr(node, field, None)
			self.visit(value)

	@classmethod
	def __init_subclass__(cls):
		for key in vars(cls):
			if key.startswith('visit_'):
				assert key[6:] in globals(), f"{key} no coincide con nodos AST"

# NO MODIFICAR
def flatten(top):
	class Flattener(NodeVisitor):
		def __init__(self):
			self.depth = 0
			self.nodes = []
		def generic_visit(self, node):
			self.nodes.append((self.depth, node))
			self.depth += 1
			NodeVisitor.generic_visit(self, node)
			self.depth -= 1

	d = Flattener()
	d.visit(top)
	return d.nodes
