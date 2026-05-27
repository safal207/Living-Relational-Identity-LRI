# Living-Relational-Identity (LRI) — Беклог задач

## Условные обозначения

| Метка | Значение |
|---|---|
| P0 | Блокер / критично |
| P1 | Важно |
| P2 | Желательно |
| P3 | Улучшение |

---

## Фаза 0: Фундамент (P0)

- [#39](https://github.com/safal207/Living-Relational-Identity-LRI/issues/39) **Добавить лицензию** (MIT / Apache 2.0)
- [#41](https://github.com/safal207/Living-Relational-Identity-LRI/issues/41) **Вынести секреты** — пароли, JWT-ключи, API-ключи в переменные окружения / `.env`
- [#44](https://github.com/safal207/Living-Relational-Identity-LRI/issues/44) **Исправить систему импортов** — заменить `sys.path.append()` на `pyproject.toml` + `pip install -e .`
- [#48](https://github.com/safal207/Living-Relational-Identity-LRI/issues/48) **Унифицировать язык** — весь код и комменты на английском

## Фаза 1: Инфраструктура (P0–P1)

- [#40](https://github.com/safal207/Living-Relational-Identity-LRI/issues/40) **Добавить Docker** — `Dockerfile` + `docker-compose.yml` для reference implementation
- [#42](https://github.com/safal207/Living-Relational-Identity-LRI/issues/42) **Настроить CI (GitHub Actions)** — автоматический прогон тестов, валидации, линтера при push/PR
- [#45](https://github.com/safal207/Living-Relational-Identity-LRI/issues/45) **Добавить pre-commit** — ruff (линтер), black (форматтер), проверка YAML
- [#49](https://github.com/safal207/Living-Relational-Identity-LRI/issues/49) **Создать Makefile / Taskfile** — стандартные команды: `test`, `run`, `validate`, `clean`

## Фаза 2: Персистентность (P0)

- [#43](https://github.com/safal207/Living-Relational-Identity-LRI/issues/43) **Добавить БД** — SQLite для dev, PostgreSQL для prod
- [#46](https://github.com/safal207/Living-Relational-Identity-LRI/issues/46) **Переписать in-memory storage (`subjects = {}`)** на репозиторий с БД
- [#52](https://github.com/safal207/Living-Relational-Identity-LRI/issues/52) **Добавить миграции** — Alembic или аналог
- [#54](https://github.com/safal207/Living-Relational-Identity-LRI/issues/54) **Сохранять DMP-лог в БД, а не в JSONL-файл**

## Фаза 3: Безопасность (P1)

- [#47](https://github.com/safal207/Living-Relational-Identity-LRI/issues/47) **Реализовать нормальную авторизацию** — убрать заглушку `all subjects are authorized`
- [#50](https://github.com/safal207/Living-Relational-Identity-LRI/issues/50) **Реальная криптография** — проверка подписей, работа с ключами
- [#51](https://github.com/safal207/Living-Relational-Identity-LRI/issues/51) **Добавить scopes/роли** — admin, agent, observer с разграничением
- [#53](https://github.com/safal207/Living-Relational-Identity-LRI/issues/53) **Добавить rate limiting и аудит запросов**

## Фаза 4: Тестирование (P1)

- [#55](https://github.com/safal207/Living-Relational-Identity-LRI/issues/55) **Покрыть API-роуты** — FastAPI TestClient для subject, relations, authority, observer
- [#56](https://github.com/safal207/Living-Relational-Identity-LRI/issues/56) **Покрыть адаптеры** — CLI, UI, multi-agent
- [#58](https://github.com/safal207/Living-Relational-Identity-LRI/issues/58) **Добавить code coverage** — `pytest-cov` с порогом > 70%
- [#60](https://github.com/safal207/Living-Relational-Identity-LRI/issues/60) **Интегрировать Playwright-тест** в pytest как `@pytest.mark.e2e`
- [#64](https://github.com/safal207/Living-Relational-Identity-LRI/issues/64) **Добавить property-based testing** — Hypothesis для инвариантов протокола

## Фаза 5: Качество кода (P2)

- [#57](https://github.com/safal207/Living-Relational-Identity-LRI/issues/57) **Добавить typing** — аннотации во все функции
- [#59](https://github.com/safal207/Living-Relational-Identity-LRI/issues/59) **Вынести HTML/CSS/JS из Python** — Jinja2 шаблоны для `alice_demo_server.py` и `ui_adapter.py`
- [#61](https://github.com/safal207/Living-Relational-Identity-LRI/issues/61) **Заменить `print()` на `logging`**
- [#65](https://github.com/safal207/Living-Relational-Identity-LRI/issues/65) **Добавить обработку ошибок** — для edge-кейсов во всех роутах и сервисах
- [#68](https://github.com/safal207/Living-Relational-Identity-LRI/issues/68) **Добавить конфигурацию через Pydantic Settings**

## Фаза 6: Улучшение протокола (P2)

- [#62](https://github.com/safal207/Living-Relational-Identity-LRI/issues/62) **Автоматическая валидация YAML-схем** — прогонять валидатор на `protocol/`
- [#67](https://github.com/safal207/Living-Relational-Identity-LRI/issues/67) **Добавить OpenAPI/Swagger** — описание API поверх того, что генерирует FastAPI
- [#69](https://github.com/safal207/Living-Relational-Identity-LRI/issues/69) **Добавить примеры на других языках** — TypeScript / Rust / Go

## Фаза 7: Документация (P2)

- [#63](https://github.com/safal207/Living-Relational-Identity-LRI/issues/63) **Добавить архитектурные диаграммы** — Mermaid-схемы в docs/
- [#66](https://github.com/safal207/Living-Relational-Identity-LRI/issues/66) **Обновить документы** — убрать ссылки на PR, которые уже вмержены
- [#70](https://github.com/safal207/Living-Relational-Identity-LRI/issues/70) **Добавить CONTRIBUTING.md** — как контрибьютить

## Фаза 8: Операции (P3)

- [#71](https://github.com/safal207/Living-Relational-Identity-LRI/issues/71) **Добавить health-check эндпоинт** — `/health`
- [#72](https://github.com/safal207/Living-Relational-Identity-LRI/issues/72) **Добавить метрики** — Prometheus + Grafana
- [#73](https://github.com/safal207/Living-Relational-Identity-LRI/issues/73) **Graceful shutdown** — корректное завершение сервера
- [#74](https://github.com/safal207/Living-Relational-Identity-LRI/issues/74) **Backup стратегия** — для DMP и состояния идентичностей
