
ARITHM_OPS = ["PLUS","MINUS","TIMES","DIV"]

REL_OPS = ["EQ","NE","LT","GT","LE","GE"]

BOOL_OPS = ["AND","OR"]

class Type():
    @classmethod
    def binOpType(cls,op, rightType):
        return None

    @classmethod
    def unaryOpType(cls,typeName):
        return None

    @classmethod
    def getByName(cls,typeName):
        for type_cls in cls.__subclasses__():
            if type_cls.name == typeName:
                return type_cls
        return None


class FloatType(Type):
    name = "float"

    @classmethod
    def binop_type(cls,op,rightType):
        
