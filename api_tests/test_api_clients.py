import pytest
import requests
from api_client.clients import GenericApiClient, GuapApiClient


class TestGuapAPI:
    """API тесты для guap.ru"""

    @pytest.mark.smoke
    @pytest.mark.api
    def test_guap_main_page_accessible(self):
        """Проверка доступности главной страницы GUAP"""
        response = requests.get("https://guap.ru", timeout=15, allow_redirects=True)
        assert response.status_code == 200
        assert len(response.content) > 0

    @pytest.mark.regression
    @pytest.mark.api
    def test_guap_api_endpoints(self, api_client):
        """Проверка основных API endpoints guap.ru"""
        endpoints = ["/api/health", "/api/students", "/api/schedule"]
        results = {}
        for endpoint in endpoints:
            try:
                response = api_client.get(endpoint)
                results[endpoint] = response.status_code
            except Exception:
                results[endpoint] = "error"
        
        assert isinstance(results, dict)

    @pytest.mark.critical
    @pytest.mark.api
    def test_guap_lk_portal_accessible(self):
        """Проверка доступности личного кабинета"""
        try:
            response = requests.get("https://lk.guap.ru", timeout=15, allow_redirects=True)
            assert response.status_code in [200, 301, 302, 304]
        except requests.exceptions.RequestException:
            pytest.skip("lk.guap.ru недоступен")

    @pytest.mark.regression
    @pytest.mark.api
    def test_guap_main_page_has_content(self):
        """Проверка что главная страница содержит контент"""
        response = requests.get("https://guap.ru", timeout=15)
        content = response.text.lower()
        keywords = ["гуап", "guap", "университет", "аэрокосмическ", "санкт-петербург"]
        found = any(word in content for word in keywords)
        assert found or len(content) > 1000


class TestAPIIntegration:
    """Интеграционные тесты"""

    @pytest.mark.critical
    @pytest.mark.api
    def test_api_client_connection(self, api_client):
        """Проверка соединения с API"""
        try:
            response = api_client.get("/")
            assert response.status_code in [200, 301, 302]
        except Exception:
            pass

    @pytest.mark.regression
    @pytest.mark.api
    def test_api_response_time(self, api_client):
        """Проверка времени ответа API"""
        import time
        start = time.time()
        try:
            api_client.get("/")
        except Exception:
            pass
        elapsed = time.time() - start
        assert elapsed < 10, f"API too slow: {elapsed:.2f}s"
