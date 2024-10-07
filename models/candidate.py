class Candidato:
    def __init__(self, first_name, middle_name, last_name, email, contact_number):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.contact_number = contact_number
        self.status = "Application Initiated"  # Estado inicial

    def __str__(self):
        return f"Candidato: {self.first_name} {self.middle_name} {self.last_name} - {self.email}"

    def actualizar_estado(self, nuevo_estado):
        """Actualizar el estado del candidato."""
        self.status = nuevo_estado

    def obtener_info(self):
        """Obtener información del candidato."""
        return {
            "nombre_completo": f"{self.first_name} {self.middle_name} {self.last_name}",
            "email": self.email,
            "contact_number": self.contact_number,
            "estado": self.status
        }
