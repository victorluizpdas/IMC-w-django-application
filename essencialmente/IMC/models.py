from django.db import models
from stdimage.models import StdImageField

# Create your models here.
class User(models.Model):

    masc = 'Masculino'
    fem = 'Feminino'

    sexo_choices = [
        (masc , 'Masculino'),
        (fem , 'Feminino')
    ]

    cpf = models.CharField('CPF', null=False, blank=False, max_length=11, unique=True, primary_key=True)
    nome = models.CharField('Nome', max_length=60, null=False, blank=False)
    datanascimento = models.DateField('Data nascimento', null=False, blank=False)
    escola = models.CharField('Escola', max_length=70,choices=sexo_choices, default=masc, null=False)
    sexo = models.CharField('Sexo', max_length=10, blank=True)
    peso = models.DecimalField('Peso',max_digits=5, decimal_places=2, blank=False, null=False)
    altura = models.DecimalField('Altura',max_digits=3, decimal_places=2, blank=False, null=False)
    imc = models.DecimalField('IMC',max_digits=4, decimal_places=2)
    image = StdImageField('Imagem', upload_to='produtos', null=False, default='user/sem_foto.png', variations={'thumb':(125,125)})

    def save(self, *args, **kwargs):
        if self.peso and self.altura:
            self.imc = self.peso/self.altura**2
        super(User, self).save(*args, **kwargs)


   
    def __str__(self):
        return self.nome
    