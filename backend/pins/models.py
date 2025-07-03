from django.db import models

# Create your models here.

# --- Modelo Único: La Ruta o "Post" ---

class Ruta(models.Model):
    """
    Representa un "pin" o un post en el tablero de anuncios.
    No tiene dependencias de usuarios ni calificaciones.
    """

    # Opciones predefinidas para el tipo de transporte.
    # Ayuda a mantener los datos consistentes y facilita futuros filtros.
    TIPOS_TRANSPORTE = [
        ('BUS', 'Bus'),
        ('TROLE', 'Trolebús / Ecovía'),
        ('BICI', 'Bicicleta'),
        ('PIE', 'A pie'),
        ('AUTO', 'Auto'),
        ('OTRO', 'Otro'),
    ]

    titulo = models.CharField(max_length=200, help_text="Ej: Ruta Segura desde la PUCE al CCI en Trole")
    descripcion = models.TextField(help_text="Describe los pasos, paradas, y cualquier consejo útil.")
    punto_inicio = models.CharField(max_length=255, help_text="Ej: 'Universidad PUCE (Av. 12 de Octubre)'")
    punto_destino = models.CharField(max_length=255, help_text="Ej: 'Centro Comercial Iñaquito (CCI)'")
    tipo_transporte = models.CharField(max_length=10, choices=TIPOS_TRANSPORTE, default='BUS')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']