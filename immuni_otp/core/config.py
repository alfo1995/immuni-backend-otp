#   Copyright (C) 2020 Presidenza del Consiglio dei Ministri.
#   Please refer to the AUTHORS file for more information.
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <https://www.gnu.org/licenses/>.

from datetime import timedelta

from decouple import config

OTP_CACHE_REDIS_URL: str = config("OTP_CACHE_REDIS_URL", default="redis://localhost:6379/0")
OTP_CACHE_REDIS_MAX_CONNECTIONS: int = config(
    "OTP_CACHE_REDIS_MAX_CONNECTIONS", default=10, cast=int
)
OTP_EXPIRATION_SECONDS: int = config(
    "OTP_EXPIRATION_SECONDS", default=int(timedelta(minutes=2.5).total_seconds()), cast=int
)
