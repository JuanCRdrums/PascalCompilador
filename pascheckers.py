from errors import error
from astobjects import *
from typesys import *
from parser import *
import sys

class CheckProgramVisitor(NodeVisitor):

    def __init__(self):
        self.symbols = {}
        self.temp_symbols = {}
        self.expected_ret_type = None
        self.current_ret_type = None
        self.functions = {}
        self.keywords = [t.name for t in DType.__subclasses__()]

    def visit_OneVarDeclaration(self,node):
        if node.identifier.value in self.keywords:
            error(node.lineno, f"Nombre '{node.identifier.value}' no es un nombre legal para declaración de variable")
            return

        if node.identifier.value not in self.symbols:
            self.visit(node.type)
            node.type = node.type.type.type_identifier.identifier.value
            if node.type in self.keywords:
                self.symbols[node.identifier.value] = node.type
            else:
                error(node.lineno, f"Tipo desconocido '{node.type}'")
        else:
            error(node.lineno, f"'{node.identifier.value}' ya se ha definido")

    def visit_MuchVarDeclaration(self,node):
        print(self.visit_ListIdentifier(node.list_identifier))

    def visit_ListIdentifier(self,node):
        if not isinstance(node.identifier, list):
            self.visit_ListIdentifier(node.identifier)
        if isinstance(node.identifier, list):
            return node.identifier

#------------------------------------PRUEBA---------------------------------
def check_program(ast):
	checker = CheckProgramVisitor()

	checker.visit(ast)



def main():
	if len(sys.argv) < 2:

		sys.stderr.write('Uso: python -m mpascal.checker filename\n')

		raise SystemExit(1)

	parse = PasParser()

	lexer = PascalLexer()
	parser = PasParser()
	toopen = open(sys.argv[1])
	code = toopen.read()
	ast = parser.parse(lexer.tokenize(code))
	check_program(ast)

	if '--show-types' in sys.argv:

		for depth, node in flatten(ast):

			print('%s: %s%s type: %s' % (getattr(node, 'lineno', None), ' '*(4*depth), node,

			getattr(node, 'type', None)))



if __name__ == '__main__':

	main()
