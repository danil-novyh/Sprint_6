import pytest
import allure
from pages.main_page import MainPage
from data import FAQData

class TestFAQ:
    @allure.title("Проверка раскрытия ответа на вопрос в разделе «Вопросы о важном»")
    @pytest.mark.parametrize("index, expected", FAQData.QUESTIONS_ANSWERS)
    def test_faq_answers(self, driver, index, expected):
        page = MainPage(driver)
        page.accept_cookies()
        page.click_faq_question(index)
        actual = page.get_faq_answer(index)
        assert actual == expected
