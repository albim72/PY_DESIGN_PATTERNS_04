from typing import Any

class Product1:
    def __init__(self) -> None:
        self.parts = []
    
    def add(self,part:Any) -> None:
        self.parts.append(part)
        
    def list_parts(self):
        print(f'części produktu: {", ".join(self.parts)}',end="")
