class ValidadorFormulario:
    @staticmethod
    def validar_tramite(estudiante, tipo, costo):
        if estudiante == "" or tipo == "":
            return False
        try:
            float(costo)
            return True
        except ValueError:
            return False