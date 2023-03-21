from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.journal import journal

tags = [
    {
        "name": "Journal",
        "description": "API for Journal Entries"
    },
]

origins = [
    "*"
]

app = FastAPI(
    title='On Track API',
    version='0.1.0',
    docs_url="/api/docs",
    openapi_tags=tags
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(journal.router, prefix='/api/journal')
