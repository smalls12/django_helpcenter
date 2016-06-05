from django.core.urlresolvers import reverse
from django.test import TestCase

from helpcenter import utils
from helpcenter.testing_utils import create_article


class TestArticleDetailFunction(TestCase):
    """ Test cases for the article detail function """

    def test_call_with_article(self):
        """ Test calling the function with an Article instance.

        If the function is called with an Article instance, it should
        return the url for the detail view of that Article.
        """
        article = create_article()
        expected = reverse('article-detail', kwargs={'pk': article.pk})

        self.assertEqual(expected, utils.article_detail(article))

    def test_call_with_pk(self):
        """ Test calling the function with an Article's pk.

        If the function is called with the pk of an Article, it should
        return the url for the detail view of the article with that pk.
        """
        article = create_article()
        expected = reverse('article-detail', kwargs={'pk': article.pk})

        self.assertEqual(expected, utils.article_detail(pk=article.pk))

    def test_no_args(self):
        """ Test calling the function with no arguments.

        If the function is called with no arguments, it should raise a
        ValueError.
        """
        with self.assertRaises(ValueError):
            utils.article_detail()