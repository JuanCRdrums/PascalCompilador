from sly import Parser

class Program:
    def __init__(self,id,block):
        self.id = id
        self.block = block

class Block:
    def __init(self,vardec,procdec,stat):
        self.vardec = vardec
        self.procdec = procdec
        self.stat = stat
