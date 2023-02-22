class Carrito:
    def __init__(self,request):
        self.request= request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito=self.session["carrito"]
        else:
            self.carrito=carrito
    
    
    def agregar(self, repuesto):
        id=str(repuesto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id":repuesto.id,
                "nombre":repuesto.nombre,
                "acumulado":repuesto.precio,
                "cantidad":1,                
            }
        else:
            if self.carrito[id]["cantidad"]< repuesto.cantidad:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += repuesto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, repuesto):
        id = str(repuesto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, repuesto):
        id = str(repuesto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= repuesto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(repuesto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True