from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME ="BQGIzloAfcxANJrgKzZPAYhP5memCBvbKhdV0DvNBp4bnMykBy5M-FIl1mOuPtXxjhgI9cEGQssFzspFMqL-QVQFxFU-l-fJHvNy_IJgLDQYrbPC5bqJwPvcvqBbXim7v9T8s1frMpYcVGDctJYA_KRTrhlc5j1eVZv3nWKlBmOi5ii2r7qw4p856c-2rSOf4b_b_eGB3NL0qCwWgaz83kCd2L6nTCZ2YQisRf0rsjn_9E-CDUYl4a8Y0QpyzQkr8zOLu-pK9a8i4N-pUxT2fTPeLZ_UEXxPR77__LBMIJ2-ZGlzeEkGiJSOBeCWZ6G8PmbO1jaYGiWKxbpyauSIc1FQSEcreQAAAAG7QxP_AA"

BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AbishnoiMF")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Abishnoi_bots")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5938660179").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5938660179").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
