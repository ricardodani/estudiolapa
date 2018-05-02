import logging
from django.db import models
from django.utils.text import slugify
from thumbnails import get_thumbnail


logger = logging.getLogger(__name__)


class _BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    THUMBNAIL_SPECS = ()

    @property
    def slug(self):
        return slugify(self.title)

    def _get_thumbnail(self, size="200x200", crop="center"):
        if self.image:
            try:
                return get_thumbnail(self.image.file.name, size, crop=crop)
            except Exception as e:
                logger.error(e)

    @property
    def resized_image(self):
        return self._get_thumbnail(*self.THUMBNAIL_SPECS)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


BACKGROUND_PLACES = (
    ('bg_logo', 'Fundo da Logo'),
    ('bg_fazemos', 'Fundo do O que fazemos?'),
)
class Background(_BaseModel):

    title = models.CharField(max_length=255, verbose_name=u'Título')
    place = models.CharField(max_length=20, choices=BACKGROUND_PLACES,
                             verbose_name='Local', default='BG Logo')
    THUMBNAIL_SPECS = ("1920x1275", "center")

    class Meta:
        verbose_name = 'Plano de Fundo'
        verbose_name_plural = 'Planos de Fundo'
        get_latest_by = 'updated_at'


class Category(_BaseModel):

    title = models.CharField(max_length=255, verbose_name=u'Título')
    description = models.TextField(null=True, blank=True, verbose_name=u'Descrição')
    THUMBNAIL_SPECS = ("750x500", "center")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class CategoryPhoto(_BaseModel):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=u'Título')
    THUMBNAIL_SPECS = ("80x80", "center")

    @property
    def slide_image(self):
        return self._get_thumbnail("1024", None)

    class Meta:
        verbose_name = 'Foto de Categoria'
        verbose_name_plural = 'Fotos de Categorias'


class Work(_BaseModel):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=u'Título')
    description = models.TextField(null=True, blank=True, verbose_name=u'Descrição')
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    vimeo_url = models.CharField(max_length=255, null=True, blank=True)
    THUMBNAIL_SPECS = ("750x500", "center")

    class Meta:
        verbose_name = 'Trabalho Realizado'
        verbose_name_plural = 'Trabalhos Realizados'


class WorkPhoto(_BaseModel):

    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=u'Título')
    THUMBNAIL_SPECS = ("80x80", "center")

    @property
    def slide_image(self):
        return self._get_thumbnail("1024", None)

    class Meta:
        verbose_name = 'Foto de Trabalho Realizado'
        verbose_name_plural = 'Fotos de Trabalhos Realizados'
