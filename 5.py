# -*- coding: utf-8 -*-

from enum import Enum
from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

####
#   код пока без изменений
####

import asyncio
from concurrent.futures import ThreadPoolExecutor as pool

timeout_seconds = timedelta(seconds=15).total_seconds()

class Response(Enum):
    Success = 1
    RetryAfter = 2
    Failure = 3

class ApplicationStatusResponse(Enum):
    Success = 1
    Failure = 2
  
@dataclass
class ApplicationResponse:
    application_id:     str
    status:             ApplicationStatusResponse
    description:        str
    last_request_time:  datetime
    retriesCount:       Optional[int]

async def get_application_status1(identifier: str) -> Response:
    # Метод, возвращающий статус заявки
    pass

async def get_application_status2(identifier: str) -> Response:
    # Метод, возвращающий статус заявки
    pass

async def perform_operation(identifier: str) -> ApplicationResponse:
    # TODO дополнить реализацию
    pass

# Инициализация asyncio loop
loop = asyncio.get_event_loop()

# Запуск асинхронной операции
result = loop.run_until_complete(perform_operation())
print(result)