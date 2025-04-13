from django.db import models


class FaqItem(models.Model):
    question = models.CharField(max_length=255, verbose_name="Pergunta")
    answer = models.TextField(verbose_name="Resposta")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Pergunta e resposta"
        verbose_name_plural = "Perguntas e respostas"


class Faq(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título", default="FAQ")
    subtitle = models.CharField(
        max_length=255,
        verbose_name="Subtítulo",
        default="Here are some of our Frequently Asked Questions. If you have any other questions you'd like answered please feel free to contact me.",
    )
    questions = models.ManyToManyField(FaqItem)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sessão de perguntas e respostas"
