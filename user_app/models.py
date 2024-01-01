from django.db import models
from django.contrib.auth.models import AbstractBaseUser , AbstractUser
from django.urls import reverse , reverse_lazy
from django.utils.text import slugify

class Sex(models.Model):
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.sex

from django.utils.text import slugify

class MyCustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True)
    email = models.EmailField(null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, unique=True)
    phone = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('user', kwargs={'slug': self.slug})

    def convert_to_latin_characters(self, text):
        # Тут ви можете вручну визначити відповідності між кириличними та латинськими літерами
        translation_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
            'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
            'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ь': '', 'ю': 'iu', 'я': 'ia'
        }

        return ''.join([translation_dict.get(char, char) for char in text])

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.convert_to_latin_characters(self.username))
            unique_slug = base_slug
            counter = 1

            while MyCustomUser.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)


    # def __str__(self):
    #     return self.email