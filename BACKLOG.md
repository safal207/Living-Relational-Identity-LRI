# Living-Relational-Identity (LRI) — Roadmap

## Track structure

| Track | Focus | Примеры задач |
|---|---|---|
| **Track A** — Reviewer clarity | Позиционирование, non-claims, объяснимость | #38 (done), #29 |
| **Track B** — Research/spec concepts | Примеры, глоссарий, концепты | #30, #31, #32, #33, #34, #37 |
| **Track C** — Engineering hygiene | CI, тесты, код, структура | #42, #44, #45, #48, #49, #55–#62, #64–#65, #67–#68, #70 |
| **Track D** — Security hardening | Секреты, auth, криптография | #41, #47, #50, #51, #53 |
| **Track E** — Persistence/productization | БД, Docker, операции | #40, #43, #46, #52, #54, #63, #66, #69, #71–#74 |

---

## Track A — Reviewer clarity

- [#38](https://github.com/safal207/Living-Relational-Identity-LRI/issues/38) Portfolio hardening: make LRI reviewer-ready ✅ *closed*
- [#39](https://github.com/safal207/Living-Relational-Identity-LRI/issues/39) Добавить лицензию ✅ *closed*
- [#29](https://github.com/safal207/Living-Relational-Identity-LRI/issues/29) Discussion: should AI preserve identity as a living process?

## Track B — Research/spec concepts

- [#30](https://github.com/safal207/Living-Relational-Identity-LRI/issues/30) Collect examples of identity freezing in AI systems
- [#31](https://github.com/safal207/Living-Relational-Identity-LRI/issues/31) Add glossary entries for LRI identity-governance terms
- [#32](https://github.com/safal207/Living-Relational-Identity-LRI/issues/32) Compare LRI with privacy, consent, and data minimization frameworks
- [#33](https://github.com/safal207/Living-Relational-Identity-LRI/issues/33) Define "silent authorship" in human-AI interaction
- [#34](https://github.com/safal207/Living-Relational-Identity-LRI/issues/34) Write a consent drift example for long-term AI memory
- [#37](https://github.com/safal207/Living-Relational-Identity-LRI/issues/37) Bridge issue: clarify LPI vs LRI boundaries
- ~~#35~~ *duplicate of #37, closed*

## Track C — Engineering hygiene

### P0 — Immediate
- [#44](https://github.com/safal207/Living-Relational-Identity-LRI/issues/44) Исправить систему импортов — убрать `sys.path.append()`
- [#48](https://github.com/safal207/Living-Relational-Identity-LRI/issues/48) Унифицировать язык кода и комментариев на английский
- [#42](https://github.com/safal207/Living-Relational-Identity-LRI/issues/42) Настроить CI (GitHub Actions)
- [#49](https://github.com/safal207/Living-Relational-Identity-LRI/issues/49) Создать Makefile / Taskfile
- [#45](https://github.com/safal207/Living-Relational-Identity-LRI/issues/45) Добавить pre-commit (ruff, black, YAML валидация)

### P1 — Next
- [#55](https://github.com/safal207/Living-Relational-Identity-LRI/issues/55) Покрыть API-роуты тестами (FastAPI TestClient)
- [#56](https://github.com/safal207/Living-Relational-Identity-LRI/issues/56) Покрыть адаптеры тестами (CLI, UI, multi-agent)
- [#58](https://github.com/safal207/Living-Relational-Identity-LRI/issues/58) Добавить code coverage (pytest-cov >70%)
- [#60](https://github.com/safal207/Living-Relational-Identity-LRI/issues/60) Интегрировать Playwright-тест в pytest
- [#64](https://github.com/safal207/Living-Relational-Identity-LRI/issues/64) Property-based testing (Hypothesis)

### P2 — Later
- [#57](https://github.com/safal207/Living-Relational-Identity-LRI/issues/57) Добавить typing-аннотации во все функции
- [#59](https://github.com/safal207/Living-Relational-Identity-LRI/issues/59) Вынести HTML/CSS/JS из Python в Jinja2
- [#61](https://github.com/safal207/Living-Relational-Identity-LRI/issues/61) Заменить `print()` на `logging`
- [#65](https://github.com/safal207/Living-Relational-Identity-LRI/issues/65) Обработка ошибок для edge-кейсов
- [#68](https://github.com/safal207/Living-Relational-Identity-LRI/issues/68) Конфигурация через Pydantic Settings
- [#62](https://github.com/safal207/Living-Relational-Identity-LRI/issues/62) Автоматическая валидация YAML-схем
- [#67](https://github.com/safal207/Living-Relational-Identity-LRI/issues/67) OpenAPI/Swagger документация
- [#70](https://github.com/safal207/Living-Relational-Identity-LRI/issues/70) CONTRIBUTING.md

## Track D — Security hardening

Not production certification. LRI remains a protocol/reference artifact.

- [#41](https://github.com/safal207/Living-Relational-Identity-LRI/issues/41) Вынести секреты в переменные окружения / `.env`
- [#47](https://github.com/safal207/Living-Relational-Identity-LRI/issues/47) Реализовать нормальную авторизацию (убрать заглушку)
- [#50](https://github.com/safal207/Living-Relational-Identity-LRI/issues/50) Проверка криптографических подписей
- [#51](https://github.com/safal207/Living-Relational-Identity-LRI/issues/51) Ролевая модель (admin, agent, observer)
- [#53](https://github.com/safal207/Living-Relational-Identity-LRI/issues/53) Rate limiting и аудит запросов

## Track E — Persistence/productization

- [#40](https://github.com/safal207/Living-Relational-Identity-LRI/issues/40) Docker (Dockerfile + docker-compose)
- [#43](https://github.com/safal207/Living-Relational-Identity-LRI/issues/43) БД (SQLite / PostgreSQL) вместо in-memory
- [#46](https://github.com/safal207/Living-Relational-Identity-LRI/issues/46) Storage-слой на репозиторий с БД
- [#52](https://github.com/safal207/Living-Relational-Identity-LRI/issues/52) Миграции БД (Alembic)
- [#54](https://github.com/safal207/Living-Relational-Identity-LRI/issues/54) DMP-лог из JSONL в БД
- [#63](https://github.com/safal207/Living-Relational-Identity-LRI/issues/63) Архитектурные диаграммы (Mermaid)
- [#66](https://github.com/safal207/Living-Relational-Identity-LRI/issues/66) Обновить документы (убрать устаревшие ссылки)
- [#69](https://github.com/safal207/Living-Relational-Identity-LRI/issues/69) Примеры на TypeScript / Rust / Go
- [#71](https://github.com/safal207/Living-Relational-Identity-LRI/issues/71) Health-check эндпоинт `/health`
- [#72](https://github.com/safal207/Living-Relational-Identity-LRI/issues/72) Prometheus метрики + Grafana
- [#73](https://github.com/safal207/Living-Relational-Identity-LRI/issues/73) Graceful shutdown
- [#74](https://github.com/safal207/Living-Relational-Identity-LRI/issues/74) Backup стратегия (DMP + identity state)
